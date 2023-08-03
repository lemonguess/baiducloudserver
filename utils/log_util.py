import os
import sys
import datetime
import logging
from concurrent_log_handler import ConcurrentRotatingFileHandler
import colorlog

LOGGING_CONF = {
    'formatters': {
        # 'color': "%(log_color)s[%(asctime)s][%(pathname)s:%(lineno)d][%(threadName)s:%(process)d][characterName][%(levelname)s]- %(message)s",
        # 'color': "%(log_color)s[%(asctime)s][%(filename)s:%(lineno)d][%(threadName)s:%(process)d][%(funcName)s][characterName][%(levelname)s]- %(message)s",
        'color': "%(log_color)s[%(asctime)s][%(filename)s:%(lineno)d][%(funcName)s][characterName][%(levelname)s]- %(message)s",
        'simple': "[%(asctime)s][%(pathname)s:%(lineno)d][%(threadName)s:%(process)d][characterName][%(levelname)s]- %(message)s"
    },
    'handlers': {
        'log': {
            # 'log_path': sys.path[1],
            'level': "DEBUG",
            'console': True,
            'file': True,
            'maxBytes': 100 * 1024 * 1024,
            'formatter': 'color'
        },
        'test': {
            # 'log_path': sys.path[1],
            'level': "DEBUG",
            'console': True,
            'file': False,
            'maxBytes': 300 * 1024 * 1024,
            'formatter': 'color'
        },
    },
    'log_colors_config': {
        'DEBUG': 'green',
        # 'DEBUG': 'white',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'bold_red'
    }
}

class Logger:
    def __init__(self, LOGGING=None):
        if LOGGING is None:
            self.LOGGING = LOGGING_CONF
        else:
            self.LOGGING = LOGGING

    def _init(self):
        # 创建日志器,并设置级别
        self.level = self.LOGGING['handlers'][self.name].get("level", "DEBUG")
        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(self.level)
        # 定义处理器。控制台和文本输出两种方式
        # 定义输出格式,把格式传给处理器
        self.formatter = self._init_format()
        # 控制台打印（默认为True）：
        if self.LOGGING['handlers'][self.name].get("console", True):
            # 定义处理器。控制台和文本输出两种方式 ———— 控制台相关设置
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.formatter)
            if type(console_handler) not in [type(h) for h in self.logger.handlers]:
                self.logger.addHandler(console_handler)
        # 日志文件打印（默认为True）：
        if self.LOGGING['handlers'][self.name].get("file", True):
            # 定义处理器。控制台和文本输出两种方式 ———— 文件相关设置
            self.set_file_handler()
        return self.logger

    def get_base_dir(self):
        # 按照正常的情况下, sys,path的最前面就是项目的根目录,
        # 但是保险起见我们还是写了循环获取的代码
        # 这里只循环到倒数第三个的原因是有的时候我们会在sys.path中进行插入当前路径的操作,
        # 容易插入的层级超过了项目根目录, 但是如果是用insert在最前面, 那就无能为力了
        # 注意一下这个问题就好
        # if len(sys.path) >= 6:
        #     sys_path_list = sys.path[:6]
        # else:
        #     sys_path_list = sys.path[:-2]
        sys_path_list = sys.path
        pwd = os.getcwd()
        path = pwd
        for sys_path in sys_path_list:
            if sys_path in pwd and len(sys_path) < len(path):
                path = sys_path
        return path

    def set_file_handler(self):
        maxBytes = self.LOGGING['handlers'][self.name].get("maxBytes", 1024 * 1024 * 200)
        log_dir = "logs"  # 日志存放文件夹名称
        log_path = self.LOGGING['handlers'][self.name].get("log_path", self.get_base_dir()) + os.sep + log_dir
        if not os.path.isdir(log_path):
            os.makedirs(log_path)
        # 获取当前日期并转换为字符串格式
        current_date = datetime.datetime.now().strftime('%Y-%m-%d')
        for leval in ["ERROR", "INFO", "DEBUG"]:
            handler_f = ConcurrentRotatingFileHandler(
                filename=log_path + os.sep + ('all-%s.log' % current_date if leval == "DEBUG" else (
                            leval.lower() + '-%s.log' % current_date)),
                mode='a', encoding='utf-8', maxBytes=maxBytes,
                backupCount=5)
            handler_f.setLevel(leval)
            handler_f.setFormatter(self.formatter)
            baseFilenames = []
            for h in self.logger.handlers:
                try:
                    baseFilenames.append(h.baseFilename)
                except:
                    pass
            if handler_f.baseFilename not in baseFilenames:
                self.logger.addHandler(handler_f)

    def _init_format(self):
        """
        定义格式处理器
        :return:
        """
        formatters_name = self.LOGGING['handlers'][self.name]['formatter']
        format_str = self.LOGGING['formatters'][formatters_name]
        format_str = format_str.replace("[characterName]", "[%s]" % self.characterName if self.characterName else "")
        if 'log_color' in format_str:
            log_colors_config = self.LOGGING['log_colors_config']
            formatter = colorlog.ColoredFormatter(fmt=format_str, log_colors=log_colors_config)
        else:
            formatter = logging.Formatter(fmt=format_str)
        return formatter

    def get_logger(self, handler='log', character=""):
        try:
            handler_conf_info = self.LOGGING['handlers'][handler]
            if not handler_conf_info:
                raise NameError("LOGGING配置错误:当前无适配handler[%s]" % handler)
        except Exception as e:
            raise NameError("LOGGING配置错误:\n %s" % e)
        # 日志器名称
        self.name = handler
        # 自定义特征名称
        self.characterName = character
        logger = self._init()
        return logger

if __name__ == '__main__':
    # logger = Logger().get_logger('log', 'mysql')

    logger = Logger().get_logger('log')
    def t2():
        logger.warning('222')
        logger.info('111')
        logger.debug('333')
        try:
            int('abc')
        except Exception as e:
            logger.exception(e)
    t2()