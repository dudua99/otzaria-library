# Library v38 delta — progress

Updated: 2026-11-20T10:45:59Z

## Phases done
```
```

## Current phase
```
=== [2026-11-20T05:45:17Z] PHASE v1 START
```

## Last 30 log lines
```
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
Info: (BuildLineDivineNames) Reading pinned ForDB archive /home/user/work/dl/fordb_latest.zip (sha256=50cf9d0715580d579b6bb0c7cb41ce04de1bea2a527fbabf3846d68f9cb08455)
Info: (BuildLineDivineNames) line_divine_name: 500000 lines, 21725 spans
Info: (BuildLineDivineNames) line_divine_name: 1000000 lines, 26164 spans
Info: (BuildLineDivineNames) line_divine_name: 1500000 lines, 32237 spans
Info: (BuildLineDivineNames) line_divine_name: 2000000 lines, 44660 spans
Info: (BuildLineDivineNames) line_divine_name: 2500000 lines, 49618 spans
Info: (BuildLineDivineNames) line_divine_name: 3000000 lines, 51396 spans
Info: (BuildLineDivineNames) line_divine_name: 3500000 lines, 115350 spans
Info: (BuildLineDivineNames) line_divine_name: 4000000 lines, 119593 spans
Info: (BuildLineDivineNames) line_divine_name: 4500000 lines, 121386 spans
Info: (BuildLineDivineNames) line_divine_name: 5000000 lines, 132441 spans
Info: (BuildLineDivineNames) line_divine_name: 5500000 lines, 141798 spans
Info: (BuildLineDivineNames) line_divine_name: 6000000 lines, 143136 spans
Info: (BuildLineDivineNames) line_divine_name: 6500000 lines, 143731 spans
Info: (BuildLineDivineNames) line_divine_name: 7000000 lines, 144515 spans
```

## Machine
```
               total        used        free      shared  buff/cache   available
Mem:           16087        1877        4048          12       10503       14210
Swap:              0           0           0
/dev/vda        252G   37G   33G  53% /
 10:45:59 up  5:15,  0 user,  load average: 1.00, 1.05, 1.06
-rw-r--r--  1 root root 10353115136 Nov 20 10:37 seforim.db
-rw-r--r--  1 root root       32768 Nov 20 10:42 seforim.db-shm
-rw-r--r--  1 root root      420272 Nov 20 10:43 seforim.db-wal
-rw-r--r--  1 root root  1157332992 Nov 20 10:36 seforim.db.buildstate
-rw-------  1 root root        3946 Nov 20 06:49 seforim.db.link-import-metrics.json
```
