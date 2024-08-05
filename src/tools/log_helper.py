import logging
import colorlog

# 创建一个颜色日志记录器
log = colorlog.getLogger()
log.setLevel(logging.DEBUG)

# 日志style枚举
log_style_enum = {
    "none": "%(message)s",
    "simple": "[%(pathname)s:%(lineno)d]%(message)s",
    "standard": "[%(message_log_color)s%(pathname)s:%(lineno)d%(reset)s] %(log_color)s%(message)s",
    "simple_color": "%(log_color)s%(message)s",
    "verbose": "%(log_color)s[%(pathname)s:%(lineno)d] %(message)s",
    "debug": "%(log_color)s[%(pathname)s:%(lineno)d] %(levelname)-8s %(message)s",
}
# 暂时不用冻结
# frozenset_log_style_enum = frozenset(log_style_enum.items())

log_style = "standard"  # 日志输出格式

# 日志style选择
def get_log_style():
    global log_style
    print("log_style:", log_style)
    return log_style_enum[log_style]

# 设置日志输出格式
def set_log_style(style):
    """设置日志输出格式"""
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
            "CRITICAL": "red,bg_white",
            
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