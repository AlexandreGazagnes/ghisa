"""
Load module
"""

import os
import shutil


def clone_repo(repo_url, tmp: str = "./tmp"):
    """Clone the repository"""

    # TODO : implement vaidator url

    if os.path.exists(tmp):
        # os.rmdir(tmp)
        shutil.rmtree(tmp)

    if not os.path.exists(tmp):
        os.makedirs(tmp)

    os.system(f"git clone {repo_url} {tmp}")
    os.system(f"rm -rf {tmp}/.git")
