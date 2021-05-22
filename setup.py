"""Setup file"""
from typing import Tuple, List
import py2exe

from setuptools import setup, find_packages
package_name = "Catapulte jump"

PACKAGE_NAME = package_name  # The name of the package
VERSION = '0.0.1'
PYTHON_VERSION = '~=3.6'  # Any python 3 version since python3.6
SHORT_DESCRIPTION = ''
DESCRIPTION = open('README.md').read()
AUTHOR = ''
MAIL = ''
PROJECT_URL = 'https://github.com/$url_name/$project@latest'
LICENCE = 'GPLv3+'
DEVELOPMENT_STATUS = 'Planning'
ENVIRONMENT = []
FRAMEWORK = []
AUDIENCE = ['Developers']
PROGRAMMING_LANGUAGE = ['Pythonv3.6', 'Pythonv3.7', 'Pythonv3.8']

def get_requirements(filename: str) -> Tuple[List[str], List[str]]:
    """Get requirements and dependency from a file (like 'requirements.txt')

    This return the requirement and link to python package from a file formats for pip.
    You will want to use this function to make a bridge between a requirements.txt and
    setup.py

    :Example:

    >>> get_requirements('requirements.txt')
    (['test', 'nine'], ['git://github.com/psf/request/#egg=request'])

    :param filename: The path to the file
    :type filename: str
    :return: The list of requirements and a list of dependency
    :rtype: Tuple[List[str], List[str]]
    """
    requirements = open(filename, 'r').read().splitlines()

    install_requires = []
    dependency_links = []
    for requirement in requirements:
        if requirements[0] == '#':
            # It's a comment
            pass
        elif requirement[0:11] == '--index-url':
            # We are on a private pypi
            dependency_links.append(requirement[12:])
        elif requirement[0:2] == '-e':
            # The requirement use a version control systems
            dependency_links.append(requirement[3:])
        elif requirement[0:2] == '-r':
            # A link to an other file
            new_install_requires, new_dependency_links = get_requirements(requirement[3:])
            install_requires = install_requires + new_install_requires
            dependency_links = dependency_links + new_dependency_links
        else:
            install_requires.append(requirement)
    return install_requires, dependency_links


install_requires, dependency_links = get_requirements('requirements.txt')

# For more info see <https://python-packaging.readthedocs.io/en/latest/metadata.html>
setup(
    windows="src/main.py",
    name=PACKAGE_NAME,
    version=VERSION,
    description=SHORT_DESCRIPTION,
    long_description=DESCRIPTION,
    long_description_content_type='text/markdown',
    url=PROJECT_URL,
    author=AUTHOR,
    author_email=MAIL,
    license=LICENCE,
    python_requires=PYTHON_VERSION,
    packages=find_packages(),
    install_requires=install_requires,
    dependency_links=dependency_links,
    include_package_data=True,
    zip_safe=False
)
