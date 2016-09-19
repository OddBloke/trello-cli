"""
A CLI for Trello
"""
from setuptools import find_packages, setup

dependencies = [
    'click<7',
    'py-trello',
]


setup(
    name='trello-cli',
    version='0.1.0',
    license='AGPLv3',
    author='Daniel Watkins',
    author_email='daniel@daniel-watkins.co.uk',
    description='',
    long_description=__doc__,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    platforms='any',
    install_requires=dependencies,
    entry_points={
        'console_scripts': [
            'trello = trello_cli:main',
        ],
    },
)


