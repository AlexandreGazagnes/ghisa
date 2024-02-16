"""
Console Application
"""

from cleo.application import Application

from .gui import GuiCommand
from .profile import ProfileCommand
from .repo import RepoCommand

# from cleo.commands.command import Command
# from cleo.helpers import argument, option


# class GuiCommand(Command):
#     """GUI Command"""

#     name = "gui"
#     description = "Launch Streamlit local Web App someone"

#     def handle(self):

#         self.line("Launching Streamlit Web App...")


def main() -> int:
    """Main function of the console application"""

    # app
    application = Application()

    # commands
    application.add(GuiCommand())
    application.add(RepoCommand())
    application.add(ProfileCommand())

    # run
    exit_code: int = Application().run()

    return exit_code


if __name__ == "__main__":
    # application = Application()
    # application.add(GuiCommand())
    # application.add(ProfileCommand())
    # application.add(RepoCommand())

    # application.run()

    main()
