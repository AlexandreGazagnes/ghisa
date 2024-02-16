"""
Fixtures for the tests
"""

import os
import shutil

import pytest

from ghisa.core.ghisa import Ghisa
from ghisa.logger import logger

# @pytest.fixture
# def list_queries() -> list:
#     """List of video queries"""

#     return []


def pytest_sessionstart(session):
    """
    Called after the Session object has been created and
    before performing collection and entering the run test loop.
    """

    if os.path.exists(Ghisa.DEFAULT_TMP):
        # os.rmdir(Ghisa.DEFAULT_TMP)
        shutil.rmtree(Ghisa.DEFAULT_TMP)

    if not os.path.exists(Ghisa.DEFAULT_TMP):
        os.makedirs(Ghisa.DEFAULT_TMP)

    pass
