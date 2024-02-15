"""
Ghisa is a library to crawl and analyze the data from github.
"""

import os
import glob

import requests
from bs4 import BeautifulSoup

from .helpers import get_import, extract_from_import_line, counter
from ghisa.core.scrap import make_soup, extract_repositories


class Ghisa:
    """Ghisa is the main class of the library. It is used to create a new"""

    DEFAULT_REPO = repo_url = "https://github.com/MentalDeFer972/project2py-ocr"
    DEFAULT_TMP = "tmp"

    def __init__(self, config={}, tmp=None, test_mode=False):
        """Constructor of the class. It takes the url of the website to be"""

        # self.url = url
        self.config = config

        self.test_mode = test_mode
        self.url = ""
        self.repo_url = ""
        self.repo_name = ""

        self.file_list = []

        self.pattern = "**/*.py"

        self.tmp: str = self.DEFAULT_TMP if not tmp else tmp

    def crawl_repo(self, repo_url: None):
        """Method to crawl the repository"""

        self._clone_repo(repo_url)

        self._make_file_list()

        imports = self._count_imports()

        return imports

    # def craw_profile(self, url):
    #     """Method to crawl the profile"""
    #     pass

    # def get_repo(self, url):
    #     """Method to get the repository"""
    #     pass

    # def get_profile(self, url):
    #     """Method to get the profile"""
    #     pass

    def _clone_repo(self, repo_url):
        """Clone the repository"""

        if not repo_url:
            repo_url = self.DEFAULT_REPO

        if not os.path.exists(self.tmp):
            os.makedirs(self.tmp)

        if not repo_url.startswith("https://github.com"):
            raise ValueError(f"Expected {repo_url} to be a github url")

        if not repo_url.endswith(".git"):
            repo_url = repo_url + ".git"

        os.system(f"git clone {repo_url} {self.tmp}")
        os.system(f"rm -rf {self.tmp}/.git")

        self.repo_name = f"./{self.tmp}/"

    def _make_file_list(self):
        """Make the file list"""

        query2 = self.repo_name + self.pattern
        self.file_list = glob.glob(query2, recursive=True)

    def _count_imports(self):
        """Count the imports"""

        import_list = []
        for fn in self.file_list:

            lines = get_import(fn)
            modules = [extract_from_import_line(i) for i in lines]

            import_list.extend(modules)

        return counter(import_list)

    def craw_profile(self, profile_url):
        """Method to crawl the profile"""

        dict_ = {}

        self.profile_url = profile_url

        soup = make_soup()
        repos = extract_repositories(soup)

        repos = self.get_repos(profile_url)

        for repo in repos:
            dict_[repo] = self.crawl_repo(repo)

        return dict_
