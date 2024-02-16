"""
Test the Repo class.
"""

import pytest

from ghisa.core import Profile
from ghisa.logger import logger


class TestProfileIntegration:
    """Test for the Profile class."""

    def test_repo(self):
        """Test the Profile class."""

        profile = Profile(
            repo_pages_limit=1,
            repo_number_limit=100,
            profile_name="AlexandreGazagnes",
        )
