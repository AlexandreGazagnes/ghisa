"""
Test the ghisa class.
"""

import pytest

from ghisa.core.ghisa import Ghisa
from ghisa.logger import logger

from ghisa.config import config


class TestGhisa:
    """Test the ghisa class."""

    def test___init__(self):
        Ghisa(test_mode=True)
