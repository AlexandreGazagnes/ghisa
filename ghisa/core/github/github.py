"""
github module
"""

from ghisa.logger import logger
from .urls import make_repo_list_url, make_profile_url, make_git_repo_url
from .extract import make_soup, extract_repositories


def get_repositories_from_a_page(profile, page=0, sort=None):
    """Get the repositories from a page of a repository profile"""

    profile_url = make_profile_url(profile)
    repo_list_url = make_repo_list_url(profile_url, page=page, sort=sort)

    soup = make_soup(repo_list_url)
    repos = extract_repositories(soup, profile_url)

    return repos


def get_repositories_from_profile(profile, pages=0, sort=None):
    """Parse various pages of a profile repository list and return the list of repositories"""

    repos = []

    for page in range(pages):
        if page == 1:
            continue
        repos += get_repositories_from_a_page(profile, page=page, sort=sort)

    return repos
