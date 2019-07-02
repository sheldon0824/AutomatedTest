import logging
import os.path
import time


class Logger(object):

    def __init__(self, logger):
        """
        指定了保存日志的路径、日志的级别、以及调用文件
        将日志存入到指定的文件中
        :param logger:
        """

        #  创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)  # 设置日志级别, 显示debug以上的信息
        # 日志级别等级为：CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET

        riqi = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
        log_path = os.path.dirname(os.getcwd()) + '/logs/'
        log_name = log_path + riqi + '.log'

        #  创建一个handler，用于写入日志文件
        fh = logging.FileHandler(log_name, encoding='GBK')
        fh.setLevel(logging.INFO)

        #  再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        #  定义handler的输出格式
        formatter =logging.Formatter("%(asctime)s - %(filename)s - [line:%(lineno)d] - %(levelname)s - %(message)s")
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        #  给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def get_log(self):
        return self.logger


