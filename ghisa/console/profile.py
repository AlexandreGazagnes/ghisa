"""
ProfileCommand
"""

from cleo.commands.command import Command
from cleo.helpers import argument, option

from ghisa.core.defaults import (  # DEFAULT_ASYNCHRONOUS,; DEFAULT_TEST_MODE,; DEFAULT_TMP,; DEFAULT_TOP_LIBRAIRIES,; DEFAULT_CONFIG,; DEFAULT_FORCE_UNIQUE,; DEFAULT_SORT,; DEFAULT_REPO_PAGES_LIMIT,; DEFAULT_REPO_NUMBER_LIMIT,; DEFAULT_PROFILE_NAME,; DEFAULT_EXCLUDE_FORKS,
    DEFAULT_DEST,
    DEFAULT_FILE,
    DEFAULT_OUTPUT,
)
from ghisa.core.profile import Profile
from ghisa.logger import logger

# from ghisa.core.ghisa import Ghisa


class ProfileCommand(Command):
    name = "run profile"

    description = "Run github profile session"

    arguments = [
        argument(
            "profile_name",
            description="The profile to analyze.",
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
        profile_name = self.argument("profile_name")

        # no flags options
        dest = self.option("dest")
        file = self.option("file")
        output = self.option("output")

        # flags options
        asynchronous = self.option("asynchronous")

        # # useless logging
        # logger.debug(f"url: {url}")

        # logger.debug(f"dest: {dest}")
        # logger.debug(f"file: {file}")
        # logger.debug(f"output: {output}")

        # logger.debug(f"search: {search}")
        # logger.debug(f"asynchronous: {asynchronous}")

        self.line("Eh! I'm running the command")

        Profile(
            profile_name=profile_name,
            dest=dest,
            file=file,
            # top_librairies=top_librairies,
            # config=config,
            # tmp=tmp,
            # force_unique=force_unique,
            # test_mode=test_mode,
            # sort=sort,
            # exclude_forks=exclude_forks,
            # repo_pages_limit=repo_pages_limit,
            # repo_number_limit=repo_number_limit,
            asynchronous=asynchronous,
        )
