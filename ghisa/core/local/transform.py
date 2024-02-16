def _transform_from_mode(txt):

    if txt.startswith("from ."):
        return []

    txt = txt.split("from")[1]
    txt = txt.split("import")[0]
    txt = over_clean_import_statement(txt)

    return [txt.strip()]


def _transform_import_mode(txt):

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

    return (
        _transform_from_mode(txt)
        if txt.startswith("from")
        else _transform_import_mode(txt)
    )


def make_final_data(df, top_librairies=20):

    df = pd.DataFrame(df)

    # logging.info(f"df = {df.to_dict(orient='records')}")

    ans = df.sum(axis=0).sort_values(ascending=False)
    ans = ans.head(top_librairies)
    ans = ans.to_dict()

    return ans
