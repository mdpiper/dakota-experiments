#! /usr/bin/env python
#
# Functions for working with files.
#
# Mark Piper (mark.piper@colorado.edu)

import os
import shutil
from subprocess import check_call, CalledProcessError


def remove(target):
    '''
    Deletes a file or directory. Silently passes if the file or directory
    doesn't exist.
    '''
    try:
        remove_file(target)
        remove_directory(target)
    except OSError:
        pass


def remove_file(fname):
    '''
    Deletes a file. Silently passes if the file doesn't exist.
    '''
    try:
        os.remove(fname)
    except OSError:
        pass


def remove_directory(dname):
    '''
    Recursively deletes a directory. Silently passes if the directory
    doesn't exist.
    '''
    try:
        shutil.rmtree(dname)
    except OSError:
        pass


def touch(fname):
    '''
    Touches a file.
    '''
    try:
        check_call(['touch', fname])
    except CalledProcessError:
        raise
