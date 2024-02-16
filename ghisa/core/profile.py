"""
"""

from ghisa.logger import logger

from .repo import Repo

from .local.transform import make_final_df
from .local.load import save
import pandas as pd


# from .github.load import clone_repo
# from .local.extract import make_python_file_list
# from .local.local import make_modules_list_from_file
# from .local.helpers import counter

from .github.github import get_repositories_from_profile, get_repositories_from_a_page
from .defaults import (
    DEFAULT_ASYNCHRONOUS,
    DEFAULT_DEST,
    DEFAULT_FILE,
    DEFAULT_PROFILE_NAME,
    DEFAULT_REPO_URL,
    DEFAULT_TEST_MODE,
    DEFAULT_CONFIG,
    DEFAULT_REPO_PAGES_LIMIT,
    DEFAULT_TOP_LIBRAIRIES,
    DEFAULT_SORT,
    DEFAULT_TMP,
    BASE_URL,
    DEFAULT_TEST_MODE,
    FORCE_UNIQUE,
    DEFAULT_REPO_PAGES_LIMIT,
    DEFAULT_REPO_NUMBER_LIMIT,
)


class Profile:
    """Profile class"""

    DEFAULT_DEST = DEFAULT_DEST
    DEFAULT_FILE = DEFAULT_FILE
    # DEFAULT_REPO_URL = DEFAULT_REPO_URL
    DEFAULT_TOP_LIBRAIRIES = DEFAULT_TOP_LIBRAIRIES
    DEFAULT_CONFIG = DEFAULT_CONFIG
    DEFAULT_TMP = DEFAULT_TMP
    DEFAULT_TEST_MODE = DEFAULT_TEST_MODE
    DEFAULT_PROFILE_NAME = DEFAULT_PROFILE_NAME
    FORCE_UNIQUE = FORCE_UNIQUE

    DEFAULT_SORT = DEFAULT_SORT
    DEFAULT_REPO_PAGES_LIMIT = DEFAULT_REPO_PAGES_LIMIT
    DEFAULT_REPO_NUMBER_LIMIT = DEFAULT_REPO_NUMBER_LIMIT
    DEFAULT_PROFILE_NAME = DEFAULT_PROFILE_NAME
    DEFAULT_ASYNCHRONOUS = DEFAULT_ASYNCHRONOUS

    BASE_URL = BASE_URL

    def __init__(
        self,
        profile_name=None,
        dest=None,
        file=None,
        top_librairies=None,
        config=None,
        tmp=None,
        force_unique=False,
        test_mode=None,
        sort=None,
        repo_pages_limit=None,
        repo_number_limit=None,
        asynchronous=None,
    ) -> None:
        """Constructor of the class"""

        self.profile_name = profile_name if profile_name else self.DEFAULT_PROFILE_NAME
        self.dest = dest if dest else self.DEFAULT_DEST
        self.file = file if file else self.DEFAULT_FILE
        self.top_librairies = (
            top_librairies if top_librairies else self.DEFAULT_TOP_LIBRAIRIES
        )
        self.config = config if config else self.DEFAULT_CONFIG
        self.tmp = tmp if tmp else self.DEFAULT_TMP
        self.force_unique = force_unique if force_unique else self.FORCE_UNIQUE
        self.test_mode = test_mode if test_mode else self.DEFAULT_TEST_MODE
        self.sort = sort if sort else self.DEFAULT_SORT
        self.repo_pages_limit = (
            repo_pages_limit if repo_pages_limit else self.DEFAULT_REPO_PAGES_LIMIT
        )
        self.repo_number_limit = (
            repo_number_limit if repo_number_limit else self.DEFAULT_REPO_NUMBER_LIMIT
        )

        self.asynchronous = asynchronous if asynchronous else self.DEFAULT_ASYNCHRONOUS

        self.repo_list_url = []
        self.repo_list_object = []

        self.module_unique_list = []
        self.module_dict = []

        self._get_repo_list()
        self._make_repo_objects()
        self._count_imports()

    def _get_repo_list(self):
        """ """

        self.repo_list_url = get_repositories_from_profile(
            self.profile_name,
            pages=self.repo_pages_limit,
            sort=self.sort,
        )

        if self.repo_number_limit:
            self.repo_list_url = self.repo_list_url[: self.repo_number_limit]

    def _make_repo_objects(self):
        """ """

        for repo_url in self.repo_list_url:

            try:
                repo = Repo(repo_url)
                self.repo_list_object.append(repo)
            except Exception as e:
                logger.error(e)
                continue

    def _count_imports(self):
        """"""

        li = []
        for repo in self.repo_list_object:
            logger.warning(f"repo.module_dict is :{repo.module_dict}")
            li.append(repo.module_dict)

        ans = make_final_df(li, top_librairies=self.top_librairies)

        logger.warning(f"ans is :{ans}")

        save(ans, "test.json")
        # df.to_csv("test.csv", index=False)

        # ans = df.sum
