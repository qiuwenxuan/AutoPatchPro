import logging

from config.constants import LOG_PATH
from utils.logger import setup_logger


def pytest_configure():
    """
    pytest配置钩子，在测试执行前自动调用日志初始化。
    """
    setup_logger(default_path=LOG_PATH)
    logger = logging.getLogger("logger")
    logger.info("日志已初始化")
