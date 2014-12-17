#! /usr/bin/env python
#
# A module for working with HydroTrend.
#
# Mark Piper (mark.piper@colorado.edu)

import subprocess
import numpy as np


def load(output_file):
    '''
    Reads a column of text containing HydroTrend output. Returns a numpy array,
    or None on an error.
    '''
    try:
        series = np.loadtxt(output_file, skiprows=2)
    except (IOError, StopIteration):
        pass
    else:
        return(series)


def is_in_path():
    '''
    Returns True if the HydroTrend executable is in the path.
    '''
    try:
        subprocess.call(['hydrotrend', '--version'])
    except OSError:
        return False
    else:
        return True


def call(input_dir, output_dir):
    '''
    Invokes HydroTrend through the shell.
    '''
    call(['hydrotrend', '--in-dir', input_dir, '--out-dir', output_dir])
