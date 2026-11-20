# Library v38 delta — progress

Updated: 2026-11-20T15:46:21Z

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
Info: (BuildLineDhIndexCli) line_dh: dropping noisy book 7715 'קרן לדוד על שבת' (distinct=0.80, oneWord=0.96, opener=0.56, hits=25)
Info: (BuildLineDhIndexCli) line_dh: dropping noisy book 7716 'קרן לדוד על תענית' (distinct=1.00, oneWord=1.00, opener=0.42, hits=12)
Info: (BuildLineDhIndexCli) line_dh: dropping noisy book 7745 'ראש יוסף על ביצה' (distinct=0.46, oneWord=1.00, opener=0.25, hits=490)
Info: (BuildLineDhIndexCli) line_dh: dropping noisy book 7746 'ראש יוסף על ברכות' (distinct=0.46, oneWord=1.00, opener=0.30, hits=668)
Info: (BuildLineDhIndexCli) line_dh: dropping noisy book 7747 'ראש יוסף על חולין' (distinct=0.19, oneWord=1.00, opener=0.35, hits=1624)
Info: (BuildLineDhIndexCli) line_dh: dropping noisy book 7763 'כפות תמרים על סוכה' (distinct=0.42, oneWord=1.00, opener=0.17, hits=293)
Info: (BuildLineDhIndexCli) line_dh: dropping noisy book 7768 'שפת אמת על ברכות' (distinct=0.30, oneWord=0.89, opener=0.19, hits=27)
Info: (BuildLineDhIndexCli) line_dh: dropping noisy book 7769 'שפת אמת על עירובין' (distinct=0.06, oneWord=0.71, opener=0.02, hits=231)
Info: (BuildLineDhIndexCli) line_dh: dropping noisy book 7770 'שפת אמת על פסחים' (distinct=0.08, oneWord=0.72, opener=0.08, hits=372)
Info: (BuildLineDhIndexCli) line_dh: dropping noisy book 7771 'שפת אמת על שבת' (distinct=0.09, oneWord=0.71, opener=0.10, hits=689)
Info: (BuildLineDhIndexCli) line_dh: dropping noisy book 7772 'שפת אמת על בכורות' (distinct=0.14, oneWord=1.00, opener=0.03, hits=74)
Info: (BuildLineDhIndexCli) line_dh: dropping noisy book 7773 'שפת אמת על זבחים' (distinct=0.09, oneWord=1.00, opener=0.04, hits=343)
Info: (BuildLineDhIndexCli) line_dh: dropping noisy book 7774 'שפת אמת על כריתות' (distinct=0.12, oneWord=1.00, opener=0.11, hits=65)
Info: (BuildLineDhIndexCli) line_dh: dropping noisy book 7775 'שפת אמת על מנחות' (distinct=0.12, oneWord=1.00, opener=0.12, hits=353)
Info: (BuildLineDhIndexCli) line_dh: dropping noisy book 7776 'שפת אמת על מעילה' (distinct=0.20, oneWord=1.00, opener=0.07, hits=44)
Info: (BuildLineDhIndexCli) line_dh: dropping noisy book 7777 'שפת אמת על ערכין' (distinct=0.19, oneWord=1.00, opener=0.13, hits=75)
Info: (BuildLineDhIndexCli) line_dh: dropping noisy book 7778 'שפת אמת על תמורה' (distinct=0.16, oneWord=1.00, opener=0.10, hits=86)
Info: (BuildLineDhIndexCli) line_dh: dropping noisy book 7791 'תפארת יעקב על גיטין' (distinct=0.06, oneWord=1.00, opener=0.49, hits=2642)
Info: (BuildLineDhIndexCli) line_dh: dropping noisy book 7959 'חידושי הרן (מיוחס לו) על שבת' (distinct=0.49, oneWord=1.00, opener=0.20, hits=1823)
Info: (BuildLineDhIndexCli) line_dh: dropping noisy book 7972 'אור הישר (ירושלמי)' (distinct=0.03, oneWord=1.00, opener=0.02, hits=1145)
Info: (BuildLineDhIndexCli) line_dh: dropping noisy book 8032 'שקל הקדש על ירושלמי שקלים' (distinct=0.25, oneWord=1.00, opener=0.52, hits=677)
Info: (BuildLineDhIndexCli) line_dh: dropping noisy book 8085 'תורת נתנאל על התורה' (distinct=0.53, oneWord=0.98, opener=0.38, hits=217)
Info: (BuildLineDhIndexCli) line_dh: 1273279 dibburim over 2631 bold-format (35 of them lead-bold) + 107 dash-format books (2143 books below threshold, 294 books dropped as non-dibbur marking; eligible=4892 metadata + 283 reviewed overrides, unreviewed=3010)

> Task :sefariasqlite:buildLineDivineNameIndex
Picked up JAVA_TOOL_OPTIONS: -Djavax.net.ssl.trustStore=/etc/ssl/certs/java/cacerts -Djavax.net.ssl.trustStoreType=JKS -Dhttps.proxyHost=127.0.0.1 -Dhttps.proxyPort=36609 -Dhttp.nonProxyHosts=localhost|127.0.0.1|::1|127.*|0.*|::|169.254.*|api.anthropic.com|api-staging.anthropic.com|api-pr-preview.an
Picked up _JAVA_OPTIONS: -XX:+UnlockDiagnosticVMOptions -XX:DisableIntrinsic=_base64_encodeBlock,_base64_decodeBlock
Info: (BuildLineDivineNames) Reading pinned ForDB archive /home/user/work/dl/fordb_v2.zip (sha256=166c758ca01d6b76ba081e4c39c040de2d3f8e72722b4937736fcfbe593ffc94)
Info: (BuildLineDivineNames) line_divine_name: 500000 lines, 21725 spans
Info: (BuildLineDivineNames) line_divine_name: 1000000 lines, 26164 spans
```

## Machine
```
               total        used        free      shared  buff/cache   available
Mem:           16087        1918        4086          12       10424       14168
Swap:              0           0           0
/dev/vda        252G   47G   22G  69% /
 15:46:21 up 10:15,  0 user,  load average: 1.08, 1.14, 1.06
-rw-r--r--  1 root root 10354024448 Nov 20 15:44 seforim.db
-rw-r--r--  1 root root       32768 Nov 20 15:44 seforim.db-shm
-rw-r--r--  1 root root           0 Nov 20 15:44 seforim.db-wal
-rw-r--r--  1 root root  1155768320 Nov 20 15:42 seforim.db.buildstate
-rw-r--r--  1 root root  1157332992 Nov 20 10:36 seforim.db.buildstate.v1
-rw-------  1 root root        3946 Nov 20 11:54 seforim.db.link-import-metrics.json
-rw-r--r--  1 root root 10396733440 Nov 20 10:49 seforim.db.v1
-rw-r--r--  1 root root       32768 Nov 20 10:50 seforim.db.v1-shm
-rw-r--r--  1 root root           0 Nov 20 10:50 seforim.db.v1-wal
```
