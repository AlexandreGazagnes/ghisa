from ghisa.logger import logger

import glob


def make_python_file_list(self, repo_name):
    """Glob files to find .py or .iypnb Make the file list"""

    query1 = repo_name + "**/*.ipynb"
    l1 = glob.glob(query1, recursive=True)

    query2 = repo_name + "**/*.py"
    l2 = glob.glob(query2, recursive=True)

    file_list = l1 + l2

    return file_list


def get_imports_line_from_file(
    filename,
):
    """Get the import lines from a file"""

    with open(filename, "r") as f:
        lines = f.readlines()

    lines = [i.strip() for i in lines]

    lines = [i.removeprefix('"') for i in lines]
    lines = [i for i in lines if i.startswith("import") or i.startswith("from")]

    return lines
