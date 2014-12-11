#! /usr/bin/env python
#
# Functions for working with files.
#
# Mark Piper (mark.piper@colorado.edu)

import os
from subprocess import check_call


def remove(file):
    '''
    Deletes a file. Silently passes if the file doesn't exist.
    '''
    try:
        os.remove(file)
    except OSError:
        pass


def touch(file):
    '''
    Touches a file.
    '''
    try:
        check_call(['touch', file])
    except CalledProcessError:
        raise
