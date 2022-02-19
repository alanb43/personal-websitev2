"""
Insta485 python package configuration.

Andrew DeOrio <awdeorio@umich.edu>

Taken for swetter (personal website)
    by Alan Bergsneider <bera@umich.edu>
"""

from setuptools import setup

setup(
    name='swetter',
    version='0.1.0',
    packages=['swetter'],
    include_package_data=True,
    install_requires=[
        'arrow',
        'bs4',
        'Flask',
        'html5validator',
        'pycodestyle',
        'pydocstyle',
        'pylint',
        'pytest',
        'requests',
        'selenium',
    ],
    python_requires='>=3.6',
)
