from 常量 import 版本信息, 版权信息, 帮助信息
from 运行 import 运行

def 欢迎() -> None:
    print(版本信息)
    print(版权信息)
    print(帮助信息)

if __name__ == '__main__':
    欢迎()
    运行()