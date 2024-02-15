import os
import glob

import collections


def counter(li):

    c = collections.Counter(li)

    return dict(c)


def get_import(fn):
    """Get the import lines from a file"""

    with open(fn, "r") as f:
        lines = f.readlines()

    lines = [i.strip() for i in lines]
    lines = [i for i in lines if i.startswith("import") or i.startswith("from")]

    return lines


def extract_from_import_line(txt):
    """Extract the module name from an import line"""

    # From
    if txt.startswith("from"):
        txt = txt.split("from")[1]
        txt = txt.split("import")[0]
        # txt = txt.strip()
        # txt = txt.split(" ")[0]
        txt = txt.split(".")[0]
        return txt.strip()

    txt = txt.split("import ")[1]

    if "," in txt:
        txt = txt.split(",")
        txt = [i.strip() for i in txt]
        return txt

    txt = txt.split(".")[0]
    return txt.strip()


def parse_a_file(fn):
    """Parse a file"""

    lines = get_import(fn)
    modules = [extract_from_import_line(i) for i in lines]

    return modules
