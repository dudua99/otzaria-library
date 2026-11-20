import sqlite3, zstandard, json, collections
V1=sqlite3.connect('file:seforim.db.v1?mode=ro',uri=True); V2=sqlite3.connect('file:seforim.db?mode=ro',uri=True); P=sqlite3.connect('patch-v1-v2.db')
def dz(db):
    d=db.execute('select dict from zstd_dict').fetchone()[0]; return zstandard.ZstdDecompressor(dict_data=zstandard.ZstdCompressionDict(d))
D1,D2=dz(V1),dz(V2)
dec=lambda d,b: d.decompress(b,max_output_size=1<<24).decode()
r={}
# upsert_line split
ul=P.execute('select id,bookId,lineIndex,heRef from upsert_line').fetchall()
newids={i for (i,) in P.execute('select id from upsert_line_content')}
upd=[x for x in ul if x[0] not in newids]
r['upsert_line_heRef_only']=collections.Counter(b for _,b,_,_ in upd)
bad=[]
for i,b,li,h in upd:
    o=V1.execute('select bookId,lineIndex,heRef,tocEntryId,charCount from line where id=?',(i,)).fetchone()
    n=V2.execute('select bookId,lineIndex,heRef,tocEntryId,charCount from line where id=?',(i,)).fetchone()
    if o[:2]!=n[:2] or o[3:]!=n[3:] or o[2].replace('עהת','עה״ת')!=n[2]: bad.append((i,o,n))
r['heRef_only_violations']=len(bad)
# content of replaced lines: same (bookId,lineIndex), compare text
cmp=[]
for (did,) in P.execute('select id from delete_line'):
    b,li=V1.execute('select bookId,lineIndex from line where id=?',(did,)).fetchone()
    nid=V2.execute('select id from line where bookId=? and lineIndex=?',(b,li)).fetchone()[0]
    o=dec(D1,V1.execute('select content from line_content where id=?',(did,)).fetchone()[0]); n=dec(D2,V2.execute('select content from line_content where id=?',(nid,)).fetchone()[0])
    cmp.append((b,li,o==n,o[:120],n[:120]))
r['replaced_lines_same_text']={f'{b}:{s}':c for (b,s),c in collections.Counter((b,s) for b,_,s,_,_ in cmp).items()}
r['replaced_line_examples']=[c for c in cmp if not c[2]][:3]+[c for c in cmp if c[2]][:1]
# notes
for db,nm in ((V1,'v1'),(V2,'v2')):
    r['notes_'+nm]=db.execute('select l.bookId,count(*),sum(n.hasMarker) from line_note n join line l on l.id=n.lineId where l.bookId in (6726,7952) group by 1').fetchall()
# links mapped
def links(db):
    return sorted(db.execute('select l.sourceBookId,l.sourceLineId,l.targetBookId,t.lineIndex,l.connectionTypeId from link l join line t on t.id=l.targetLineId where l.targetBookId=7952 or l.sourceBookId=7952'))
r['links_7952_equal_modulo_lineid']=links(V1)==links(V2); r['links_7952_count']=len(links(V2))
for t in ['book','line','link','line_note','author','book_author','category']:
    r['count_'+t]=(V1.execute(f'select count(*) from {t}').fetchone()[0],V2.execute(f'select count(*) from {t}').fetchone()[0])
r['author_642_users_v1']=V1.execute('select count(*) from book_author where authorId=642').fetchone()[0]
r['author_new_v2']=V2.execute("select a.id,a.name,(select count(*) from book_author where authorId=a.id) from author a where name like '%מאזוז%'").fetchall()
r['pnei_line2']=[dec(D1,V1.execute("select c.content from line l join line_content c on c.id=l.id where l.bookId=6147 and l.lineIndex=1").fetchone()[0]),dec(D2,V2.execute("select c.content from line l join line_content c on c.id=l.id where l.bookId=6147 and l.lineIndex=1").fetchone()[0])]
print(json.dumps(r,ensure_ascii=False,indent=1,default=str))
json.dump(r,open('/home/user/work/out/checks.json','w'),ensure_ascii=False,indent=1,default=str)
