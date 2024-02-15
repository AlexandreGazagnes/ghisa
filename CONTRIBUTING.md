# Contributing

## About 

ghisa is an open-source project and we are always looking for more people to contribute to its development.

It could be by adding new features, fixing bugs, improving the documentation, or any other way you see fit.

Any help is welcome, and we will do our best to help you get started.

Any feedback is also welcome.


Pull requests are welcome.

For major changes, please open an issue first to discuss what you would like to change.



## Local development

- The complete test suite depends on having at least the following installed
  (possibly not a complete list)
  - git (Version 2.24.0 or above is required )
  - python3.10.x (Required by a test which checks different python versions)
  <!-- - tox (or venv) -->
  - poetry, pip, pipenv, virtualenv, or similar
  - poetry is the preferred tool for managing dependencies, highly recommended

### Setting up an environment

The project uses [Poetry](https://python-poetry.org/) to manage its dependencies.
Please install it using the following command :

```bash
pip install poetry
```

Then, please install the dependencies using the following command :

```bash
poetry install
```

Activate the environment using the following command :

```bash
poetry shell
```

And finally, install the pre-commit hooks using the following command :

```bash
pre-commit install
```


### Running a specific test

Running a specific test with the environment activated is as easy as:
`pytest tests -k test_the_name_of_your_test`

### Running all the tests

With the environment activated you can run all of the tests
using:
`pytest tests`



## Workflow


## Reading issues

Please read the [issues page](https://alexandregazagnes.github.io/ghisa/issues/) before creating a new issue.

Find a new issue to work on in the page. If you want to work on an issue, please comment on the issue to let others know that you are working on it.

##  Creating a new issue

Feel free to create a new issue if you have any question, suggestion, or if you want to report a bug.

You will find a template to fill in when creating a new issue.  

We have carefully crafted the template to help you provide the information we need to help you.

We will add relevant labels to your issue to help us keep track of it.


## Finding the good issue to work on  

Most important issues are tagged with the `good first issue` label.
Find relevant issues to work on by filtering the issues with the `good first issue`, `urgent`, `tricky` labels.

When you find an issue you want to work on, please comment on the issue to let others know that you are working on it.

You will have to make a comment to the issue in order to block it to other contributors.


## Creating a new branch

When you are ready to start working on an issue, please create a new branch from the issue page.

Please choose `dev` as the base branch and not `main`.

You will not habe to worry about the name of your branch : it will be automatically generated from the issue title.

Once you have created the branch, you can start working on the issue.


## Creating a pull request

When you are ready to submit your work, please create a pull request from the issue page.

** IMPORTANT ** : Please choose `dev` as the dest branch and not `main`.

You will have to fill in the pull request template.

We will review your pull request and give you feedback.

Once your pull request is approved, we will merge it into the `dev` branch.

We will then close the issue and add the `merged` label to it.