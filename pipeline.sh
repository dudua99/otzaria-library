#!/bin/bash
# v1 (v38 inputs) -> v2 (v38 inputs + 3 fixes) -> compress -> patch+verify -> analyze
set -o pipefail
export LANG=C.UTF-8 LC_ALL=C.UTF-8
export JAVA_HOME=/usr/lib/jvm/java-25-openjdk-amd64 PATH=/usr/lib/jvm/java-25-openjdk-amd64/bin:$PATH
W=/home/user/work; S=$W/state; R=/home/user/SeforimLibrary; B=$R/build
cd $R
G="./gradlew --no-daemon --no-configuration-cache --stacktrace"
FORDB1_SHA=50cf9d0715580d579b6bb0c7cb41ce04de1bea2a527fbabf3846d68f9cb08455
FORDB2_SHA=$(sha256sum $W/dl/fordb_v2.zip | cut -d' ' -f1)
ts(){ date -u +%FT%TZ; }
step(){ echo; echo "=== [$(ts)] PHASE $1 START"; }
done_(){ echo "=== [$(ts)] PHASE $1 DONE ($(( $(date +%s) - $2 ))s)"; echo "$(( $(date +%s) - $2 ))" > $S/$1.done; }
fail(){ echo "=== [$(ts)] PHASE $1 FAILED"; echo "$1" > $S/FAILED; exit 1; }
rm -f $S/FAILED

if [ ! -f $S/v1.done ]; then
  step v1; t=$(date +%s)
  rm -f $B/seforim.db $B/seforim.db-* $B/seforim.db.buildstate $B/seforim.db.v1 $B/seforim.db.buildstate.v1
  $G generateSeforimDb -PdbVersion=1 -PexportDir=$W/in/sefaria -PsourceDir=$W/in/otz1 \
     -PforDbArchive=$W/dl/fordb_latest.zip -PforDbSha256=$FORDB1_SHA -PimageCacheDir=$W/imgcache \
     -PinMemoryDb=false -x :packaging:downloadLexicalDb || fail v1
  V=$(sqlite3 $B/seforim.db "SELECT value FROM schema_meta WHERE key='db_version'"); [ "$V" = 1 ] || fail v1-stamp
  mv $B/seforim.db $B/seforim.db.v1; mv $B/seforim.db.buildstate $B/seforim.db.buildstate.v1
  rm -f $B/lexical.db $B/release_info.txt; ls -la $B; df -h /
  done_ v1 $t
fi

if [ ! -f $S/v2.done ]; then
  step v2; t=$(date +%s)
  rm -f $B/seforim.db $B/seforim.db-*
  cp $B/seforim.db.buildstate.v1 $B/seforim.db.buildstate
  $G generateSeforimDb -PdbVersion=2 -PtoVersion=2 -PexportDir=$W/in/sefaria -PsourceDir=$W/in/otz2 \
     -PforDbArchive=$W/dl/fordb_v2.zip -PforDbSha256=$FORDB2_SHA -PimageCacheDir=$W/imgcache \
     -PinMemoryDb=false -x :packaging:downloadLexicalDb || fail v2
  V=$(sqlite3 $B/seforim.db "SELECT value FROM schema_meta WHERE key='db_version'"); [ "$V" = 2 ] || fail v2-stamp
  rm -f $B/lexical.db; ls -la $B; df -h /
  done_ v2 $t
fi

for side in v1 v2; do
  if [ ! -f $S/compress_$side.done ]; then
    step compress_$side; t=$(date +%s)
    db=$B/seforim.db; [ $side = v1 ] && db=$B/seforim.db.v1
    $G :generator-common:compressLineContent -PdbPath=$db || fail compress_$side
    done_ compress_$side $t
  fi
done

if [ ! -f $S/patch.done ]; then
  step patch; t=$(date +%s)
  rm -f $B/catalog.pb $B/patch-v1-v2.db $B/patch-v1-v2.db.manifest.json
  $G :generator-common:producePatchAndVerify -PprevDb=$B/seforim.db.v1 -PnewDb=$B/seforim.db \
     -Pout=$B/patch-v1-v2.db -PfromVersion=1 -PtoVersion=2 -PmaxDeltaUncompressedRatio=1000 || fail patch
  ls -la $B/patch-v1-v2.db*; cat $B/patch-v1-v2.db.manifest.json
  done_ patch $t
fi

step analyze; t=$(date +%s)
python3 $W/scripts/analyze_patch.py $B/patch-v1-v2.db $B/seforim.db.v1 $B/seforim.db $W/out || fail analyze
done_ analyze $t
echo "=== [$(ts)] PIPELINE COMPLETE"
touch $S/PIPELINE_COMPLETE
