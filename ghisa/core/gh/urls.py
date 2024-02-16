"""
url module
"""


def make_profile_url(profile):
    """Method to make the profile url from the profile name

    Args:
        profile (str): The profile name on github ex : AlexandreGazagnes"""

    profile_url = "https://github.com/" + profile

    return profile_url


def make_repo_list_url(profile_url, page=0, sort=None):
    """Method to make the repository list url from the profile url"""

    profile_url.removesuffix("/")
    repo_list_url = profile_url + "?tab=repositories"

    if sort == "stars":
        repo_list_url += "&sort=stargazers"

    if page:
        repo_list_url += f"&page={page}"

    # TODO : AJOUTER OPTION PAS LES FORKS
    # 30 repo per page

    return repo_list_url


def make_git_repo_url(profile_url, repo_name, ext=".git"):
    """from a profile url and a repo name, build the repo url"""

    if not profile_url.endswith("/"):
        profile_url = profile_url + "/"

    repo_url = profile_url + repo_name
    repo_url = repo_url.removesuffix("/")
    repo_url = repo_url + ext

    return repo_url
