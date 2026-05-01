from 颜色 import *
from 常量 import 退出命令, 帮助命令, 缩进
from importlib.util import spec_from_file_location, module_from_spec
import sys
import os

命令目录 = '命令'
sys.path.append(命令目录)

def 打印命令条目(名称: str, 命令与参数: str) -> None:
    用颜色打印(f'{缩进}{名称}: {命令与参数}', 蓝色)

def 加载命令(命令: str, 文件: str) -> object:
    模块规格 = spec_from_file_location(命令, 文件)
    模块对象 = module_from_spec(模块规格)
    模块规格.loader.exec_module(模块对象)
    return 模块对象

def 处理命令(命令: str, 参数: list) -> int:
    if 命令.startswith(('_', '.')):
        错误(f'命令 {命令} 是内部工具 或 隐藏文件')
        return 0

    if 命令 in 帮助命令:
        用颜色打印('可用命令:', 绿色)

        打印命令条目('退出', ' | '.join(退出命令))
        打印命令条目('帮助', ' | '.join(帮助命令))

        for 命令文件 in os.listdir(命令目录):
            if 命令文件.endswith('.py') and not 命令文件.startswith(('_', '.')):
                命令名 = 命令文件[:-3]
                路径 = os.path.join(命令目录, 命令文件)
                打印命令条目(命令名, 加载命令(命令名, 路径).帮助)

        return 0
    
    路径 = os.path.join(命令目录, 命令 + '.py')
    if not os.path.exists(路径):
        错误(f'命令 {命令} 不存在')
        return 127

    命令对象 = 加载命令(命令, 路径)
    try:
        return 命令对象.运行(参数)
    except KeyboardInterrupt:
        错误('^C')
        return 130
    except Exception:
        import traceback
        错误(f'命令 {命令} 运行时出错')
        traceback.print_exc()
        return 1
