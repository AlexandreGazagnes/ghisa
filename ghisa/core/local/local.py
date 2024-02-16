def parse_a_file(fn):
    """Parse a file"""

    lines = get_import(fn)
    nested_modules = [extract_from_import_line(i) for i in lines]

    modules = denest_modules(nested_modules)

    modules = clean_modues(modules)

    # logger.info(f"") = modules

    return modules
