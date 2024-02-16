def clone_repo(repo_url, tmp):
    """Clone the repository"""

    if not os.path.exists(tmp):
        os.makedirs(tmp)

    # if not repo_url.startswith("https://github.com"):
    #     raise ValueError(f"Expected {repo_url} to be a github url")

    if not repo_url.endswith(".git"):
        repo_url = repo_url + ".git"

    os.system(f"git clone {repo_url} {tmp}")
    os.system(f"rm -rf {tmp}/.git")

    repo_name = f"./{tmp}/"
    return repo_name
