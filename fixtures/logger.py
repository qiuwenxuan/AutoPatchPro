import logging
import logging.config
import os

import yaml

from config.config import LOG_PATH


def setup_logging(default_path=LOG_PATH, default_level=logging.INFO):
    """
    初始化日志配置。

    :param default_path: 默认的日志配置文件路径。
    :param default_level: 如果没有提供配置文件，使用的默认日志级别。
    """
    # 尝试从配置文件中加载日志配置
    if os.path.exists(default_path):
        with open(default_path, 'rt', encoding='utf-8') as file:
            config = yaml.safe_load(file.read())
            logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)
        logging.info(f"警告: 找不到日志配置文件 {default_path}。使用默认基础配置。")


# 示例用法
if __name__ == '__main__':
    print(os.getcwd())
    setup_logging()
    logger = logging.getLogger('logger')  # 获取配置中的自定义 logger
    logger.info('这是一个信息日志')
    logger.error('这是一个错误日志')
