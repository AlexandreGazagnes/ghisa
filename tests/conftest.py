"""
Fixtures for the tests
"""

import os

import pytest

from ghisa.logger import logger
from ghisa.core.ghisa import ghisa


VIDEO_URL = "https://www.youtube.com/watch?v=9diaThxYnKA"
VIDEO_ID = "V62oKsHdsLU"
VIDEO_QUERY = "jo l'rigolo"


@pytest.fixture
def list_queries() -> list:
    """List of video queries"""

    return []


def pytest_sessionstart(session):
    """
    Called after the Session object has been created and
    before performing collection and entering the run test loop.
    """

    if os.path.exists(ghisa.DEFAULT_TMP):
        for file in os.listdir(ghisa.DEFAULT_TMP):
            os.remove(ghisa.DEFAULT_TMP + file)
        os.rmdir(ghisa.DEFAULT_TMP)

    if not os.path.exists(ghisa.DEFAULT_TMP):
        os.makedirs(ghisa.DEFAULT_TMP)

    pass
