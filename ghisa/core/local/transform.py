"""
Transform module
"""

from .helpers import over_clean_import_statement
import pandas as pd

from ghisa.logger import logger


def __transform_from_mode(txt):

    if txt.startswith("from ."):
        return []

    txt = txt.split("from")[1]
    txt = txt.split("import")[0]
    txt = over_clean_import_statement(txt)

    return [txt]


def __transform_import_mode(txt):

    if txt.startswith("import ."):
        return []

    if "," in txt:
        li = txt.split(",")
        li = [over_clean_import_statement(i) for i in li]
        return li

    txt = txt.split(".")[0]

    txt = over_clean_import_statement(txt)

    return [txt]


def transform_import_line(txt):
    """Extract the module name from an import line"""

    txt = txt.strip()

    if txt.startswith("import"):
        return __transform_import_mode(txt)

    elif txt.startswith("from"):
        return __transform_from_mode(txt)

    else:
        raise AttributeError(f"line code not starting with import or from : {txt}")


"""
Transform module
"""


def make_final_df(dict_list, top_librairies=20):
    """Make the final dataframe from the list of dictionaries of modules used in the files of the repository"""

    df = pd.DataFrame(dict_list)

    # logging.info(f"df = {df.to_dict(orient='records')}")

    ans = df.sum(axis=0).sort_values(ascending=False)
    ans = ans.head(top_librairies)
    ans = ans.to_dict()

    logger.info(f"final ans = {ans}")

    return ans
