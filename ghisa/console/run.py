"""
Run command
"""

import os

from cleo.commands.command import Command
from cleo.helpers import argument, option

from ghisa.core.ghisa import Ghisa
from ghisa.logger import logger


class RunCommand(Command):
    """Run Ghisa session"""

    name = "run"

    description = "Run Ghisa session"

    arguments = [
        argument(
            "url",
            description="The url to analyze.",
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
            default=Ghisa.DEFAULT_DEST,
        ),
        option(
            "file",
            "f",
            description="The input file with list of [...]",
            flag=False,
            default=Ghisa.DEFAULT_FILE,
        ),
        option(
            "output",
            "o",
            description="The output file name",
            flag=False,
            default=Ghisa.DEFAULT_OUTPUT,
        ),
        option(
            "search",
            "s",
            description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla nec odio nec urna tincidunt tincidunt",
            flag=True,
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
        search = self.option("search")
        asynchronous = self.option("asynchronous")

        # # useless logging
        # logger.debug(f"url: {url}")

        # logger.debug(f"dest: {dest}")
        # logger.debug(f"file: {file}")
        # logger.debug(f"output: {output}")

        # logger.debug(f"search: {search}")
        # logger.debug(f"asynchronous: {asynchronous}")

        self.line("Eh! I'm running the command")

        Ghisa(
            url=url,
            dest=dest,
            file=file,
            output=output,
            search=search,
            asynchronous=asynchronous,
            streamlit=False,
        ).run()
