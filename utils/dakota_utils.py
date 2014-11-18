#! /usr/bin/env python
#
# Dakota utility programs.
#
# Mark Piper (mark.piper@colorado.edu)

import numpy as np


def get_names(dat_file):
    '''
    Reads the header from Dakota tabular graphics file. Returns a list
    of variable names.
    '''
    fp = open(dat_file, 'r')
    return fp.readline().split()


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
