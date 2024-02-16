"""
Helper functions
"""

import collections

from ghisa.logger import logger

from .builtins_modules import buildin_list
from .extract import get_folder_list


def over_clean_import_statement(txt):
    """Clean the import statement"""

    logger.debug("txt before clean = " + txt)

    txt = txt.strip()
    if txt.startswith("import "):
        txt = txt.removeprefix("import ")

    txt = txt.strip()
    txt = txt.split(" as")[0]

    txt = txt.strip()
    txt = txt.split(".")[0]

    # txt = txt.strip()
    # txt = txt.split(" as")[0]

    txt = txt.strip()
    txt = txt.removesuffix("\n")
    txt = txt.removesuffix("\\n")
    txt = txt.removesuffix('\\n"')
    txt = txt.removesuffix(";")
    txt = txt.strip()

    # TODO: enmable package selection : only if in pypi_list

    logger.debug("txt after clean = " + txt)

    return txt


def counter(module_list):
    """Count the number of occurences of each module in the list of modules"""

    c = collections.Counter(module_list)
    c = dict(c)

    return c


def clean_module_list(module_list, repo_name=None, tmp="./tmp"):
    """Clean the module list from unwanted modules"""

    module_list = [i for i in module_list if i]
    # module_list = [i for i in module_list if i not in dir(__builtins__)]

    module_list = [over_clean_import_statement(i) for i in module_list]
    module_list = [i for i in module_list if i not in buildin_list]

    extras = [
        "src",
        "time",
        "datetime",
        "os",
        "sys",
        "re",
        "json",
        "pathlib",
        "path",
        "random",
        "string",
        "math",
    ]
    module_list = [i for i in module_list if i not in extras]
    module_list = [i for i in module_list if i != repo_name]

    module_list = [i for i in module_list if i not in get_folder_list(tmp)]
    # module_list = [i for i in module_list if i]
    module_list = [i.strip() for i in module_list]

    return module_list


def get_repo_name_from_repo_url(repo_url):
    """Extract the repository name from the repository url"""

    repo_url = repo_url.split(".git")[0]
    repo_name = repo_url.split("/")[-1]

    return repo_name
