"""
Repo class Module
"""

from ghisa.logger import logger

from .defaults import (
    BASE_URL,
    DEFAULT_CONFIG,
    DEFAULT_DEST,
    DEFAULT_FILE,
    DEFAULT_FORCE_UNIQUE,
    DEFAULT_REPO_URL,
    DEFAULT_TEST_MODE,
    DEFAULT_TMP,
    DEFAULT_TOP_LIBRAIRIES,
)
from .gh.load import clone_repo
from .local.extract import make_python_file_list
from .local.helpers import counter
from .local.local import make_modules_list_from_file


class Repo:
    """ """

    DEFAULT_DEST = DEFAULT_DEST
    DEFAULT_FILE = DEFAULT_FILE
    DEFAULT_REPO_URL = DEFAULT_REPO_URL
    DEFAULT_TOP_LIBRAIRIES = DEFAULT_TOP_LIBRAIRIES
    DEFAULT_CONFIG = DEFAULT_CONFIG
    DEFAULT_TMP = DEFAULT_TMP
    DEFAULT_TEST_MODE = DEFAULT_TEST_MODE
    DEFAULT_FORCE_UNIQUE = DEFAULT_FORCE_UNIQUE

    BASE_URL = BASE_URL

    def __init__(
        self,
        repo_url=None,
        dest=None,
        file=None,
        top_librairies=None,
        config=None,
        test_mode=None,
        force_unique=False,
        tmp=None,
    ) -> None:
        """Constructor of the class"""

        self.repo_url = repo_url if repo_url else self.DEFAULT_REPO_URL
        self.dest = dest if dest else self.DEFAULT_DEST
        self.file = file if file else self.DEFAULT_FILE
        self.top_librairies = (
            top_librairies if top_librairies else self.DEFAULT_TOP_LIBRAIRIES
        )
        self.config = config if config else self.DEFAULT_CONFIG
        self.test_mode = test_mode if test_mode else self.DEFAULT_TEST_MODE
        self.tmp = tmp if tmp else self.DEFAULT_TMP
        self.force_unique = force_unique if force_unique else self.DEFAULT_FORCE_UNIQUE
        self.repo_git = ""
        self.repo_name = ""
        self.profile = ""
        self.branch = ""

        self._file_list = []
        self.module_unique_list = []
        self.module_dict = {}

        self._run()

    def _run(self):
        """ """

        # TODO : add github module

        # TODO : add a validator

        # TODO : add if is_forked => NO

        self._manage_repo()
        self._clone_repo()
        self._count_imports()

    def _manage_repo(self):
        """ """

        ######################################
        #   THIS CODE SHOULD MOOVE
        #######################################

        # TODO USE A VALIDATOR
        if not self.repo_url.startswith(self.BASE_URL):
            raise ValueError(f"Expected {self.repo_url} to be a github url")

        # TODO : USE A FUNCTION
        if self.repo_url.endswith(".git"):
            self.repo_url = self.repo_url.removesuffix(".git")

        # TODO : USE A FUNCTION
        if "/tree/" in self.repo_url:
            self.repo_url = self.repo_url.split("/tree/")[0]

        # TODO : USE A FUNCTION
        _repo = self.repo_url.removeprefix(self.BASE_URL)
        _repo = _repo.removesuffix("/").removeprefix("/")

        logger.info(f"Repo _repo : {_repo}")

        self.profile = _repo.split("/")[0]

        _repo_name = _repo.split("/")[1]

        self.repo_name = _repo_name.replace("/", "")

        self.repo_url = f"{self.BASE_URL}/{self.profile}/{self.repo_name}"
        self.repo_git = f"{self.repo_url}.git"

        # logger.info(f"Profile : {self.profile}")
        # logger.info(f"Repo name : {self.repo_name}")
        # logger.info(f"Repo url : {self.repo_url}")
        # logger.info(f"Repo git : {self.repo_git}")

        ######################################
        #   THIS CODE SHOULD MOOVE
        #######################################

    def _clone_repo(self):
        """ """

        clone_repo(self.repo_git, self.tmp)

    def _count_imports(self):
        """ """

        self._file_list = make_python_file_list(self.tmp)

        modules = []
        for file in self._file_list:
            modules.extend(make_modules_list_from_file(file, self.repo_name))

        # list
        self.module_unique_list = sorted(list(set(modules)))

        # dict
        if not self.force_unique:
            self.module_dict = counter(modules)
        else:
            self.module_dict = {k: 1 for k in self.module_unique_list}

        logger.warning(f"Module unique list : {self.module_unique_list}")
        logger.warning(f"Module dict : {self.module_dict}")

    @property
    def dict(self):
        return {k: v for k, v in self.__dict__.items() if not k.startswith("_")}

    @property
    def n_files(self):
        return len(self._file_list)

    @property
    def n_modules(self):
        return len(self.module_unique_list)

    @property
    def file_list(self):
        li = [i.removeprefix(self.tmp) for i in self._file_list]
        li = [i.removeprefix("/") for i in li]

        return li

    def __repr__(self):
        return f"{self.__dict__}"
