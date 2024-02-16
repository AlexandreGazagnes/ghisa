def over_clean_import_statement(txt):

    txt = txt.strip()
    txt = txt.split(" as")[0]

    txt = txt.strip()
    txt = txt.split(".")[0]

    txt = txt.strip()
    txt = txt.split(" as")[0]

    return txt.strip()


def counter(li):

    c = collections.Counter(li)

    return dict(c)


def denest_modules(nested_modules):

    modules = []
    for module in nested_modules:
        modules.extend(module)

    return modules


def clean_modues(modules):

    modules = [i for i in modules if i]
    modules = [i for i in modules if i not in dir(__builtins__)]

    extras = ["os"]
    modules = [i for i in modules if i not in extras]

    return modules
