<!-- ![image](./docs/assets/img/image.png) -->
<!-- [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) -->
![Python](https://img.shields.io/badge/python-3.10.x-green.svg)
![Repo Size](https://img.shields.io/github/repo-size/AlexandreGazagnes/ghisa)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)
[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
<!-- ![Coverage](https://github.com/AlexandreGazagnes/ghisa/blob/main/docs/assets/img/cov.svg?raw=true) -->
![Tests](https://github.com/AlexandreGazagnes/ghisa/actions/workflows/tests.yaml/badge.svg)
![Statics](https://github.com/AlexandreGazagnes/ghisa/actions/workflows/statics.yaml/badge.svg)
![Doc](https://github.com/AlexandreGazagnes/ghisa/actions/workflows/docs.yaml/badge.svg)
![Pypi](https://github.com/AlexandreGazagnes/ghisa/actions/workflows/publish.yaml/badge.svg)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/AlexandreGazagnes/ghisa)

# ghisa - Github Import Statistic Analyzer 

## About
ghisa is a free and open-source software, app and python package that allows that helps you to analyze the import statistics of your github repositories.

## Key Features

Main features of ghisa are:
- Import statistics of your github repositories
- Import statistics of your github profile

## Installation

Using regular pip and venv tools :

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install ghisa
```

## Usage


### Local


#### As executable

In a terminal :
* ```ghisa repo [my-github-repo] ``` standard usage


* ```ghisa repo -f my_file.txt [my-github-repo]  ``` specify a file list output

* ```ghisa profile [profile-name] ``` specify a profile name and output



#### As library

In a terminal :

```python
from ghisa import Repo, Profile

repo_url  = "https://github.com/AlexandreGazagnes/ghisa"

repo = Repo(repo_url)
print(repo)

# or

profile_name = "AlexandreGazagnes"
profile = Profile(profile_name)
print(profile)
```

#### As local web app

In a terminal :


* ```ghisa gui ``` launch local streamlit

### On line

* The on line web app is temporarily unavailable. It will be available in the `0.1.0` release.


## Documentation

Please visit [Documentation](https://alexandregazagnes.github.io/ghisa/) page.


## Updates


Please visit the 
- [Changelog](https://alexandregazagnes.github.io/ghisa/changelog) page 
- [Roadmap](https://github.com/AlexandreGazagnes/ghisa/projects?query=is%3Aopen) page
- [Release](https://github.com/AlexandreGazagnes/ghisa/releases) page
- [Issues](https://github.com/AlexandreGazagnes/ghisa/issues) page


## Contributing

ghisa is an open-source project and we are always looking for more people to contribute to its development.

It could be by adding new features, fixing bugs, improving the documentation, or any other way you see fit.

Any help is welcome, and we will do our best to help you get started.

Any feedback is also welcome.

Please visit [Contributing](https://alexandregazagnes.github.io/ghisa/contributing) page.
