from _run_background_process import run_background_process
from 颜色 import *

帮助 = '运行我的世界'

基础目录 = '/Users/yhm/Desktop/hmcl/minecraft'
命令 = [
    '/Users/yhm/Java/17.0.18/bin/java',
    '-Xmx8817m',
    '-Dfile.encoding=UTF-8',
    '-Dsun.stdout.encoding=UTF-8',
    '-Dsun.stderr.encoding=UTF-8',
    '-Djava.rmi.server.useCodebaseOnly=true',
    '-Dcom.sun.jndi.rmi.object.trustURLCodebase=false',
    '-Dcom.sun.jndi.cosnaming.object.trustURLCodebase=false',
    '-Dlog4j2.formatMsgNoLookups=true',
    f'-Dlog4j.configurationFile={基础目录}/versions/1.20.1/log4j2.xml',
    f'-Dminecraft.client.jar={基础目录}/versions/1.20.1/1.20.1.jar',
    '-Xdock:name=我的世界 一点二十点一',
    f'-Xdock:icon={基础目录}/assets/objects/f0/f00657542252858a721e715a2e888a9226404e35',
    '-Duser.home=/Users/yhm/Desktop/hmcl',
    '-Djava.net.useSystemProxies=true',
    '-XX:+UnlockExperimentalVMOptions',
    '-XX:+UnlockDiagnosticVMOptions',
    '-XX:+UseG1GC',
    '-XX:G1MixedGCCountTarget=5',
    '-XX:G1NewSizePercent=20',
    '-XX:G1ReservePercent=20',
    '-XX:MaxGCPauseMillis=50',
    '-XX:G1HeapRegionSize=32m',
    '-XX:-OmitStackTraceInFastThrow',
    '-XX:-DontCompileHugeMethods',
    '-XX:MaxNodeLimit=240000',
    '-XX:NodeLimitFudgeFactor=8000',
    '-XX:TieredCompileTaskTimeout=10000',
    '-XX:ReservedCodeCacheSize=400M',
    '-XX:NonNMethodCodeHeapSize=12M',
    '-XX:ProfiledCodeHeapSize=194M',
    '-XX:NmethodSweepActivity=1',
    '-Dfml.ignoreInvalidMinecraftCertificates=true',
    '-Dfml.ignorePatchDiscrepancies=true',
    '-XstartOnFirstThread',
    f'-Djava.library.path={基础目录}/versions/1.20.1/natives-macos-arm64',
    f'-Djna.tmpdir={基础目录}/versions/1.20.1/natives-macos-arm64',
    f'-Dorg.lwjgl.system.SharedLibraryExtractPath={基础目录}/versions/1.20.1/natives-macos-arm64',
    f'-Dio.netty.native.workdir={基础目录}/versions/1.20.1/natives-macos-arm64',
    '-Dminecraft.launcher.brand=你好我的世界启动器',
    '-Dminecraft.launcher.version=三点十四点零点三四二',
    '-cp',
    f'{基础目录}/libraries/ca/weblite/java-objc-bridge/1.1/java-objc-bridge-1.1.jar:{基础目录}/libraries/com/github/oshi/oshi-core/6.2.2/oshi-core-6.2.2.jar:{基础目录}/libraries/com/google/code/gson/gson/2.10/gson-2.10.jar:{基础目录}/libraries/com/google/guava/failureaccess/1.0.1/failureaccess-1.0.1.jar:{基础目录}/libraries/com/google/guava/guava/31.1-jre/guava-31.1-jre.jar:{基础目录}/libraries/com/ibm/icu/icu4j/71.1/icu4j-71.1.jar:{基础目录}/libraries/com/mojang/authlib/4.0.43/authlib-4.0.43.jar:{基础目录}/libraries/com/mojang/blocklist/1.0.10/blocklist-1.0.10.jar:{基础目录}/libraries/com/mojang/brigadier/1.1.8/brigadier-1.1.8.jar:{基础目录}/libraries/com/mojang/datafixerupper/6.0.8/datafixerupper-6.0.8.jar:{基础目录}/libraries/com/mojang/logging/1.1.1/logging-1.1.1.jar:{基础目录}/libraries/com/mojang/patchy/2.2.10/patchy-2.2.10.jar:{基础目录}/libraries/com/mojang/text2speech/1.17.9/text2speech-1.17.9.jar:{基础目录}/libraries/commons-codec/commons-codec/1.15/commons-codec-1.15.jar:{基础目录}/libraries/commons-io/commons-io/2.11.0/commons-io-2.11.0.jar:{基础目录}/libraries/commons-logging/commons-logging/1.2/commons-logging-1.2.jar:{基础目录}/libraries/io/netty/netty-buffer/4.1.82.Final/netty-buffer-4.1.82.Final.jar:{基础目录}/libraries/io/netty/netty-codec/4.1.82.Final/netty-codec-4.1.82.Final.jar:{基础目录}/libraries/io/netty/netty-common/4.1.82.Final/netty-common-4.1.82.Final.jar:{基础目录}/libraries/io/netty/netty-handler/4.1.82.Final/netty-handler-4.1.82.Final.jar:{基础目录}/libraries/io/netty/netty-resolver/4.1.82.Final/netty-resolver-4.1.82.Final.jar:{基础目录}/libraries/io/netty/netty-transport-classes-epoll/4.1.82.Final/netty-transport-classes-epoll-4.1.82.Final.jar:{基础目录}/libraries/io/netty/netty-transport-native-unix-common/4.1.82.Final/netty-transport-native-unix-common-4.1.82.Final.jar:{基础目录}/libraries/io/netty/netty-transport/4.1.82.Final/netty-transport-4.1.82.Final.jar:{基础目录}/libraries/it/unimi/dsi/fastutil/8.5.9/fastutil-8.5.9.jar:{基础目录}/libraries/net/java/dev/jna/jna-platform/5.12.1/jna-platform-5.12.1.jar:{基础目录}/libraries/net/java/dev/jna/jna/5.12.1/jna-5.12.1.jar:{基础目录}/libraries/net/sf/jopt-simple/jopt-simple/5.0.4/jopt-simple-5.0.4.jar:{基础目录}/libraries/org/apache/commons/commons-compress/1.21/commons-compress-1.21.jar:{基础目录}/libraries/org/apache/commons/commons-lang3/3.12.0/commons-lang3-3.12.0.jar:{基础目录}/libraries/org/apache/httpcomponents/httpclient/4.5.13/httpclient-4.5.13.jar:{基础目录}/libraries/org/apache/httpcomponents/httpcore/4.4.15/httpcore-4.4.15.jar:{基础目录}/libraries/org/apache/logging/log4j/log4j-api/2.19.0/log4j-api-2.19.0.jar:{基础目录}/libraries/org/apache/logging/log4j/log4j-core/2.19.0/log4j-core-2.19.0.jar:{基础目录}/libraries/org/apache/logging/log4j/log4j-slf4j2-impl/2.19.0/log4j-slf4j2-impl-2.19.0.jar:{基础目录}/libraries/org/joml/joml/1.10.5/joml-1.10.5.jar:{基础目录}/libraries/org/lwjgl/lwjgl-glfw/3.3.1/lwjgl-glfw-3.3.1.jar:{基础目录}/libraries/org/lwjgl/lwjgl-glfw/3.3.1/lwjgl-glfw-3.3.1-natives-macos.jar:{基础目录}/libraries/org/lwjgl/lwjgl-glfw/3.3.1/lwjgl-glfw-3.3.1-natives-macos-arm64.jar:{基础目录}/libraries/org/lwjgl/lwjgl-jemalloc/3.3.1/lwjgl-jemalloc-3.3.1.jar:{基础目录}/libraries/org/lwjgl/lwjgl-jemalloc/3.3.1/lwjgl-jemalloc-3.3.1-natives-macos.jar:{基础目录}/libraries/org/lwjgl/lwjgl-jemalloc/3.3.1/lwjgl-jemalloc-3.3.1-natives-macos-arm64.jar:{基础目录}/libraries/org/lwjgl/lwjgl-openal/3.3.1/lwjgl-openal-3.3.1.jar:{基础目录}/libraries/org/lwjgl/lwjgl-openal/3.3.1/lwjgl-openal-3.3.1-natives-macos.jar:{基础目录}/libraries/org/lwjgl/lwjgl-openal/3.3.1/lwjgl-openal-3.3.1-natives-macos-arm64.jar:{基础目录}/libraries/org/lwjgl/lwjgl-opengl/3.3.1/lwjgl-opengl-3.3.1.jar:{基础目录}/libraries/org/lwjgl/lwjgl-opengl/3.3.1/lwjgl-opengl-3.3.1-natives-macos.jar:{基础目录}/libraries/org/lwjgl/lwjgl-opengl/3.3.1/lwjgl-opengl-3.3.1-natives-macos-arm64.jar:{基础目录}/libraries/org/lwjgl/lwjgl-stb/3.3.1/lwjgl-stb-3.3.1.jar:{基础目录}/libraries/org/lwjgl/lwjgl-stb/3.3.1/lwjgl-stb-3.3.1-natives-macos.jar:{基础目录}/libraries/org/lwjgl/lwjgl-stb/3.3.1/lwjgl-stb-3.3.1-natives-macos-arm64.jar:{基础目录}/libraries/org/lwjgl/lwjgl-tinyfd/3.3.1/lwjgl-tinyfd-3.3.1.jar:{基础目录}/libraries/org/lwjgl/lwjgl-tinyfd/3.3.1/lwjgl-tinyfd-3.3.1-natives-macos.jar:{基础目录}/libraries/org/lwjgl/lwjgl-tinyfd/3.3.1/lwjgl-tinyfd-3.3.1-natives-macos-arm64.jar:{基础目录}/libraries/org/lwjgl/lwjgl/3.3.1/lwjgl-3.3.1.jar:{基础目录}/libraries/org/lwjgl/lwjgl/3.3.1/lwjgl-3.3.1-natives-macos.jar:{基础目录}/libraries/org/lwjgl/lwjgl/3.3.1/lwjgl-3.3.1-natives-macos-arm64.jar:{基础目录}/libraries/org/slf4j/slf4j-api/2.0.1/slf4j-api-2.0.1.jar:{基础目录}/versions/1.20.1/1.20.1.jar',
    'net.minecraft.client.main.Main',
    '--username',
    '玩家',
    '--version',
    '一点二十点一',
    '--gameDir',
    f'{基础目录}',
    '--assetsDir',
    f'{基础目录}/assets',
    '--assetIndex',
    '5',
    '--uuid',
    '10241024102410241024102410241024',
    '--accessToken',
    'd1906f5484e84bc2aefc22a6729b338c',
    '--versionType',
    '你好我的世界启动器 三点十四点零点三四二',
    '--width',
    '854',
    '--height',
    '480'
]

加载完成日志关键词 = '[Render thread/INFO]: Created: 128x128x0 minecraft:textures/atlas/mob_effects.png-atlas'

def 运行(参数: list) -> int:
    print(f'{蓝色}正在启动我的世界 ...{重置}')
    try:
        进程 = run_background_process(
            命令,
            cwd=基础目录,
            text=True
        )
    except Exception:
        import traceback
        错误('我的世界启动失败')
        traceback.print_exc()
        return 1
    else:
        for 日志条目 in 进程.stdout:
            print(日志条目, end='', flush=True)
            if 加载完成日志关键词 in 日志条目:
                break
        成功('我的世界启动成功')
        return 0