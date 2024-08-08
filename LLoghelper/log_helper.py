import logging
import colorlog
import builtins
import inspect
import sys
from datetime import datetime


class LogHelper:
    ''' 日志辅助类 
    Just: from LLoghelper.log_helper import log, logger
    支持log.info, print 等方法提供日志输出、格式设置、颜色设置等功能
    调用方法：
        log.info("This is a test.")
        log.warning("This is a warning.")
        log.error("This is an error.")
        log.critical("This is a critical error.")
        log.debug("This is a debug message.")
    替换原生的 print 函数, 并支持颜色输出：
        print("This is a test.")
    主要功能：
    1. 日志输出到控制台和文件
    2. 日志格式设置：simple, standard, simple_color, verbose, debug
    3. 日志颜色设置：red, green, yellow, blue, magenta, cyan, reset
    4. 日志级别设置：DEBUG, INFO, WARNING, ERROR, CRITICAL, NOTSET
    5. 日志打印控制：可以控制日志是否可以打印到控制台和文件

    '''

    #字符串颜色代码
    COLOR_CODES = {
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "reset": "\033[0m",
    } #字符串颜色代码

    LOG_STYLE_ENUM = {
        
        "none": "%(message)s",
        "simple": "[%(asctime)s %(pathname)s:%(lineno)d] %(message)s",
        "standard": "[%(message_log_color)s%(asctime)s %(pathname)s:%(lineno)d%(reset)s] %(log_color)s%(message)s",
        "simple_color": "%(log_color)s%(asctime)s %(message)s",
        "verbose": "%(log_color)s[%(asctime)s%(pathname)s:%(lineno)d] %(message)s",
        "debug": "%(log_color)s[%(asctime)s%(pathname)s:%(lineno)d] %(levelname)-8s %(message)s",
    }

    def __init__(self, logger_name='my_logger', log_file='output.log'):
        self.logger_name = logger_name
        self.log_file = log_file
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.NOTSET)

        # 创建一个日志处理器，将日志输出到控制台
        self.console_handler = logging.StreamHandler()
        self.console_handler.setLevel(logging.DEBUG)

        # 设置日志文件处理器
        self.file_handler = logging.FileHandler(log_file, mode='a', encoding='utf-8')
        self.file_handler.setLevel(logging.DEBUG)
        logging.basicConfig(
            filename='output.log', 
            level=logging.DEBUG, 
            encoding='utf-8',
            format='[%(asctime)s %(pathname)s:%(lineno)d] %(message)s'
            )
        # 初始化日志格式
        self.set_log_style("standard")

        # 保存原始的 print 函数
        self.original_print = builtins.print

        # 添加日志处理器
        # self.logger.addHandler(self.console_handler)
        # self.logger.addHandler(self.file_handler)
        self.set_log_enable(True)


    def set_log_level(self, level):
        """设置日志级别
        level: logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL, logging.NOTSET"""
        self.logger.setLevel(level)

    def get_log_style(self):
        return self.LOG_STYLE_ENUM[self.log_style]

    def set_log_style(self, style):
        """设置日志输出格式, style: simple, standard, simple_color, verbose, debug"""
        self.log_style = style
        self.set_log_format(self.get_log_format())

    def get_log_format(self):
        """获取日志格式"""
        log_format = colorlog.ColoredFormatter(
            self.get_log_style(),
            log_colors={
                "DEBUG": "cyan",
                "INFO": "green",
                "WARNING": "yellow",
                "ERROR": "red",
                "CRITICAL": "white,bg_red",
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
        # self.file_handler.setFormatter(logging.Formatter(self.get_log_style()))

    def get_color_text(self, text, color_code):
        ''' 获取带颜色的文本 '''
        ansi_escape = f"\033[{color_code}m"
        reset_escape = self.COLOR_CODES["reset"]
        return f"{ansi_escape}{text}{reset_escape}"

    def my_print(self, *args, sep=' ', end='\n', file=sys.stdout, flush=False):
        # 获取调用者的栈帧信息
        stack = inspect.stack()
        # 调用者信息在栈中的位置通常是第二个元素（索引为1）
        if len(stack) > 1:
            # 获取调用者的文件名和行号
            caller_frame = stack[1]
            filename = caller_frame.filename
            lineno = caller_frame.lineno
            # 为了简洁，我们只显示文件名和行号的一部分
            filename = filename.split('/')[-1]  # 假设路径是以'/'分隔的
            # 获取当前时间
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # 将文件路径和行号添加到输出中
            head = (f"[{current_time} {filename}:{lineno}] ",)
            color_head = (f"{self.COLOR_CODES['blue']}[{current_time} {filename}:{lineno}] {self.COLOR_CODES['green']}",)
            color_args = color_head + args
            args = head + args
    
        # 将输出内容转换为字符串
        output = sep.join(map(str, args)) + end
        color_output = sep.join(map(str, color_args)) + end + self.COLOR_CODES["reset"]
    
        # 写入到标准输出
        file.write(color_output)
        if flush:
            file.flush()
        # 同时将内容写入到日志文件
        with open(self.log_file, 'a', encoding='utf-8') as logfile:
            logfile.write(output)

    def set_log_enable(self, logEnable: bool, printEnable=True):
        """是否可以打印到控制台"""
        print(f"logEnable: {logEnable}\nprintEnable: {printEnable}")
        if logEnable:
            self.logger.addHandler(self.console_handler)
        else:
            self.logger.removeHandler(self.console_handler)
        if printEnable:
            builtins.print = self.my_print
        else:
            builtins.print = self.original_print

    def __enter__(self):
        # 替换原生的 print 函数
        builtins.print = self.my_print
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # 恢复原始的 print 函数
        builtins.print = self.original_print
        # 清理资源
        self.logger.removeHandler(self.console_handler)
        self.logger.removeHandler(self.file_handler)
        return False  # 不处理异常

# # 使用示例
# if __name__ == "__main__":
#     with LogHelper() as logger:  # with时候会自动调用__enter__，下面代码执行完成调用__exit__方法
#         logger.my_print("Hello, World!")
#         logger.my_print("This is a test.", "Another line.")
#         logger.set_log_style("simple_color")
#         logger.my_print("Testing simple_color style.")

logger = LogHelper()
log = logger.logger