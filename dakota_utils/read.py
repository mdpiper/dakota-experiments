#! /usr/bin/env python
#
# Dakota utility programs for reading output.
#
# Mark Piper (mark.piper@colorado.edu)

import re
import numpy as np


def get_labels(params_file):
    '''
    Uses a regular expression to extract labels from a Dakota parameters file.
    '''
    labels = []
    try:
        fp = open(params_file, 'r')
        for line in fp:
            if re.search('ASV_', line):
                labels.append(''.join(re.findall(':(\S+)', line)))
    except IOError:
        raise
    finally:
        fp.close()
        return(labels)


def get_names(dat_file):
    '''
    Reads the header from Dakota tabular graphics file. Returns a list
    of variable names.
    '''
    with open(dat_file, 'r') as fp:
        names = fp.readline().split() 
    return names


def get_data(dat_file):
    '''
    Reads the data from Dakota tabular graphics file. Returns a numpy array.
    '''
    return np.loadtxt(dat_file, skiprows=1, unpack=True)


def read_tabular(dat_file):
    '''
    Reads a Dakota tabular graphics file. Returns a dict with variable
    names and a numpy array with data.
    '''
    names = get_names(dat_file)
    data = get_data(dat_file)
    return {'names':names, 'data':data}
