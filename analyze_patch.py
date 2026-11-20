#!/usr/bin/env python3
"""Per-table row counts of patch.db, mapped to books, with old->new samples. Writes OUT/delta.json + OUT/DELTA_draft.md"""
import sqlite3, sys, json, os, collections
try:
    import zstandard
except ImportError:
    zstandard = None
patch, v1p, v2p, out = sys.argv[1:5]
os.makedirs(out, exist_ok=True)
EXPECTED = {8037, 8045, 8061, 6147, 6726, 7952}  # v1-local ids by title (see VERDICT)
P = sqlite3.connect(patch)
V1 = sqlite3.connect(f'file:{v1p}?mode=ro', uri=True)
V2 = sqlite3.connect(f'file:{v2p}?mode=ro', uri=True)
def dctx(db):
    if not zstandard: return None
    try:
        r = db.execute('select dict from zstd_dict limit 1').fetchone()
        return zstandard.ZstdDecompressor(dict_data=zstandard.ZstdCompressionDict(r[0])) if r else None
    except Exception: return None
D = {1: dctx(V1), 2: dctx(V2)}
def show(v, side=2):
    if isinstance(v, bytes):
        if v[:4] == b'\x28\xb5\x2f\xfd' and D.get(side):
            try: v = D[side].decompress(v, max_output_size=1 << 24).decode('utf-8', 'replace')
            except Exception as e: return f'<zstd blob {len(v)}B: {e}>'
        else: return f'<blob {len(v)}B>'
    if isinstance(v, str) and len(v) > 400: v = v[:400] + '…'
    return v
def cols(db, t): return [r[1] for r in db.execute(f'pragma table_info("{t}")')]
def pk(db, t):
    c = [(r[5], r[1]) for r in db.execute(f'pragma table_info("{t}")') if r[5]]
    return [n for _, n in sorted(c)]
title_cache = {}
def title(bid):
    if bid is None: return None
    if bid not in title_cache:
        r = V2.execute('select title from book where id=?', (bid,)).fetchone() or V1.execute('select title from book where id=?', (bid,)).fetchone()
        title_cache[bid] = r[0] if r else '?'
    return title_cache[bid]
def line_book(lid):
    for db in (V2, V1):
        r = db.execute('select bookId from line where id=?', (lid,)).fetchone()
        if r: return r[0]
def books_of(t, row):
    if 'bookId' in row: return [row['bookId']]
    if t == 'book': return [row.get('id')]
    if 'lineId' in row: return [line_book(row['lineId'])]
    if t in ('line_content',): return [line_book(row.get('id'))]
    if t == 'link': return [row.get('sourceBookId'), row.get('targetBookId')]
    if t == 'author' and 'id' in row:
        s = set()
        for db in (V1, V2):
            s |= {r[0] for r in db.execute('select bookId from book_author where authorId=?', (row['id'],))}
        return sorted(s) or [None]
    return [None]
tables = [r[0] for r in P.execute("select name from sqlite_master where type='table' order by name")]
res = {'tables': {}, 'other_tables': {}}
for t in tables:
    if not (t.startswith('upsert_') or t.startswith('delete_')):
        try: res['other_tables'][t] = P.execute(f'select count(*) from "{t}"').fetchone()[0]
        except Exception as e: res['other_tables'][t] = str(e)
        continue
    kind, base = t.split('_', 1)
    n = P.execute(f'select count(*) from "{t}"').fetchone()[0]
    if n == 0: continue
    pc = cols(P, t)
    try: keys = pk(V2, base) or pk(V1, base)
    except Exception: keys = []
    keys = [k for k in keys if k in pc] or pc
    books = collections.Counter(); samples = []
    for i, r in enumerate(P.execute(f'select * from "{t}"')):
        row = dict(zip(pc, r))
        if kind == 'delete':
            full = V1.execute(f'select * from "{base}" where ' + ' and '.join(f'"{k}"=?' for k in keys), [row[k] for k in keys]).fetchone()
            if full: row = dict(zip(cols(V1, base), full))
        bl = books_of(base, row)
        for b in bl: books[b] += 1
        if len(samples) < 10:
            s = {'key': {k: show(row.get(k)) for k in keys}, 'books': [(b, title(b)) for b in bl]}
            if kind == 'upsert':
                old = V1.execute(f'select * from "{base}" where ' + ' and '.join(f'"{k}"=?' for k in keys), [row[k] for k in keys]).fetchone()
                if old is None: s['change'] = 'INSERT'; s['new'] = {k: show(v) for k, v in row.items()}
                else:
                    oc = dict(zip(cols(V1, base), old))
                    s['change'] = 'UPDATE'
                    s['diff'] = {k: [show(oc.get(k), 1), show(v, 2)] for k, v in row.items() if oc.get(k) != v}
                    if not s['diff']: s['diff_note'] = 'identical to v1 row (byte-equal)'
            else:
                s['change'] = 'DELETE'; s['old'] = {k: show(v, 1) for k, v in row.items()}
            samples.append(s)
    res['tables'][t] = {'count': n, 'books': [(b, title(b), c) for b, c in books.most_common()], 'samples': samples,
                        'unexpected_books': sorted({b for b in books if b not in EXPECTED}, key=lambda x: (x is None, x))}
json.dump(res, open(os.path.join(out, 'delta.json'), 'w'), ensure_ascii=False, indent=1, default=str)
L = ['| table | rows | books (id title ×rows) | outside expected set |', '|---|---:|---|---|']
for t, d in res['tables'].items():
    L.append(f"| `{t}` | {d['count']} | " + '; '.join(f'{b} {ti} ×{c}' for b, ti, c in d['books'][:12]) + f" | {d['unexpected_books'][:12]} |")
md = ['# DELTA draft', '', *L, '', '## Non-upsert/delete tables in patch', '```', json.dumps(res['other_tables'], ensure_ascii=False, indent=1), '```', '']
for t, d in res['tables'].items():
    md += [f'## `{t}` — {d["count"]} rows', '```json', json.dumps(d['samples'], ensure_ascii=False, indent=1, default=str), '```', '']
open(os.path.join(out, 'DELTA_draft.md'), 'w').write('\n'.join(md))
print('\n'.join(L))
