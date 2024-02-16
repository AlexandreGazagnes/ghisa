"""
Extract module 
"""

import requests

from bs4 import BeautifulSoup

from ghisa.logger import logger
from .urls import make_repo_list_url, make_profile_url, make_git_repo_url


def make_soup(repo_list_url):
    """Method to get the repository"""

    repo_list_url = repo_list_url + "?tab=repositories"

    response = requests.get(repo_list_url)

    # response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    return soup


def extract_repositories(soup, profile_url):
    """ """

    repos = soup.find_all("a", {"itemprop": "name codeRepository"})

    repos = [repo.text for repo in repos]

    # repos = [repo.href for repo in repos]

    logger.info(repos)

    repos = [repo for repo in repos if repo != ""]
    repos = [repo.strip() for repo in repos]
    repo_url_list = [make_git_repo_url(profile_url, repo) for repo in repos]

    # <a href="/AlexandreGazagnes/ghisa" itemprop="name codeRepository">
    #     ghisa</a>

    return repo_url_list
