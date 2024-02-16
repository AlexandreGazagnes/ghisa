"""
Python script to get the top 1000 packages from 
pypi and save them to a file
"""

import logging
import requests
from bs4 import BeautifulSoup

# url = "https://hugovk.github.io/top-pypi-packages/"
url = "https://robert-96.github.io/top-pypi-packages/"


def main():
    """Get the top 1000 packages from pypi and save them to a file"""

    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")

    li = soup.find_all("a", {"class": "mr-1"})

    li = [i.text for i in li if i.text != ""]

    print(li)

    # with open(".utils/top_packages.txt", "w") as f:
    #     txt = "\n".join(li)
    #     f.write(txt)


if __name__ == "__main__":
    main()
