"""Build v2 inputs: v38 otzaria tree + v38 ForDB with the three fix branches applied at packaged paths."""
import json, os, subprocess, sys, hashlib, shutil
REPO = '/home/user/otzaria-library'
OTZ1, OTZ2 = '/home/user/work/in/otz1', '/home/user/work/in/otz2'
FDB1, FDB2 = '/home/user/work/fordb1', '/home/user/work/fordb2'
BR = ['origin/fix/dicta-gershayim-2766', 'origin/fix/pnei-hamelech-author-3468', 'origin/fix/hearot-note-markers-3775']
ROOTS = [l.strip() for l in """Ben-YehudaToOtzaria/ספרים/אוצריא
DictaToOtzaria/ערוך/ספרים/אוצריא
OnYourWayToOtzaria/ספרים/אוצריא
OraytaToOtzaria/ספרים/אוצריא
tashmaToOtzaria/ספרים/אוצריא
sefariaToOtzaria/sefaria_export/ספרים/אוצריא
sefariaToOtzaria/sefaria_api/ספרים/אוצריא
MoreBooks/ספרים/אוצריא
KSK/ספרים/אוצריא
wikiJewishBooksToOtzaria/ספרים/אוצריא
wikisourceToOtzaria/ספרים/אוצריא
ToratEmetToOtzaria/ספרים/אוצריא
pninimToOtzaria/ספרים/אוצריא
National-LibraryToOtzaria/ספרים/אוצריא
yam-HaHachmaToOtzaria/ספרים/אוצריא
BeitAharonVeYisraelToOtzaria/ספרים/אוצריא""".splitlines()]
log = []
def git(*a): return subprocess.run(['git', '-C', REPO, '-c', 'core.quotepath=off', *a], capture_output=True, check=True).stdout
def packaged(p):
    for r in ROOTS:
        if p.startswith(r + '/'): return 'אוצריא/' + p[len(r) + 1:]
    return None
def hunks(br, path):
    out = git('diff', '-U0', 'origin/main', br, '--', path).decode()
    hs, cur = [], None
    for l in out.split('\n'):
        if l.startswith('@@'):
            cur = ([], []); hs.append(cur)
        elif cur is not None and l.startswith('-') and not l.startswith('---'): cur[0].append(l[1:])
        elif cur is not None and l.startswith('+') and not l.startswith('+++'): cur[1].append(l[1:])
    return hs
def apply_hunks(br, path, target):
    s = open(target, encoding='utf-8').read()
    for old, new in hunks(br, path):
        o, n = '\n'.join(old) + '\n', '\n'.join(new) + '\n'
        c = s.count(o)
        if c == 1:
            s = s.replace(o, n)
            log.append(f'{br} {path}: exact hunk {len(old)}->{len(new)} lines'); continue
        if len(old) != len(new): sys.exit(f'FAIL {target}: hunk found {c}x: {old[:1]}')
        lines = s.split('\n')
        for a, b in zip(old, new):
            pre = 0
            while pre < min(len(a), len(b)) and a[pre] == b[pre]: pre += 1
            suf = 0
            while suf < min(len(a), len(b)) - pre and a[-1 - suf] == b[-1 - suf]: suf += 1
            key = a[:len(a) - suf]; nkey = b[:len(b) - suf]
            idx = [i for i, l in enumerate(lines) if l.startswith(key)]
            if len(idx) != 1: sys.exit(f'FAIL {target}: line key found {len(idx)}x: {key[:80]}')
            i = idx[0]; lines[i] = nkey + lines[i][len(key):]
            log.append(f'{br} {path}: line-prefix edit at target line {i+1}: ...{a[max(0,pre-30):len(a)-suf]!r} -> ...{b[max(0,pre-30):len(b)-suf]!r}')
        s = '\n'.join(lines)
    # replace file (break hardlink)
    os.unlink(target); open(target, 'w', encoding='utf-8').write(s)

shutil.rmtree(OTZ2, ignore_errors=True); shutil.rmtree(FDB2, ignore_errors=True)
subprocess.run(['cp', '-al', OTZ1, OTZ2], check=True)
subprocess.run(['cp', '-a', FDB1, FDB2], check=True)
man_path = os.path.join(OTZ2, 'files_manifest.json')
man_raw = open(man_path, 'rb').read(); man = json.loads(man_raw)
canon = lambda d: json.dumps(d, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()
assert canon(man) == man_raw.rstrip(b'\n') or canon(man) + b'\n' == man_raw, 'manifest canonical form differs'
trail = b'\n' if man_raw.endswith(b'\n') else b''
for br in BR:
    for line in git('diff', '--name-status', '-M', 'origin/main', br).decode().splitlines():
        st, *paths = line.split('\t')
        if st.startswith('R'):
            old, new = paths
            po, pn = packaged(old), packaged(new)
            if po:
                src = os.path.join(OTZ2, po); dst = os.path.join(OTZ2, pn)
                assert os.path.exists(src) and not os.path.exists(dst), (src, dst)
                os.rename(src, dst); log.append(f'{br} RENAME {po} -> {pn}')
            if old in man:
                man[new] = man.pop(old); log.append(f'{br} manifest key {old} -> {new}')
            if st != 'R100': sys.exit('non-R100 rename ' + line)
            continue
        p = paths[0]; pk = packaged(p)
        if pk and not p.endswith('.txt'):
            t = os.path.join(OTZ2, pk); assert os.path.exists(t), t
            apply_hunks(br, p, t)
            if p in man:
                man[p]['hash'] = hashlib.sha256(open(t, 'rb').read()).hexdigest(); log.append(f'{br} manifest hash {p}')
        elif pk:
            t = os.path.join(OTZ2, pk); assert os.path.exists(t), t
            data = git('show', f'{br}:{p}')
            assert open(t, 'rb').read() == git('show', f'origin/main:{p}'), 'zip != main for ' + p
            os.unlink(t); open(t, 'wb').write(data)
            if p in man:
                man[p]['hash'] = hashlib.sha256(data).hexdigest()
                log.append(f'{br} manifest hash {p}')
            log.append(f'{br} REPLACE {pk}')
        elif p == 'metadata.json':
            apply_hunks(br, p, os.path.join(OTZ2, 'metadata.json'))
        elif p.startswith('ForDB/'):
            apply_hunks(br, p, os.path.join(FDB2, p))
        else:
            log.append(f'{br} not packaged: {p}')
os.unlink(man_path); open(man_path, 'wb').write(canon(man) + trail)
print('\n'.join(log))
