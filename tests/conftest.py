"""
Fixtures for the tests
"""

import os

import pytest


import shutil

from ghisa.logger import logger
from ghisa.core.ghisa import Ghisa


# VIDEO_URL = "https://www.youtube.com/watch?v=9diaThxYnKA"
# VIDEO_ID = "V62oKsHdsLU"
# VIDEO_QUERY = "jo l'rigolo"


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
