#! /usr/bin/env python
#
# A module for working with HydroTrend.
#
# Mark Piper (mark.piper@colorado.edu)

import numpy as np


def load_series(output_file):
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
