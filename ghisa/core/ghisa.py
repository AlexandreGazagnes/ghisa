"""
Ghisa is a library to crawl and analyze the data from github.
"""

import os
import glob

import shutil

import pandas as pd

import requests
import logging
from bs4 import BeautifulSoup

from .helpers import get_import, extract_from_import_line, counter
from ghisa.core.scrap import make_soup, extract_repositories


class Ghisa:
    """Ghisa is the main class of the library. It is used to create a new"""

    DEFAULT_REPO = repo_url = "https://github.com/MentalDeFer972/project2py-ocr"
    DEFAULT_TMP = "tmp"

    DEFAULT_DEST = "./result.txt"

    def __init__(self, config={}, tmp=None, test_mode=False, limit=20, dest=None):
        """Constructor of the class. It takes the url of the website to be"""

        # self.url = url
        self.config = config
        self.dest = dest if dest else self.DEFAULT_DEST

        self.limit = limit
        self.test_mode = test_mode
        self.url = ""
        self.repo_url = ""
        self.repo_name = ""

        self.file_list = []

        self.pattern = "**/*.py"

        self.tmp: str = self.DEFAULT_TMP if not tmp else tmp

    def crawl_repo(self, url: None):
        """Method to crawl the repository"""

        self.repo_url = url

        self._clone_repo(url)

        self._make_file_list()

        imports = self._count_imports()

        return imports

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

    def craw_profile(self, url):
        """Method to crawl the profile"""

        df = []

        self.profile_url = url

        soup = make_soup(url)
        repos = extract_repositories(soup, url)

        logging.info(repos)

        self.repo_list = []

        for repo in repos[: self.limit]:

            if not os.path.exists(self.tmp):
                os.makedirs(self.tmp)

            logging.info(repo)

            try:
                dict_ = self.crawl_repo(repo)

                logging.info(dict_)

                df.append(dict_)

                shutil.rmtree(self.tmp)

                self.repo_list.append(repo)

            except Exception as e:
                logging.error(e)

        df = pd.DataFrame(df)

        logging.info(df)

        ans = df.sum(axis=0).sort_values(ascending=False)

        logging.info(ans)

        with open(self.dest, "w") as f:
            f.write(str(ans))

        # ans = df.sum(axis=1).sort_values(ascending=False)

        # logging.info(ans)
