#! /usr/bin/env python
#
# Functions for working with files.
#
# Mark Piper (mark.piper@colorado.edu)

import os


def remove(file):
    '''
    Deletes a file. Silently passes if the file doesn't exist.
    '''
    try:
        os.remove(file)
    except OSError:
        pass

