def make_soup(repo_list_url):
    """Method to get the repository"""

    repo_list_url = repo_list_url + "?tab=repositories"

    response = requests.get(repo_list_url)

    # response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    return soup


def extract_repositories(soup, profile_url):
    """ """

    repos = soup.find_all("a", {"itemprop": "name codeRepository"})

    repos = [repo.text for repo in repos]

    # repos = [repo.href for repo in repos]

    logger.warning(repos)

    repos = [repo for repo in repos if repo != ""]
    repos = [repo.strip() for repo in repos]
    repos = [build_repo_url(profile_url, repo) for repo in repos]

    # <a href="/AlexandreGazagnes/ghisa" itemprop="name codeRepository">
    #     ghisa</a>

    return repos


def get_repositories(profile, page=0, sort=None):

    if page <= 1:
        profile_url = make_profile_url(profile)
        repo_list_url = make_repo_list_url(profile_url, page=page, sort=sort)

        soup = make_soup(repo_list_url)
        repos = extract_repositories(soup, profile_url)

        return repos

    else:
        raise NotImplementedError("Pagination not implemented yet")
