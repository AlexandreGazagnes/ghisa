"""
github module
"""

from ghisa.logger import logger
from .urls import make_repo_list_url, make_profile_url, make_git_repo_url
from .extract import make_soup, extract_repositories


def get_repositories_from_a_page(profile_name, page=0, sort=None):
    """Get the repositories from a page of a repository profile"""

    profile_url = make_profile_url(profile_name)
    repo_list_url = make_repo_list_url(profile_url, page=page, sort=sort)

    soup = make_soup(repo_list_url)
    repos = extract_repositories(soup, profile_url)

    if not repos:
        raise AttributeError(
            f"no repositories found on page {page}   of {profile_name} {profile_url} and {repo_list_url}: "
        )

    # logger.info(
    #     f" Repositories from page {page}  of {profile_name} {profile_url} and {repo_list_url}: {repos}"
    # )

    return repos


def get_repositories_from_profile(profile_name, pages=1, sort=None):
    """Parse various pages of a profile repository list and return the list of repositories"""

    repos = []

    for page in range(1, pages + 1):
        # if page == 0:
        #     continue
        try:
            repos += get_repositories_from_a_page(profile_name, page=page, sort=sort)
        except AttributeError as e:
            logger.error(e)
            break

    logger.info(repos)
    return repos
