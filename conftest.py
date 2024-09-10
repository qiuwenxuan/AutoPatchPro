from config.constants import LOG_PATH
from utils.logger import setup_logger


def pytest_configure():
    """
    pytest配置钩子，在测试执行前自动调用日志初始化。
    """
    # 读取日志配置文件,初始化自定义日志对象logger
    setup_logger(default_path=LOG_PATH)
