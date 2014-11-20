#! /usr/bin/env python

from ez_setup import use_setuptools # https://pypi.python.org/pypi/setuptools

use_setuptools()

from setuptools import setup, find_packages
from setuptools.command.install import install

from experiments import __version__

setup(
    name='foobar',
    version=__version__,
    description='Experiments on CSDMS models with the DAKOTA iterative systems analysis toolkit',
    url='http://csdms.colorado.edu',
    author='Mark Piper',
    author_email='mark.piper@colorado.edu',
    license='MIT',
    packages=find_packages(exclude='test*'),
    install_requires=['numpy', 'matplotlib'],
    entry_points={
        'console_scripts': [
            'run_dakota = experiments.scripts.run:main',
            ],
        },
    )
