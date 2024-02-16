"""
Test the Repo class.
"""

import pytest

from ghisa.logger import logger
from ghisa.core import Profile


class TestProfileIntegration:
    """Test for the Profile class."""

    def test_repo(self):
        """Test the Profile class."""

        profile = Profile(
            repo_pages_limit=1,
            repo_number_limit=3,
            profile_name="AlexandreGazagnes",
        )

        assert profile.repo_list_url

        # logger.warning(profile.repo_list_url)

        # logger.warning(profile.repo_list_object)
