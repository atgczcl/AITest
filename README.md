# LLoghelper

#### 1.使用：

> pip install LLoghelper

#### 2.导入：

> ```python
> from LLoghelper.log_helper import log, logger
>
>
> ```

#### 3.控制日志log, print 是否可以打印  print=false恢复原样

```python
logger.set_log_enable(True, True)  
```

说明：

```python
 ''' 日志辅助类 
    Just: 
    pip install LLoghelper
    from LLoghelper.log_helper import log, logger
    支持log.info, print 等方法提供日志输出、格式设置、颜色设置等功能
    调用方法：
        log.info("This is a test.")
        log.warning("This is a warning.")
        log.error("This is an error.")
        log.critical("This is a critical error.")
        log.debug("This is a debug message.")
    替换原生的 print 函数, 并支持颜色输出：
        print("This is a test.")
        print("This is a critical test.", log_level=logger.CRITICAL)
        print("This is a warning test.", log_level=logger.WARNING)
        print("This is an error test.", log_level=logger.ERROR)
        print("This is a debug test.", log_level=logger.DEBUG)
        print("This is a info test.", log_level=logger.INFO)
    主要功能：
    1. 日志输出到控制台和文件
    2. 日志格式设置：simple, standard, simple_color, verbose, debug
    3. 日志颜色设置：red, green, yellow, blue, magenta, cyan, reset
    4. 日志级别设置：DEBUG, INFO, WARNING, ERROR, CRITICAL, NOTSET
    5. 日志打印控制：可以控制日志是否可以打印到控制台和文件

    '''
```

![image](./docs/screenshot.png)
