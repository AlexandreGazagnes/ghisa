"""
Exctract module
"""

import glob
import os

from ghisa.logger import logger


def get_folder_list(tmp):
    """Get the package name from a file"""

    li = [i for i in os.listdir(tmp) if (os.path.isdir(i) and (not i.startswith(".")))]
    return li


def make_python_file_list(self, tmp: str = "./tmp"):
    """Glob files to find .py or .iypnb Make the file list"""

    # notebooks
    query1 = os.path.join(tmp, "**/*.ipynb")
    l1 = glob.glob(query1, recursive=True)

    # python files
    query2 = os.path.join(tmp, "**/*.py")
    l2 = glob.glob(query2, recursive=True)

    return l1 + l2


def get_imports_line_from_file(filename):
    """Get the import lines from a file"""

    with open(filename, "r") as f:
        lines = f.readlines()

    lines = [i.strip() for i in lines]
    lines = [i.removeprefix('"') for i in lines]
    lines = [i for i in lines if i.startswith("import") or i.startswith("from")]

    return lines
