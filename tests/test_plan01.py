import logging

import pytest

from fixtures.logger import logger


def test_01_check_autopatch_devices_monitor_view(logger):
    logger.info("hello world")
    pass


if __name__ == '__main__':
    logger = logging.getLogger("logger")
    logger.info("hello world")
    pytest.main([r'.\AutopatchDevice\testcase\test_01_Check_autopatch_devices_monitor_view.py ', '-vs'])
