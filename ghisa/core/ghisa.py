"""
Ghisa is a library to crawl and analyze the data from github.
"""

import os
import glob

import shutil

from ghisa.logger import logger
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

    def __init__(
        self,
        config={},
        tmp=None,
        test_mode=False,
        limit=20,
        dest=None,
        top=20,
        sort="stargazers",
    ):
        """Constructor of the class. It takes the url of the website to be"""

        # self.url = url
        self.config = config
        self.dest = dest if dest else self.DEFAULT_DEST

        self.top = top
        self.limit = limit
        self.test_mode = test_mode
        self.sort = sort
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

    def _count_imports(self):
        """Count the imports"""

        import_list = []
        for fn in self.file_list:

            lines = get_import(fn)
            modules = [extract_from_import_line(i) for i in lines]

            import_list.extend(modules)

        return counter(import_list)

    def craw_profile(self, profile):
        """Method to crawl the profile"""

        df = []

        self.profile = profile

        self.repos = get_repositories(profile)

        logging.info(self.repos)

        self.repo_list = []

        for repo in repos[: self.limit]:

            if not os.path.exists(self.tmp):
                os.makedirs(self.tmp)

            logging.info(repo)

            dict_ = self.crawl_repo(repo)

            logging.info(f"dict_ = {dict_}")

            df.append(dict_)

            shutil.rmtree(self.tmp)

            self.repo_list.append(repo)

        ans = make_final_data(df)

        logging.info(f"ans = {ans}")

        save(ans, self.dest)

        # ans = df.sum(axis=1).sort_values(ascending=False)

        # logging.info(ans)


# https://docs.python.org/3/py-modindex.html
