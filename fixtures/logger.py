import logging

import pytest


@pytest.fixture(scope="module")
def logger():
    logger = logging.getLogger('logger')
    logger.info("日志已初始化")
    return logger
