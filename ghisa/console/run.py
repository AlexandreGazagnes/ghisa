"""
Run command
"""

import os

from cleo.commands.command import Command
from cleo.helpers import argument, option

from ghisa.core.ghisa import Ghisa
from ghisa.logger import logger


class RunCommand(Command):
    """Run Awdible session"""

    name = "run"

    description = "Run Awdible session"

    arguments = [
        argument(
            "url",
            description="The url to analyze.",
            optional=True,
            # default=Awdible.DEFAULT_VIDEO_URL,
        )
    ]
    options = [
        option(
            "dest",
            "d",
            description="The destination directory of the file",
            flag=False,
            default=Awdible.DEFAULT_DEST,
        ),
        option(
            "file",
            "f",
            description="The input file With list of urls/videos",
            flag=False,
        ),
        option(
            "output",
            "o",
            description="The output file name",
            flag=False,
            default=Awdible.DEFAULT_OUTPUT,
        ),
        option(
            "search",
            "s",
            description="If set, the video argument will be treated as a search query and the first result will be downloaded.",
            flag=True,
        ),
        option(
            "asynchronous",
            "a",
            description="If set, the download will be asynchronous.",
            # This means that the download will be done in the background and the command will return immediately. The download progress can be checked using the `awdible progress` command.
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

        # useless logging
        logger.debug(f"url: {url}")

        logger.debug(f"dest: {dest}")
        logger.debug(f"file: {file}")
        logger.debug(f"output: {output}")

        logger.debug(f"search: {search}")
        logger.debug(f"asynchronous: {asynchronous}")

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
