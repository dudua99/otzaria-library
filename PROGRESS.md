# Library v38 delta — progress

Updated: 2026-11-20T16:46:26Z

## Phases done
```
compress_v1: 1409s
compress_v2: 1343s
v1: 18240s
v2: 18432s
compress_v1.done
compress_v2.done
v1.done
v2.done
```

## Current phase
```
=== [2026-11-20T15:56:29Z] PHASE compress_v1 START
=== [2026-11-20T16:19:58Z] PHASE compress_v1 DONE (1409s)
=== [2026-11-20T16:19:58Z] PHASE compress_v2 START
=== [2026-11-20T16:42:21Z] PHASE compress_v2 DONE (1343s)
=== [2026-11-20T16:42:21Z] PHASE patch START
```

## Last 30 log lines
```
> Task :generator-common:jvmProcessResources UP-TO-DATE
> Task :generator-common:processJvmMainResources SKIPPED
> Task :dao:generateCommonMainSeforimDbInterface UP-TO-DATE
> Task :dao:jvmProcessResources NO-SOURCE
> Task :dao:processJvmMainResources SKIPPED
> Task :core:compileKotlinJvm UP-TO-DATE
> Task :core:compileJvmMainJava NO-SOURCE
> Task :core:jvmProcessResources NO-SOURCE
> Task :core:processJvmMainResources SKIPPED
> Task :core:jvmMainClasses UP-TO-DATE
> Task :core:jvmJar UP-TO-DATE
> Task :dao:compileKotlinJvm UP-TO-DATE
> Task :dao:compileJvmMainJava NO-SOURCE
> Task :dao:jvmMainClasses UP-TO-DATE
> Task :dao:jvmJar UP-TO-DATE
> Task :generator-common:compileKotlinJvm UP-TO-DATE
> Task :generator-common:compileJvmMainJava NO-SOURCE
> Task :generator-common:jvmMainClasses UP-TO-DATE
> Task :generator-common:jvmJar UP-TO-DATE

> Task :generator-common:producePatchAndVerify
Picked up JAVA_TOOL_OPTIONS: -Djavax.net.ssl.trustStore=/etc/ssl/certs/java/cacerts -Djavax.net.ssl.trustStoreType=JKS -Dhttps.proxyHost=127.0.0.1 -Dhttps.proxyPort=36609 -Dhttp.nonProxyHosts=localhost|127.0.0.1|::1|127.*|0.*|::|169.254.*|api.anthropic.com|api-staging.anthropic.com|api-pr-preview.an
Picked up _JAVA_OPTIONS: -XX:+UnlockDiagnosticVMOptions -XX:DisableIntrinsic=_base64_encodeBlock,_base64_decodeBlock
Info: (PatchPipelineCli) Producing patch /home/user/SeforimLibrary/build/seforim.db.v1 → /home/user/SeforimLibrary/build/seforim.db at /home/user/SeforimLibrary/build/patch-v1-v2.db (v1 → v2, schema 7 → 7)
Info: (PatchPipelineCli) Shipping 97 sqlite_stat1 row(s) as stat1_snapshot
Info: (PatchPipelineCli) Produced patch.db at /home/user/SeforimLibrary/build/patch-v1-v2.db — upserts=2524, deletes=205 (from v1 to v2)
Info: (PatchPipelineCli) patch.db produced — upserts=2524, deletes=205
Info: (PatchPipelineCli)   upserts by table: {author=1, book=6, book_author=1, line=2353, line_content=41, line_toc=41, link=19, line_divine_name=3, line_note=58, schema_meta=1}
Info: (PatchPipelineCli)   deletes by table: {author=1, book_author=1, line=41, line_content=41, line_toc=41, link=19, line_divine_name=3, line_note=58}
Info: (PatchPipelineCli) Patch size within budget: patch.db 786432 B is 0.0% of the new seforim.db (10393022464 B); limit is 100000.0%
```

## Machine
```
               total        used        free      shared  buff/cache   available
Mem:           16087        1503        1313          12       13613       14584
Swap:              0           0           0
/dev/vda        252G   53G   17G  76% /
 16:46:26 up 11:15,  0 user,  load average: 1.07, 1.76, 2.15
-rw-r--r--  1 root root      786432 Nov 20 16:44 patch-v1-v2.db
-rw-r--r--  1 root root 10393022464 Nov 20 16:42 seforim.db
-rw-r--r--  1 root root  1155768320 Nov 20 15:42 seforim.db.buildstate
-rw-r--r--  1 root root  1157332992 Nov 20 10:36 seforim.db.buildstate.v1
-rw-------  1 root root        3946 Nov 20 11:54 seforim.db.link-import-metrics.json
-rw-r--r--  1 root root 10396733440 Nov 20 16:19 seforim.db.v1
-rw-r--r--  1 root root 10396733440 Nov 20 16:44 verify-patch-v1-v2.db
-rw-r--r--  1 root root       32768 Nov 20 16:45 verify-patch-v1-v2.db-shm
-rw-r--r--  1 root root           0 Nov 20 16:45 verify-patch-v1-v2.db-wal
```
