# Rebuild a ForDB zip exactly as fordb_archive.build() does, minus check_coverage
# (the v38 ForDB predates gemara_daf_alt_toc.csv / inline_marker_alt_toc.csv).
import sys; sys.path.insert(0, '/home/user/otzaria-library/.github/scripts')
import fordb_archive as fa
from pathlib import Path
fa.check_coverage = lambda paths: None
repo, out = Path(sys.argv[1]), Path(sys.argv[2])
print(fa.build(repo, out))
