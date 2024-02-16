import pytest

from ghisa.core.github.extract import extract_repositories, make_soup
from ghisa.logger import logger


class TestGhitHubExtract:
    """Test the extract module"""

    def test_make_soup(self):
        """Test the make_soup method"""

        repo_list_url = "https://github.com/AlexandreGazagnes?tab=repositories"
        soup = make_soup(repo_list_url)

    def test_extract_repositories(self):
        """Test the extract_repositories method"""

        repo_list_url = "https://github.com/AlexandreGazagnes?tab=repositories"
        soup = make_soup(repo_list_url)

        profile_url = "https://github.com/AlexandreGazagnes"

        repos = extract_repositories(soup, profile_url)
        assert repos
