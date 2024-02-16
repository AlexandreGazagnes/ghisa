import asyncio

import github


async def get_user():
    client = await github.GHClient()

    user = await client.get_user(user="AlexandreGazagnes")

    print(user)
    print(user.html_url)

    return user


user = asyncio.run(get_user())


async def get_repo():
    """ """

    client = await github.GHClient()
    _repo = await client.get_repo(owner="AlexandreGazagnes", repo="P7_scoring_ML")

    return _repo


repo = asyncio.run(get_repo())
