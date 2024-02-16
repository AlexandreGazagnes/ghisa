"""
Test the Repo class.
"""

import pytest

from ghisa.core import Repo


class TestRepoIntegration:
    """Test for the Repo class."""

    def test_repo(self):
        """Test the Repo class."""

        url = "https://github.com/AlexandreGazagnes/awdible"
        repo = Repo(repo_url=url, test_mode=True)
        repo.module_dict

        with open("repo.txt", "w") as f:
            f.write(str(repo.module_dict))
