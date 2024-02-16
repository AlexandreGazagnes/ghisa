"""
Local module    
"""

from .extract import get_imports_line_from_file

from .transform import transform_import_line
from .helpers import denest_module_list, clean_module_list, counter


def make_modules_list_from_file(filename, repo_name) -> list:
    """Parse a file and return a list of modules used in the file"""

    lines = get_imports_line_from_file(filename)

    nested_modules = [transform_import_line(i) for i in lines]

    modules = denest_module_list(nested_modules)

    modules = clean_module_list(modules, repo_name=repo_name)

    # logger.info(f"") = modules

    return modules


def make_module_dict_from_file(filename, repo_name) -> dict:
    """Parse a file and return a counter dictionary of modules used in the file and their counts"""

    module_list = make_modules_list_from_file(filename, repo_name=repo_name)

    module_dict = counter(module_list)

    return module_dict
