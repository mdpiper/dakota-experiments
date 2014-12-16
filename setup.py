#! /usr/bin/env python
#
# The dakota_utils package setup.
#
# Mark Piper (mark.piper@colorado.edu)

from ez_setup import use_setuptools # https://pypi.python.org/pypi/setuptools
use_setuptools()
from setuptools import setup, find_packages
from dakota_utils import __version__, \
    run_script, cleanup_script, convert_script

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
    name='dakota_utils',
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
    install_requires=['numpy', 'matplotlib', 'scipy'],
    entry_points={
        'console_scripts': [
            run_script + ' = dakota_utils.run:main',
            cleanup_script + ' = dakota_utils.cleanup:main',
            convert_script + ' = dakota_utils.convert:main'
            ],
        },
    )
