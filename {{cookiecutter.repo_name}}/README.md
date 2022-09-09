# {{cookiecutter.project_name}}

{{cookiecutter.project_desc}}

Started on {{cookiecutter.start_date}}.

## Project Organization

```
├── LICENSE
├── Makefile           <- Makefile with commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── datasets
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── final          <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── docs               <- Code documentation and generated analysis as HTML, PDF, LaTeX, etc.
│   └── images         <- Generated graphics and figures to be used in reporting
|   └── reports        <- Generated analysis as HTML, PDF, LaTeX, etc.
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── src                <- Source code for use in this project.
|__ output             <- Temporary Output files
```
## Features
- Commit Message checking via commitlint
- [Linter support for R lang](https://github.com/r-lib/lintr)
- [R Lang Code formatter using Styler](https://github.com/r-lib/styler)
- [R lang general checks using pre-commit hooks](https://lorenzwalthert.github.io/precommit/articles/available-hooks.html)
- [Local Testing via pre-commit](https://pre-commit.com/)
- Github Integration 
- CI testing via Github actions and pre-commit.ci
- Github CODEOWNERS to automatically add owners to Github PR
- Github pull request remplates for standardizing description
- Multiple programming language support in the directory structure

## Requirements:
- [pre-commit](https://pre-commit.com/)
    ```
        pip install pre-commit
    ```
- [commitlint](https://github.com/conventional-changelog/commitlint)
    ```
        npm install -g @commitlint/cli @commitlint/config-conventional
    ```
    for this Nodejs is required. Download and install from here [Nodejs](https://nodejs.org/en/download/)

## Acknowledgments
- [drivendata/cookiecutter-data-science](https://github.com/drivendata/cookiecutter-data-science)
- [pal0064/ml-project-template](https://github.com/pal0064/ml-project-template)