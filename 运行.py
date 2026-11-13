from 颜色 import *
from 常量 import 提示信息
from 处理命令 import 处理命令
from 常量 import 退出命令

def 运行() -> None:
    while True:
        try:
            完整命令 = 用颜色输入(f'\n{提示信息}', 黄色, 蓝色)
        except (KeyboardInterrupt, EOFError):
            错误('^C')
            continue
        完整命令 = 完整命令.strip()

        if not 完整命令:
            continue

        分割 = 完整命令.split()
        命令 = 分割[0]
        参数 = [] if len(分割) == 1 else 分割[1:]

        if 命令 in 退出命令:
            break

        处理命令(命令, 参数)