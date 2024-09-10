import logging

import pytest


@pytest.fixture(scope="module")
def logger():
    logger = logging.getLogger("logger")
    return logger
