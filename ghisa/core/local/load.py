"""
Load module
"""


def save(ans, dest):

    with open(dest, "w") as f:
        f.write(str(ans))
