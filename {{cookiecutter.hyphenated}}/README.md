# {{ cookiecutter.hyphenated }}

[![CI](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.hyphenated }}/actions/workflows/test.yml/badge.svg?event=push)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.hyphenated }}/actions/workflows/test.yml)
[![pypi](https://img.shields.io/pypi/v/{{ cookiecutter.hyphenated }}.svg)](https://pypi.python.org/pypi/{{ cookiecutter.hyphenated }})
[![versions](https://img.shields.io/pypi/pyversions/{{ cookiecutter.hyphenated }}.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.hyphenated }})
[![license](https://img.shields.io/github/license/{{ cookiecutter.github_username }}/{{ cookiecutter.hyphenated }}.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.hyphenated }}/blob/main/LICENSE)

## Installation

```bash
pip install {{ cookiecutter.hyphenated }}
```

## Usage

An example

```py
import {{ cookiecutter.hyphenated }}

print("An example!")
```

## Development

Prerequisites:

- Any Python 3.8 through 3.12
- [poetry](https://github.com/python-poetry/poetry) for dependency management
- git
- make (to use the helper scripts in the Makefile)

Autoformatting can be applied by running

```bash
make lintable
```

Before commiting, remember to run

```bash
make lint
make test
```
