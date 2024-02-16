"""
Extract module 
"""

import requests
from bs4 import BeautifulSoup

from ghisa.logger import logger

from .urls import make_git_repo_url, make_profile_url, make_repo_list_url

# def get_is_forked(profile, repo_name):

#     api_repo_url = "https://api.github.com/" + profile + "/" + repo_name
#     response = requests.get(api_repo_url)
#     # Convert the response to JSON
#     data = response.json()

#     # Check if the repository is forked
#     forked = data.get("fork", False)

#     return forked


def make_soup(repo_list_url):
    """Method to get the repository"""

    response = requests.get(repo_list_url)
    # response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    return soup


def extract_repositories(soup, profile_url):
    """ """

    repos = soup.find_all("a", {"itemprop": "name codeRepository"})
    repos = [repo.text for repo in repos]

    repos = [repo for repo in repos if repo]
    repos = [repo.strip() for repo in repos if repo]
    repo_url_list = [make_git_repo_url(profile_url, repo) for repo in repos if repo]

    return repo_url_list
