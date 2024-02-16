"""
Test the Repo class.
"""

import pytest


from ghisa.core import Repo


class TestRepoIntegration:
    """Test for the Repo class."""

    def test_repo(self):
        """Test the Repo class."""

        repo = Repo()
