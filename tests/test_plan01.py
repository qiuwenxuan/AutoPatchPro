import logging

import pytest





def test_01_check_autopatch_devices_monitor_view(logger):
    logger.info("hello world")
    pass


if __name__ == '__main__':
    logger = logging.getLogger("logger")
    pytest.main([r'.\AutopatchDevice\testcase\test_01_Check_autopatch_devices_monitor_view.py ', '-vs'])
