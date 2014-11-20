#! /usr/bin/env python

from ez_setup import use_setuptools # https://pypi.python.org/pypi/setuptools
use_setuptools()
from setuptools import setup, find_packages
from experiments import __version__

setup(
    name='dakota_experiments',
    version=__version__,
    description='Experiments on CSDMS models with the DAKOTA iterative systems analysis toolkit',
    url='https://github.com/mdpiper/dakota-experiments',
    author='Mark Piper',
    author_email='mark.piper@colorado.edu',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='CSDMS modeling DAKOTA',
    packages=find_packages(),
    install_requires=['numpy', 'matplotlib'],
    entry_points={
        'console_scripts': [
            'run_dakota = experiments.scripts.run:main',
            ],
        },
    )
