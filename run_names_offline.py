# Run validate_fordb_book_names.py with SEFARIA_FETCH=1, serving www.sefaria.org/api/index/
# from the v38 Sefaria export's table_of_contents.json (sefaria.org is blocked here).
import sys, io, runpy, urllib.request
TOC = '/home/user/work/in/sefaria/table_of_contents.json'
class R(io.BytesIO):
    def __enter__(self): return self
    def __exit__(self, *a): return False
real = urllib.request.urlopen
def fake(req, *a, **k):
    url = req.full_url if hasattr(req, 'full_url') else req
    if 'sefaria.org/api/index' in url: return R(open(TOC, 'rb').read())
    return real(req, *a, **k)
urllib.request.urlopen = fake
sys.path.insert(0, '/home/user/otzaria-library/.github/scripts')
sys.argv = ['.github/scripts/validate_fordb_book_names.py'] + sys.argv[1:]
runpy.run_path(sys.argv[0], run_name='__main__')
