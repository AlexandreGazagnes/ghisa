"""
Ghisa is a library to crawl and analyze the data from github.
"""

import glob
import os
import shutil

import pandas as pd
import requests
from bs4 import BeautifulSoup

from ghisa.logger import logger

from .defaults import (
    DEFAULT_ASYNCHRONOUS,
    DEFAULT_CONFIG,
    DEFAULT_DEST,
    DEFAULT_FILE,
    DEFAULT_PROFILE_NAME,
    DEFAULT_REPO_PAGES_LIMIT,
    DEFAULT_REPO_URL,
    DEFAULT_SORT,
    DEFAULT_TEST_MODE,
    DEFAULT_TMP,
    DEFAULT_TOP_LIBRAIRIES,
)


class Ghisa:
    """Ghisa is the main class of the library. It is used to create a new"""

    DEFAULT_ASYNCHRONOUS = DEFAULT_ASYNCHRONOUS
    DEFAULT_DEST = DEFAULT_DEST
    DEFAULT_TMP = DEFAULT_TMP
    DEFAULT_FILE = DEFAULT_FILE
    DEFAULT_PROFILE_NAME = DEFAULT_PROFILE_NAME
    DEFAULT_REPO_URL = DEFAULT_REPO_URL
    DEFAULT_TEST_MODE = DEFAULT_TEST_MODE
    DEFAULT_CONFIG = DEFAULT_CONFIG
    DEFAULT_REPO_PAGES_LIMIT = DEFAULT_REPO_PAGES_LIMIT
    DEFAULT_TOP_LIBRAIRIES = DEFAULT_TOP_LIBRAIRIES
    DEFAULT_SORT = DEFAULT_SORT

    def __init__(
        self,
        dest=None,
        file=None,
        repo_limit=20,
        top_librairies=20,
        sort=None,
        test_mode=True,
        config=None,
        tmp=None,
    ):
        """Constructor of the class. It takes the url of the website to be"""

        # self.url = url
        self.config = config if config else self.DEFAULT_CONFIG
        self.dest = dest if dest else self.DEFAULT_DEST
        self.file = file if file else self.DEFAULT_FILE
        self.repo_limit = repo_limit if repo_limit else self.DEFAULT_REPO_PAGES_LIMIT
        self.top_librairies = (
            top_librairies if top_librairies else self.DEFAULT_TOP_LIBRAIRIES
        )
        self.sort = sort if sort else self.DEFAULT_SORT
        self.test_mode = test_mode if test_mode else self.DEFAULT_TEST_MODE
        self.tmp = tmp if tmp else self.DEFAULT_TMP
        self.url = ""
        self.repo_url = ""
        self.repo_name = ""

        self.file_list = []

        # self.pattern = "**/*.py"

        # self.tmp: str = self.DEFAULT_TMP if not tmp else tmp


#     def crawl_repo(self, name_or_url):
#         """Method to crawl the repository"""

#         repo_url = manage_name_or_url(name_or_url)

#         # self.repo_url = url

#         # self._clone_repo(url)

#         # self._make_file_list()

#         # imports = self._count_imports()

#         # return imports

#     def _count_imports(self):
#         """Count the imports"""

#         import_list = []
#         for fn in self.file_list:

#             lines = get_import(fn)
#             modules = [extract_from_import_line(i) for i in lines]

#             import_list.extend(modules)

#         return counter(import_list)

#     def craw_profile(self, profile):
#         """Method to crawl the profile"""

#         df = []

#         self.profile = profile

#         self.repos = get_repositories(profile)

#         logger.info(self.repos)

#         self.repo_list = []

#         for repo in repos[: self.limit]:

#             if not os.path.exists(self.tmp):
#                 os.makedirs(self.tmp)

#             logger.info(repo)

#             dict_ = self.crawl_repo(repo)

#             logger.info(f"dict_ = {dict_}")

#             df.append(dict_)

#             shutil.rmtree(self.tmp)

#             self.repo_list.append(repo)

#         ans = make_final_data(df)

#         logger.info(f"ans = {ans}")

#         save(ans, self.dest)

#         # ans = df.sum(axis=1).sort_values(ascending=False)

#         # logger.info(ans)


# # https://docs.python.org/3/py-modindex.html
