"""
Transform module
"""

import pandas as pd


def _over_clean(txt):

    txt = txt.strip()
    txt = txt.split(" as")[0]

    txt = txt.strip()
    txt = txt.split(".")[0]

    txt = txt.strip()
    txt = txt.split(" as")[0]

    return txt.strip()


def _extract_from_mode(txt):

    if txt.startswith("from ."):
        return []

    txt = txt.split("from")[1]
    txt = txt.split("import")[0]
    txt = _over_clean(txt)

    return [txt.strip()]


def _extract_normal_mode(txt):

    if txt.startswith("import ."):
        return []

    if "," in txt:
        li = txt.split(",")
        li = [i.strip() for i in li]
        li = [i.split(" as")[0] for i in li]
        li = [i.strip() for i in li]

        return li

    txt = txt.split(".")[0]

    txt = _over_clean(txt)

    return [txt.strip()]


def extract_from_import_line(txt):
    """Extract the module name from an import line"""

    return (
        _extract_from_mode(txt) if txt.startswith("from") else _extract_normal_mode(txt)
    )


def extract_from_import_line(txt):
    """Extract the module name from an import line"""

    return (
        _extract_from_mode(txt) if txt.startswith("from") else _extract_normal_mode(txt)
    )


def parse_a_file(fn):
    """Parse a file"""

    lines = get_import(fn)
    nested_modules = [extract_from_import_line(i) for i in lines]

    modules = []
    for module in nested_modules:
        modules.extend(module)

    modules = [i for i in modules if i]
    modules = [i for i in modules if i not in dir(__builtins__)]

    extras = ["os"]
    modules = [i for i in modules if i not in extras]

    # logger.info(f"") = modules

    return modules


def make_final_data(df, top=20):

    df = pd.DataFrame(df)

    # logging.info(f"df = {df.to_dict(orient='records')}")

    ans = df.sum(axis=0).sort_values(ascending=False)
    ans = ans.head(top)

    ans = ans.to_dict()

    return ans
