import logging
from datetime import datetime
import os
import threading
from util.read_config import ReadConfig

base_url = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.split(base_url)[0]

# 定义一个log输出的格式和log输出等级的定义等等
class Log:
    def __init__(self):
        global log_path, result_path
        result_path = os.path.join(project_dir, "result")
        # create result file if it does not exist
        if not os.path.exists(result_path):
            os.mkdir(result_path)
        log_path = os.path.join(result_path, str(datetime.now().strftime("%Y%m%d%H%M%S")))
        if not os.path.exists(log_path):
            os.mkdir(log_path)
        # 创建一个logger对象赋值给logger，getLogger可以有一个参数name，可选参数，意思是将要返回的日志器的名称标识，
        # 若不提供参数则默认返回root；使用同一name多次调用方法，则指向同一logger对象
        self.logger = logging.getLogger()
        # 为logger对象添加日志级别为INFO，除此之外一搬还可设置为：warning，error，debug，critical，exception
        self.logger.setLevel(logging.INFO)
        # 创建处理器对象
        handler = logging.FileHandler(os.path.join(log_path, "output.log"))
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s >> %(message)s')
        # 为处理器添加设置格式器对象，添加过滤器对象的方法为：handler.setFilter(filter)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def get_logger(self):
        return self.logger


class MyLog:
    """
    将上面的记录log的方法放到一个线程内，让它单独启用一个线程，是为了更好的写log
    """
    log = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_log():
        if MyLog.log is None:
            MyLog.mutex.acquire()
            MyLog.log = Log()
            MyLog.mutex.release()
        return MyLog.log



