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

# I stole this from @mcflugen.
def read_requirements():
    import os
    path = os.path.dirname(os.path.abspath(__file__))
    requirements_file = os.path.join(path, 'requirements.txt')
    try:
        with open(requirements_file, 'r') as f:
            requires = f.read().split()
    except IOError:
        return []
    else:
        return [r.split() for r in requires]

setup(
    name='dakota_utils',
    version=__version__,
    description='Systems analysis computer experiments on CSDMS models',
    long_description=open('README.md').read(),
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
    install_requires=read_requirements(),
    entry_points={
        'console_scripts': [
            run_script + ' = dakota_utils.run:main',
            cleanup_script + ' = dakota_utils.cleanup:main',
            convert_script + ' = dakota_utils.convert:main'
            ],
        },
    )
