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

## Acknowledgments
- [drivendata/cookiecutter-data-science](https://github.com/drivendata/cookiecutter-data-science)


## Requirements:
- [pre-commit](https://pre-commit.com/)
    ```
        pip install pre-commit
    ```
- [commit-lint](https://github.com/conventional-changelog/commitlint)
    ```
        npm install -g @commitlint/cli @commitlint/config-conventional
    ```

## Quick start 

The project can be built typing `make`.
