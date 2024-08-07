import logging
import colorlog
import builtins
import inspect
import sys
from datetime import datetime

# 创建一个颜色日志记录器
log = colorlog.getLogger()
# 日志style枚举
log_style_enum = {
    "none": "%(message)s",
    "simple": "[%(asctime)s %(pathname)s:%(lineno)d] %(message)s",
    "standard": "[%(message_log_color)s%(asctime)s %(pathname)s:%(lineno)d%(reset)s] %(log_color)s%(message)s",
    "simple_color": "%(log_color)s%(asctime)s %(message)s",
    "verbose": "%(log_color)s[%(asctime)s%(pathname)s:%(lineno)d] %(message)s",
    "debug": "%(log_color)s[%(asctime)s%(pathname)s:%(lineno)d] %(levelname)-8s %(message)s",
}

logging.basicConfig(
    filename='output.log', 
    level=logging.DEBUG, 
    encoding='utf-8',
    format='[%(asctime)s %(pathname)s:%(lineno)d] %(message)s'
    )
log.setLevel(logging.NOTSET)
# 暂时不用冻结
# frozenset_log_style_enum = frozenset(log_style_enum.items())

log_style = "standard"  # 日志输出格式

# 设置日志是否打印
def set_log_level(level):
    """设置日志级别
    level: logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL, logging.NOTSET"""
    log.setLevel(level)

# 日志style选择
def get_log_style():
    global log_style
    # print("log_style:", log_style)
    return log_style_enum[log_style]

# 设置日志输出格式
def set_log_style(style):
    """设置日志输出格式, style: simple, standard, simple_color, verbose, debug"""
    global log_style
    log_style = style
    # 设置日志格式 
    set_log_format(get_log_format())
    print("set_log_style:", log_style)


# 获取日志格式
def get_log_format():
    """设置日志格式"""
    # 创建一个颜色日志格式器
    log_format = colorlog.ColoredFormatter(
        # "%(log_color)s%(levelname)s:(message)s",
        # "%(log_color)s%(message)s",
        # "%(log_color)s[%(filename)s:%(lineno)d] %(message)s",
        # "[%(reset)s%(filename)s:%(lineno)d]%(log_color)s%(message)s",
        # "[%(message_log_color)s%(filename)s:%(lineno)d%(reset)s] %(log_color)s%(levelname)-8s %(message)s",
        # "%(log_color)s%(levelname)s:%(name)s:%(message)s",
        get_log_style(),
        log_colors={
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "white,bg_red",
            
        },
        secondary_log_colors={
            "message":{
            "DEBUG": "blue",
            "INFO": "blue",
            "WARNING": "blue",
            "ERROR": "blue",
            "CRITICAL": "blue",
            },
        },
        reset=True,  # 重置颜色
        style="%",
    )
    return log_format

# 设置日志格式
def set_log_format(log_format):
    """设置日志格式"""
    console_handler.setFormatter(log_format)

# 创建一个日志处理器，将日志输出到控制台
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
# 设置默认第一次初始化的日志格式
set_log_format(get_log_format())
# console_handler.setFormatter(log_format)

# 将日志处理器添加到日志记录器
# log.addHandler(console_handler)

# # 替换原生的 print 函数
# builtins.print = log_print

# 保存原始的 print 函数
original_print = builtins.print

# # ... 重定向 print 函数的代码 ...

# # 恢复原始的 print 函数
# builtins.print = original_print
# 定义颜色代码
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
magenta = "\033[35m"
cyan = "\033[36m"
reset = "\033[0m"
def get_color_text(text, color_code):
    ''' 获取带颜色的文本
    # 定义颜色代码
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
magenta = "\033[35m"
cyan = "\033[36m"
reset = "\033[0m"
    '''
    # 构造完整的 ANSI 转义序列 ansi_escape = f"\033[{display_code};{color_code};{background_code}m"
    # ansi_escape = f"\033[{color_code};32;1m"
    ansi_escape = f"\033[{color_code}m"
    # 重置颜色
    reset_escape = "\033[0m"
    return f"{ansi_escape}{text}{reset_escape}"

def my_print(*args, sep=' ', end='\n', file=sys.stdout, flush=False, log_file='output.log'):
    # 获取调用者的栈帧信息
    stack = inspect.stack()
    # 调用者信息在栈中的位置通常是第三个元素（索引为2）
    # 但为了安全起见，我们检查栈的深度
    if len(stack) > 1:
        # 获取调用者的文件名和行号
        caller_frame = stack[1]
        filename = caller_frame.filename
        lineno = caller_frame.lineno
        # 为了简洁，我们只显示文件名和行号的一部分
        filename = filename.split('/')[-1]  # 假设路径是以'/'分隔的
        # 获取当前时间
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f%z")
        # 将文件路径和行号添加到输出中
        # args = (f"[File '{filename}':{lineno}] ",) + args
        # args = (f"['{current_time} {filename}':{lineno}] ",) + args
        color_head = (f"{blue}[{current_time} {filename}:{lineno}] {reset}{green}",)
        head = (f"[{current_time} {filename}:{lineno}] ",)
        color_args = color_head + args
        args = head + args 
    
    # 将输出内容转换为字符串
    output = sep.join(map(str, args)) + end
    color_output = sep.join(map(str, color_args)) + end + reset
    # 设置颜色为绿色，背景无，显示方式为高亮显示 32;40;1

    # output = get_color_text(output, 34)  # 设置颜色为绿色，背景色为黑色，显示方式为高亮显示
    # output = get_color_text(output, 34, 0, 0)  # 设置颜色为蓝色，背景色为黑色，显示方式为高亮显示
    # 写入到标准输出
    file.write(color_output)
    if flush:
        file.flush()
    
    # 删除字符中的颜色代码
    # output = output.replace(red, '').replace(green, '').replace(yellow, '').replace(blue, '').replace(magenta, '').replace(cyan, '').replace(reset, '')
    # 同时将内容写入到日志文件
    with open(log_file, 'a', encoding='utf-8') as logfile:
        logfile.write(output)

# builtins.print = my_print

def set_log_printable(printable):
    """设置日志是否可以打印"""
    global log_printable
    log_printable = printable
    if log_printable:
        builtins.print = my_print
        log.addHandler(console_handler)
    else:
        builtins.print = original_print
        log.removeHandler(console_handler)
# 日志是否可以打印
log_printable = True
# 设置日志是否可以打印
set_log_printable(True)