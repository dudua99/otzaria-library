# Library v38 delta — progress

Updated: 2026-11-20T15:16:19Z

## Phases done
```
v1: 18240s
v1.done
```

## Current phase
```
=== [2026-11-20T05:45:17Z] PHASE v1 START
=== [2026-11-20T10:49:17Z] PHASE v1 DONE (18240s)
=== [2026-11-20T10:49:17Z] PHASE v2 START
```

## Last 30 log lines
```
Info: (DatabaseGenerator) Book 8159 'קובץ פרשיות ומועדים': 5000/5242 lines (95%)
Info: (DatabaseGenerator) books 2345/2705 (86.6%) · lines 4.0M · toc 762.0K · elapsed 3:12:53 · eta ~29:36
Info: (DatabaseGenerator) Book 8166 'תורת המנחה': 1000/6260 lines (15%)
Info: (DatabaseGenerator) Book 8166 'תורת המנחה': 2000/6260 lines (31%)
Info: (DatabaseGenerator) Book 8166 'תורת המנחה': 3000/6260 lines (47%)
Info: (DatabaseGenerator) Book 8166 'תורת המנחה': 4000/6260 lines (63%)
Info: (DatabaseGenerator) Book 8166 'תורת המנחה': 5000/6260 lines (79%)
Info: (DatabaseGenerator) Book 8166 'תורת המנחה': 6000/6260 lines (95%)
Info: (DatabaseGenerator) books 2359/2705 (87.2%) · lines 4.0M · toc 766.0K · elapsed 3:13:54 · eta ~28:26
Info: (DatabaseGenerator) Book 8183 'תרגום ותפסיר רסג': 2000/11885 lines (16%)
Info: (DatabaseGenerator) Book 8183 'תרגום ותפסיר רסג': 4000/11885 lines (33%)
Info: (DatabaseGenerator) Book 8183 'תרגום ותפסיר רסג': 6000/11885 lines (50%)
Info: (DatabaseGenerator) Book 8183 'תרגום ותפסיר רסג': 8000/11885 lines (67%)
Info: (DatabaseGenerator) Book 8183 'תרגום ותפסיר רסג': 10000/11885 lines (84%)
Info: (DatabaseGenerator) Book 8185 'מפקתא פשיטתא': 1000/6043 lines (16%)
Info: (DatabaseGenerator) Book 8185 'מפקתא פשיטתא': 2000/6043 lines (33%)
Info: (DatabaseGenerator) Book 8185 'מפקתא פשיטתא': 3000/6043 lines (49%)
Info: (DatabaseGenerator) Book 8185 'מפקתא פשיטתא': 4000/6043 lines (66%)
Info: (DatabaseGenerator) Book 8185 'מפקתא פשיטתא': 5000/6043 lines (82%)
Info: (DatabaseGenerator) Book 8185 'מפקתא פשיטתא': 6000/6043 lines (99%)
Info: (DatabaseGenerator) Otzaria book import (phase 1): books=2367/2705 lines=4087334 tocEntries=766866 directories=371 skipped=0 acronymBooks=906 hearotMerged=338 elapsed=3:14:49
Info: (DatabaseGenerator) Acronyms of renamed books: 453 terms carried to 69 books: 'חידושי אגדות על בבא מציעא' → 'מהרש"א - חידושי אגדות על בבא מציעא' (6, same id); 'חידושי אגדות על זבחים' → 'מהרש"א - חידושי אגדות �
Info: (DatabaseGenerator) Acronyms of renamed books: 1 renames not followed (add the new title to the Acronymizer if it is the same book): 'גר"א על סדר עולם רבה' → 'הגר"א על סדר עולם רבה' (the title changed words, not only added or dropped them)
Info: (DatabaseGenerator) Building category_closure table (phase 1)...
Info: (DatabaseGenerator) Recorded source hashes for 2367 / 2705 Otzaria books
Warn: (DatabaseGenerator) source hashes: 338 of 2705 Otzaria books have no source hash — they are fully reprocessed every cycle
Warn: (DatabaseGenerator) source hashes: 338 not recorded — merged into a base book as inline notes (הערות על אבן ספיר, הערות על אגדות מספר המעשים (ילקוט מדרשים), הערות על אגדת ימות המשיח (ילקוט מדרשים), הערות על 
Info: (DatabaseGenerator) report written to /home/user/SeforimLibrary/build/generator-reports/otzaria-source-hashes-not-recorded.json
Info: (DatabaseGenerator) Phase 1 completed.
Info: (IdAllocator) Phase-8 GC pruned orphan entries: lines=0, staleLineKeys=41, tocEntries=0, altStructures=0, altEntries=0, links=19, sourceHashes=3
```

## Machine
```
               total        used        free      shared  buff/cache   available
Mem:           16087        7901        1268          12        7261        8186
Swap:              0           0           0
/dev/vda        252G   53G   17G  76% /
 15:16:19 up  9:45,  0 user,  load average: 1.05, 1.03, 1.00
-rw-r--r--  1 root root  5192069120 Nov 20 11:56 seforim.db
-rw-r--r--  1 root root  1155768320 Nov 20 11:56 seforim.db.buildstate
-rw-r--r--  1 root root  1121366016 Nov 20 15:16 seforim.db.buildstate.candidate.tmp
-rw-r--r--  1 root root        1024 Nov 20 15:14 seforim.db.buildstate.candidate.tmp-journal
-rw-r--r--  1 root root  1157332992 Nov 20 10:36 seforim.db.buildstate.v1
-rw-r--r--  1 root root  9765847040 Nov 20 15:14 seforim.db.candidate
-rw-------  1 root root        3946 Nov 20 11:54 seforim.db.link-import-metrics.json
-rw-r--r--  1 root root 10396733440 Nov 20 10:49 seforim.db.v1
-rw-r--r--  1 root root       32768 Nov 20 10:50 seforim.db.v1-shm
-rw-r--r--  1 root root           0 Nov 20 10:50 seforim.db.v1-wal
```
