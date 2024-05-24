import {{ cookiecutter.underscored }}


def test_version() -> None:
    assert {{ cookiecutter.underscored }}.__version__ is not None
