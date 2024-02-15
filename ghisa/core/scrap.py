import requests
from bs4 import BeautifulSoup


def make_soup(self, url):
    """Method to get the repository"""

    url = +"?tab=repositories"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    return soup


def extract_repositories(soup):
    """ """

    repos = soup.find_all("a", {"itemprop": "name codeRepository"})

    return repos

    # <a href="/AlexandreGazagnes/ghisa" itemprop="name codeRepository">
    #     ghisa</a>
