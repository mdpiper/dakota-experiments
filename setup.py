#! /usr/bin/env python
#
# dakota-experiments
#
# Mark Piper (mark.piper@colorado.edu)

from ez_setup import use_setuptools # https://pypi.python.org/pypi/setuptools
use_setuptools()
from setuptools import setup, find_packages
from experiments import __version__

# Get the long description from the README file.
def get_long_description():
    from codecs import open
    from os import path

    here = path.abspath(path.dirname(__file__))
    try:
        with open(path.join(here, 'README.md'), encoding='utf-8') as f:
            long_description = f.read()
    except:
        return []
    else:
        return long_description

setup(
    name='dakota-experiments',
    version=__version__,
    description='Systems analysis computer experiments on CSDMS models',
    long_description=get_long_description(),
    url='https://github.com/mdpiper/dakota-experiments',
    author='Mark Piper',
    author_email='mark.piper@colorado.edu',
    license='MIT',
    platforms=['any'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='CSDMS, earth systems modeling, DAKOTA, systems analysis',
    packages=find_packages(exclude=['*.tests']),
    install_requires=['numpy', 'matplotlib'],
    entry_points={
        'console_scripts': [
            'run_dakota = experiments.scripts.run:main',
            'cleanup_dakota = experiments.scripts.cleanup:main',
            ],
        },
    )
