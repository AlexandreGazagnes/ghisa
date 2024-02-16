"""
Ghisa is a library to crawl and analyze the data from github.
"""

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

        pass
