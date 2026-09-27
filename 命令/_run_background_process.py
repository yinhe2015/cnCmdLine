import subprocess
import sys

def run_background_process(*args, **kwargs) -> subprocess.Popen:
    if sys.platform == 'win32':
        # Windows 系统

        # 核心参数: 让子进程完全脱离主进程
        CREATE_NEW_PROCESS_GROUP = 0x00000200
        DETACHED_PROCESS = 0x00000008
        
        return subprocess.Popen(
            *args,
            **kwargs,

            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE,
            creationflags=DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP,
            close_fds=True
        )
    else:
        # Linux / macOS 系统
        return subprocess.Popen(
            *args,
            **kwargs,

            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE,
            start_new_session=True,  # 关键: 独立会话
            close_fds=True
        )