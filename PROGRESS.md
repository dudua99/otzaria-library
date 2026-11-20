# Library v38 delta — progress

Updated: 2026-11-20T16:16:24Z

## Phases done
```
v1: 18240s
v2: 18432s
v1.done
v2.done
```

## Current phase
```
=== [2026-11-20T05:45:17Z] PHASE v1 START
=== [2026-11-20T10:49:17Z] PHASE v1 DONE (18240s)
=== [2026-11-20T10:49:17Z] PHASE v2 START
=== [2026-11-20T15:56:29Z] PHASE v2 DONE (18432s)
=== [2026-11-20T15:56:29Z] PHASE compress_v1 START
```

## Last 30 log lines
```

> Task :generator-common:kmpPartiallyResolvedDependenciesChecker
> Task :core:kmpPartiallyResolvedDependenciesChecker
> Task :dao:kmpPartiallyResolvedDependenciesChecker
> Task :generator-common:checkKotlinGradlePluginConfigurationErrors SKIPPED
> Task :dao:checkKotlinGradlePluginConfigurationErrors SKIPPED
> Task :core:checkKotlinGradlePluginConfigurationErrors SKIPPED
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

> Task :generator-common:compressLineContent
Picked up JAVA_TOOL_OPTIONS: -Djavax.net.ssl.trustStore=/etc/ssl/certs/java/cacerts -Djavax.net.ssl.trustStoreType=JKS -Dhttps.proxyHost=127.0.0.1 -Dhttps.proxyPort=36609 -Dhttp.nonProxyHosts=localhost|127.0.0.1|::1|127.*|0.*|::|169.254.*|api.anthropic.com|api-staging.anthropic.com|api-pr-preview.an
Picked up _JAVA_OPTIONS: -XX:+UnlockDiagnosticVMOptions -XX:DisableIntrinsic=_base64_encodeBlock,_base64_decodeBlock
```

## Machine
```
               total        used        free      shared  buff/cache   available
Mem:           16087        1462        1398          12       13569       14624
Swap:              0           0           0
/dev/vda        252G   43G   27G  62% /
 16:16:24 up 10:45,  0 user,  load average: 2.44, 2.57, 2.17
-rw-r--r--  1 root root 10393022464 Nov 20 15:56 seforim.db
-rw-r--r--  1 root root  1155768320 Nov 20 15:42 seforim.db.buildstate
-rw-r--r--  1 root root  1157332992 Nov 20 10:36 seforim.db.buildstate.v1
-rw-------  1 root root        3946 Nov 20 11:54 seforim.db.link-import-metrics.json
-rw-r--r--  1 root root 10396733440 Nov 20 16:16 seforim.db.v1
```
