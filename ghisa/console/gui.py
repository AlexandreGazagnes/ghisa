"""
GUI Command
"""

import os

import streamlit.web.cli as cli
from cleo.commands.command import Command

from ghisa.gui.front import *

# from cleo.helpers import argument, option


class GuiCommand(Command):
    """GUI Command"""

    name = "gui"
    description = "Launch Streamlit local Web App someone"

    def handle(self):
        self.line("Launching Streamlit Web App...")
        os.system("streamlit run ghisa/gui/front.py")
