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
log.addHandler(console_handler)
# 重定向 print 函数
# def log_print(*args, sep=" ", end="\n"):
#         """重定向 print 函数，则输出换行符"""
#         output = sep.join(map(str, args)) + end
#         log.info(output)

# # 替换原生的 print 函数
# builtins.print = log_print

# # 保存原始的 print 函数
# original_print = builtins.print

# # ... 重定向 print 函数的代码 ...

# # 恢复原始的 print 函数
# builtins.print = original_print


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
        args = (f"[{current_time} {filename}:{lineno}] ",) + args
    
    # # 将输出内容转换为字符串
    # output = sep.join(map(str, args)) + end
    # global log_style_enum
    # global log_style
    # 创建一个颜色日志格式器
    # log_format = colorlog.ColoredFormatter(
    #     "%(log_color)s%(message)s",
    #     log_colors={
    #         "DEBUG": "cyan",
    #         "INFO": "green",
    #         "WARNING": "yellow",
    #         "ERROR": "red",
    #         "CRITICAL": "white, bg_red",
    #     },
    #     reset=True,  # 重置颜色
    #     style="%",
    # )
    # 将输出内容转换为字符串
    output = sep.join(map(str, args)) + end
    # log_record = logging.makeLogRecord({
    #     "name": "my_logger",  # 日志记录器的名字
    #     "level": logging.INFO,  # 日志级别
    #     "msg": output,  # 日志消息
    #     "args": (),  # 日志消息的参数
    #     "exc_info": None,  # 异常信息
    #     "func": None,  # 函数名
    #     "filename": filename,  # 文件名
    #     "lineno": lineno,  # 行号
    #     })
    # # 使用颜色日志格式器格式化输出
    # colored_output = log_format.format(log_record)
    
    # 写入到标准输出
    file.write(output)
    if flush:
        file.flush()
    
    # 同时将内容写入到日志文件
    with open(log_file, 'a', encoding='utf-8') as logfile:
        logfile.write(output)

builtins.print = my_print