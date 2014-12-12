#! /usr/bin/env python
#
# Functions for working with files.
#
# Mark Piper (mark.piper@colorado.edu)

import os
from subprocess import check_call


def remove(fname):
    '''
    Deletes a file. Silently passes if the file doesn't exist.
    '''
    try:
        os.remove(fname)
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
