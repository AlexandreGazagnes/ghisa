import requests
from bs4 import BeautifulSoup

from ghisa.logger import logger


def make_soup(profile_url):
    """Method to get the repository"""

    profile_url = profile_url + "?tab=repositories"

    response = requests.get(profile_url)
    soup = BeautifulSoup(response.text, "html.parser")

    return soup


def extract_repositories(soup, profile_url):
    """ """

    repos = soup.find_all("a", {"itemprop": "name codeRepository"})

    repos = [repo.text for repo in repos]

    # repos = [repo.href for repo in repos]

    logger.warning(repos)

    repos = [repo for repo in repos if repo != ""]
    repos = [repo.strip() for repo in repos]
    repos = [build_repo_url(profile_url, repo) for repo in repos]

    return repos

    # <a href="/AlexandreGazagnes/ghisa" itemprop="name codeRepository">
    #     ghisa</a>


def build_repo_url(profile_url, repo):
    """ """

    if not profile_url.endswith("/"):

        profile_url = profile_url + "/"

    return profile_url + repo
