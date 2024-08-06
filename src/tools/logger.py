import logging
import colorlog
import builtins

class Logger:
    def __init__(self, log_style="standard"):
        self.logg = colorlog.getLogger()
        self.logg.setLevel(logging.DEBUG)

        # 日志style枚举
        self.log_style_enum = {
            "none": "%(message)s",
            "simple": "[%(pathname)s:%(lineno)d]%(message)s",
            "standard": "[%(message_log_color)s%(pathname)s:%(lineno)d%(reset)s] %(log_color)s%(message)s",
            "simple_color": "%(log_color)s%(message)s",
            "verbose": "%(log_color)s[%(pathname)s:%(lineno)d] %(message)s",
            "debug": "%(log_color)s[%(pathname)s:%(lineno)d] %(levelname)-8s %(message)s",
        }

        self.log_style = log_style
        self.console_handler = logging.StreamHandler()
        self.console_handler.setLevel(logging.DEBUG)
        self.set_log_format(self.get_log_format())
        self.logg.addHandler(self.console_handler)

        # 重定向 print 函数
        self.original_print = builtins.print
        builtins.print = self.log_print

    def get_log_style(self):
        """获取当前的日志样式"""
        return self.log_style_enum[self.log_style]

    def set_log_style(self, style):
        """设置日志输出格式, style: simple, standard, simple_color, verbose, debug"""
        self.log_style = style
        self.set_log_format(self.get_log_format())
        print("set_log_style:", self.log_style)

    def get_log_format(self):
        """设置日志格式"""
        log_format = colorlog.ColoredFormatter(
            self.get_log_style(),
            log_colors={
                "DEBUG": "cyan",
                "INFO": "green",
                "WARNING": "yellow",
                "ERROR": "red",
                "CRITICAL": "red,bg_white",
            },
            secondary_log_colors={
                "message": {
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

    def set_log_format(self, log_format):
        """设置日志格式"""
        self.console_handler.setFormatter(log_format)

    def log_print(self, message: str | None = "\n", *args, **kwargs):
        """重定向 print 函数，空message则输出换行符"""
        if not message:
            self.logg.info("")
        elif args or kwargs:
            self.logg.info(message.format(*args, **kwargs))
        else:
            self.logg.info(message)

    def restore_original_print(self):
        """恢复原始的 print 函数"""
        builtins.print = self.original_print
        
    def debug(self, message: str, *args, **kwargs):
        self.logger.debug(message, *args, **kwargs)

    def info(self, message: str, *args, **kwargs):
        self.logger.info(message, *args, **kwargs)

    def warning(self, message: str, *args, **kwargs):
        self.logger.warning(message, *args, **kwargs)

    def error(self, message: str, *args, **kwargs):
        self.logger.error(message, *args, **kwargs)

    def critical(self, message: str, *args, **kwargs):
        self.logger.critical(message, *args, **kwargs)