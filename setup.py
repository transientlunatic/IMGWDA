# -*- coding: utf-8 -*-

from setuptools import setup

import versioneer

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

requirements = [
    'numpy',
    'pandas',
    'lalsuite',
    'pycbc'
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='thesis',
    version='0.0.1',
    #version=versioneer.get_version(),
    #description="""A Python package for managing and interacting with gravitational waveform catalogues.""",
    long_description=readme + '\n\n' + history,
    author="Daniel Williams",
    author_email='daniel.williams@ligo.org',
    #url='https://github.com/transientlunatic/elk',
    packages=['thesis'],
    package_dir={'thesis': 'thesis'},
    # entry_points={
    #     'console_scripts': [
    #         'elk=elk.cli:main'
    #     ]
    # },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=True,
)
