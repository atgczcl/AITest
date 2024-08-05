
import sys
from tools.log_helper import log
from tools.log_helper import set_log_style


# 导入模块
import asyncio
# 关键字列表
import keyword


"""
#!/usr/bin/env python
在 Linux/Unix 系统中，你可以在脚本顶部添加以下命令让 Python 脚本可以像 SHELL 脚本一样可直接执行：
#! /usr/bin/env python3.7
./hello.py
默认情况下，Python 3 源码文件以 UTF-8 编码，所有字符串都是 unicode 字符串。 当然你也可以为源码文件指定不同的编码：
# -*- coding: cp-1252 -*-
# -*- coding: utf-8 -*-
"""
'''
三个单引号或双引号之间可以写任何内容，但一般情况下，我们会在文件开头写上文件说明，然后空一行再写代码。
'''
set_log_style("simple")

def test_print(*args):
    #哈哈哈哈哈
    """
    这是一个三引号注释，但是第一个引号必须和函数名在同一行对齐，否则会报错
    """
    print(*args, file=sys.stdout) # print(*args, file=sys.stderr)
print("Hello World")
x = 5
y = 'Hello, 你好呀！'
y = y + ' 你好呀！'
# 字符串变量可以使用单引号或双引号进行声明
x = y
X = 4444
my_list = {x, y, X}
print(x)
print(y)
print(X)
print(my_list)

"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")



# 配置日志
# logging.basicConfig(level=logging.INFO)

# 输出日志
# logging.info("这是第一行日志信息。")
# logging.info("这是第二行日志信息。")
# logging.error("这是错误日志信息。")
# logging.critical("这是严重错误日志信息。")
# logging.debug("这是调试日志信息。")
# logging.warning("这是警告日志信息。")




# 使用日志记录器记录带有颜色的日志
log.debug("这是一条debug级别的日志")
log.info("这是一条info级别的日志")
log.warning("这是一条warning级别的日志")
print()
log.error("这是一条error级别的日志")
print()
log.critical("这是一条critical级别的日志")
log.info(f"x={x}, y={y}, X={X}, my_list={my_list}")
print(f"{x}{y}{X}{my_list}")
log.info(f"{x}{y}{X}{my_list}")

x, y, z = "abc", 123, True
print(str(x)+str(y)+str(z))
log.info(f"x={x}, y={y}, z={z}")
x=y=z=0
log.info(f"x={x}, y={y}, z={z}")


def print_odd_numbers():
    """
    定义一个函数，打印出100以内的奇数：
    如果要在函数内部更改全局变量，请使用 global 关键字。
    """
    global my_list # 初始化my_list为列表，支持索引赋值
    my_list = []
    for i in range(1, 101):
        if i % 2 != 0:
            my_list.append(i)  # 使用append方法添加元素
    log.info(f"奇数列表：{my_list}")

print_odd_numbers()


# 定义一个函数，打印出100以内的奇数，并返回列表
def get_odd_numbers():
    """ 定义一个函数，打印出100以内的奇数，并返回列表 """
    odd_numbers = []
    for i in range(1, 101):
        if i % 2 != 0:
            odd_numbers.append(i)  # 使用append方法添加元素
    log.info(f"奇数列表：{odd_numbers}")
    return odd_numbers

odd_numbers = get_odd_numbers()
print(odd_numbers)
# 被global修饰的my_list变量也被修改了，所以打印出来是：[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
log.info(f"my_list={my_list}")

set_log_style("standard")

my_list = 9
log.info(f"my_list={my_list}")
# 斐波那契数列生成
async def fibonacci(n):
    """ 
    定义一个函数，打印出斐波那契数列前n项
    如果要在函数内部更改全局变量，请使用 global 关键字。
    要在函数内部更改全局变量的值，请使用 global 关键字引用该变量s
    """
    global my_list # 初始化my_list为列表，支持索引赋值
    my_list = []
    a, b = 0, 1
    await asyncio.sleep(0)  # 模拟耗时操作
    for i in range(n):
        # print(a, end='\n')
        my_list.append(a)  # 使用append方法添加元素
        a, b = b, a+b
    log.info(f"斐波那契数列[[[：{my_list}")

async def main():
    await fibonacci(10)
log.info(f"斐波那契数列[：{my_list}")
asyncio.run(main())
c1 = 1 + 2j
c2 = 3 - 4j
log.info(f"c1={c1}, c2={c2}")
c3 = c1 + c2
log.info(f"c3={c3}")
x = bytes(5)
log.info(f"x={x}")
x = bytearray(5)
log.info(f"x={x}")


mv = memoryview(b'hello')
arr = bytearray(mv)
arr[0] = ord('H')
log.info(f"arr={arr}")  # 输出：b'Hello'
print(arr)  # 输出：b'Hello'

# list
x = [1, 2, 3]
y = ["xx", "yy", "zz"]
log.info(f"x={x}, y={y}, {type(y)}")
x = dict(name="Bill", age=36)
log.info(f"x={x}, {type(x)}")
x = set([1, 2, 3, 2, 1])
log.info(f"x={x}, {type(x)}")
x = list(("apple", "banana", "cherry"))
log.info(f"x={x}, {type(x)}")

# tuple
x = (1, 2, 3)
y = ("xx", "yy", "zz")
log.info(f"x={x}, y={y}, {type(y)}")
#关键字
log.info(f"关键字列表：{keyword.kwlist}")


# nonlocal 关键字学习
def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20
        print("inner:", x)
    inner()
    print("outer:", x)
outer()  # 输出：inner: 20, outer: 20


# 装饰器学习
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


@my_decorator
def say_whee():
    """" 定义一个函数，打印出“Something is happening before the function is called. Whee! Something is happening after the function is called.,装饰器就是把自己定义的函数作为参数传给另一个函数，并返回一个新的函数（意思就是把原函数的功能加上了额外的功能，通俗一点就是把自己装饰起来，穿上衣服等的人模狗样！）"""
    print("Whee!")


say_whee()  # 输出：Something is happening before the function is called. Whee! Something is happening after the function is called.

# Python 中单引号和双引号使用完全相同，但单引号和双引号不能匹配。

x = u"你好，世界！ this is an unicode string"
y = r"你好，世界！, this is a raw string\n"
z = x.replace("h", 'H')  # 字符串是不可变的，所以不能修改
log.info(f"x={x}, y={y}, z={z}")
# x[0] = 'H'  # 字符串是不可变的，所以不能修改  [头下标: 尾下标: 步长]
log.info(f"x={x[0:-1]}, y={y[0:]}, z={z[1::2]}，xyz={x+y+z}") # 切片操作
t = "你好，世界"
#计算string长度
log.info(f"len(x)={len(x)}, len(y)={len(y)}, len(z)={len(z)}, len(xyz)={len(t)}")
#判断是否为空字符串, python 中没有char类型，所以判断空字符串可以用not x or y or z
log.info(f"x is null? {not x}, y is null? {not y}, z is null? {not z}")

# 测试input()函数
def test_input():
    """
    测试input()函数
    """
    input("\n\nPress Enter to continue...")
    x = int(input("请输入一个数字："))
    log.info(f"你输入的内容是：{type(x)}")
    sys.stdout.write(str(x) + '\n')

# 测试代码组
def test_code_group():
    """
    测试代码组
    """
    log.info("测试代码组")
    expression = True
    if expression :
        
        log.info("表达式为True1111")
    elif expression :

        log.info("表达式为True222")
    else:
        log.info("表达式为False")
test_code_group()