"""
Local module    
"""

from ghisa.logger import logger

from ..helpers import denest
from .extract import get_imports_line_from_file
from .helpers import clean_module_list, counter
from .transform import transform_import_line


def make_modules_list_from_file(filename, repo_name, tmp="./tmp") -> list:
    """Parse a file and return a list of modules used in the file"""

    lines = get_imports_line_from_file(filename)
    nested_modules = [transform_import_line(i) for i in lines]
    modules = denest(nested_modules)
    modules = clean_module_list(modules, repo_name=repo_name, tmp=tmp)

    logger.debug(f"modules : {modules}")

    return modules


def make_module_dict_from_file(filename, repo_name, tmp="./tmp") -> dict:
    """Parse a file and return a counter dictionary of modules used in the file and their counts"""

    module_list = make_modules_list_from_file(filename, repo_name=repo_name, tmp=tmp)
    module_dict = counter(module_list)

    return module_dict
