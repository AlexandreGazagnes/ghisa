"""
Fixtures for the tests
"""

import os
import shutil

import pytest

from ghisa.core.ghisa import Ghisa

# @pytest.fixture
# def my_fixture() -> None:


#     return None


def pytest_sessionstart(session):
    """session start"""

    if os.path.exists(Ghisa.DEFAULT_TMP):
        shutil.rmtree(Ghisa.DEFAULT_TMP)

    if not os.path.exists(Ghisa.DEFAULT_TMP):
        os.makedirs(Ghisa.DEFAULT_TMP)
