import logging
import colorlog

# 创建一个颜色日志记录器
log = colorlog.getLogger()
log.setLevel(logging.DEBUG)

# 创建一个颜色日志格式器
log_format = colorlog.ColoredFormatter(
    # "%(log_color)s%(levelname)s:(message)s",
    # "%(log_color)s%(message)s",
    # "%(log_color)s[%(filename)s:%(lineno)d] %(message)s",
    # "[%(reset)s%(filename)s:%(lineno)d]%(log_color)s%(message)s",
    # "[%(message_log_color)s%(filename)s:%(lineno)d%(reset)s] %(log_color)s%(levelname)-8s %(message)s",
    # "%(log_color)s%(levelname)s:%(name)s:%(message)s",
    "[%(message_log_color)s%(filename)s:%(lineno)d%(reset)s] %(log_color)s%(message)s",
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

# 创建一个日志处理器，将日志输出到控制台
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(log_format)

# 将日志处理器添加到日志记录器
log.addHandler(console_handler)