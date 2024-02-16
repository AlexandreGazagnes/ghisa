"""
RepoCommand
"""

from cleo.commands.command import Command
from cleo.helpers import argument, option

from ghisa.core.defaults import (
    DEFAULT_ASYNCHRONOUS,
    DEFAULT_CONFIG,
    DEFAULT_DEST,
    DEFAULT_EXCLUDE_FORKS,
    DEFAULT_FILE,
    DEFAULT_FORCE_UNIQUE,
    DEFAULT_OUTPUT,
    DEFAULT_PROFILE_NAME,
    DEFAULT_REPO_NUMBER_LIMIT,
    DEFAULT_REPO_PAGES_LIMIT,
    DEFAULT_SORT,
    DEFAULT_TEST_MODE,
    DEFAULT_TMP,
    DEFAULT_TOP_LIBRAIRIES,
)
from ghisa.core.repo import Repo
from ghisa.logger import logger

# from ghisa.core.ghisa import Ghisa


class RepoCommand(Command):
    name = "run repo"

    description = "Run github repo session"

    arguments = [
        argument(
            "repo_url",
            description="The repo_url to analyze.",
            optional=True,
            # default=Ghisa.DEFAULT_VIDEO_URL,
        )
    ]
    options = [
        option(
            "dest",
            "d",
            description="The destination directory of the file",
            flag=False,
            default=DEFAULT_DEST,
        ),
        option(
            "file",
            "f",
            description="The input file with list of [...]",
            flag=False,
            default=DEFAULT_FILE,
        ),
        option(
            "output",
            "o",
            description="The output file name",
            flag=False,
            default=DEFAULT_OUTPUT,
        ),
        option(
            "asynchronous",
            "a",
            description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla nec odio nec urna tincidunt tincidunt",
            flag=True,
        ),
    ]

    def handle(self):
        """handle the command"""

        # arguments
        url = self.argument("url")

        # no flags options
        dest = self.option("dest")
        file = self.option("file")
        output = self.option("output")

        # flags options
        # search = self.option("search")
        asynchronous = self.option("asynchronous")

        # # useless logging
        # logger.debug(f"url: {url}")

        # logger.debug(f"dest: {dest}")
        # logger.debug(f"file: {file}")
        # logger.debug(f"output: {output}")

        # logger.debug(f"search: {search}")
        # logger.debug(f"asynchronous: {asynchronous}")

        self.line("Eh! I'm running the command")
        Repo(
            repo_url=url,
            dest=dest,
            file=file,
            output=output,
            asynchronous=asynchronous,
        )
