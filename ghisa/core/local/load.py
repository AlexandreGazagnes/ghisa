"""
Load module
"""


def save(ans, dest=None):

    with open(dest, "w") as f:
        f.write(str(ans))
