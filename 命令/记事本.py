from _run_background_process import run_background_process
import os
from 颜色 import *

帮助 = '打开记事本'

def 运行(参数: list) -> int:
    print(f'{蓝色}正在启动记事本 ...{重置}', end=' ', flush=True)
    try:
        if os.name == 'nt':
            run_background_process(['notepad'])
        else:
            run_background_process([
                'wine',
                'notepad'
            ])
    except Exception:
        import traceback
        错误('失败')
        traceback.print_exc()
        return 1
    else:
        成功('成功')
        return 0