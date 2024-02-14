"""
GUI Command
"""

import os

from cleo.commands.command import Command
from cleo.helpers import argument, option

import streamlit.web.cli as cli

from ghisa.gui.front import *


class GuiCommand(Command):
    """GUI Command"""

    name = "gui"
    description = "Launch Streamlit local Web App someone"

    def handle(self):
        self.line("Launching Streamlit Web App...")
        os.system("streamlit run awdible/gui/front.py")
