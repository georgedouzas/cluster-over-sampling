"""Development tasks."""

import os
from glob import glob
from pathlib import Path

import nox

os.environ.update({'PDM_IGNORE_SAVED_PYTHON': '1', 'PDM_USE_VENV': '1'})

PYTHON_VERSIONS = ['3.10', '3.11']
FILES = ['src', 'tests', 'docs', 'noxfile.py']


@nox.session
def build_docs(session: nox.Session) -> None:
    """Build the documentation.

    Arguments:
        session: The nox session.
    """
    session.run('mkdocs', 'build', external=True)


@nox.session
def serve_docs(session: nox.Session) -> None:
    """Serve the documentation.

    Arguments:
        session: The nox session.
    """
    session.run('mkdocs', 'serve', external=True)


@nox.session
def deploy_docs(session: nox.Session) -> None:
    """Deploy the documentation.

    Arguments:
        session: The nox session.
    """
    session.run('mkdocs', 'gh-deploy', external=True)


@nox.session
@nox.parametrize('file', FILES)
def format_code(session: nox.Session, file: str) -> None:
    """Format the code.

    Arguments:
        session: The nox session.
        file: The file to be formatted.
    """
    session.run('black', file, external=True)
    session.run('docformatter', '--in-place', '--recursive', '--close-quotes-on-newline', file, external=True)


@nox.session
@nox.parametrize('file', FILES)
def check_quality(session: nox.Session, file: str) -> None:
    """Check code quality.

    Arguments:
        session: The nox session.
        file: The file to be checked.
    """
    session.run('ruff', file, external=True)


@nox.session(python=PYTHON_VERSIONS)
def check_dependencies(session: nox.Session) -> None:
    """Check for vulnerabilities in dependencies.

    Arguments:
        session: The nox session.
    """
    requirements_path = (Path(session.create_tmp()) / 'requirements.txt').as_posix()
    session.run('pdm', 'install', '-dG', 'check-dependencies', '--no-default', external=True)
    session.run('pdm', 'export', '-f', 'requirements', '--without-hashes', '-o', requirements_path, external=True)
    session.run('safety', 'check', '-r', requirements_path)


@nox.session(python=PYTHON_VERSIONS)
@nox.parametrize('file', ['src', 'tests', 'docs', 'noxfile.py'])
def check_types(session: nox.Session, file: str) -> None:
    """Check type annotations.

    Arguments:
        session: The nox session.
        file: The file to be checked.
    """
    session.run('pdm', 'install', '-dG', 'check-types', '--no-default', external=True)
    session.run('mypy', file)


@nox.session(python=PYTHON_VERSIONS)
def test(session: nox.Session) -> None:
    """Run tests.

    Arguments:
        session: The nox session.
    """
    session.run('pdm', 'install', '-dG', 'test', external=True)
    env = {'COVERAGE_FILE': f'.coverage.{session.python}'}
    if session.posargs:
        session.run('pytest', '-n', 'auto', '-k', *session.posargs, 'tests', env=env)
    else:
        session.run('pytest', '-n', 'auto', 'tests', env=env)


@nox.session
def coverage(session: nox.Session) -> None:
    """Run test coverage.

    Arguments:
        session: The nox session.
    """
    if not glob('.coverage*'):
        session.error(
            'No coverage data were found. Please run `pdm test` to run the tests and generate the coverage data',
        )
    if glob('.coverage.*'):
        session.run('coverage', 'combine', external=True)
    session.run('coverage', 'report', external=True)
    session.run('coverage', 'html', external=True)


@nox.session
def release(session: nox.Session, version: str) -> None:
    """Release a new Python package.

    Arguments:
        session: The nox session.
        version: The new version number to use.
    """
    version = session.posargs[0]
    session.run('git', 'add', 'pyproject.toml', 'CHANGELOG.md', external=True)
    session.run('git', 'commit', '-m', f'Release {version}', external=True)
    session.run('git', 'tag', version, external=True)
    session.run('git', 'push', external=True)
    session.run('git', 'push', '-tags', external=True)
    session.run('pdm', 'build', external=True)
    session.run('twine', 'upload', '--skip-existing', 'dist/*', external=True)