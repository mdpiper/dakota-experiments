#! /usr/bin/env python
#
# Dakota utility programs.
#
# Mark Piper (mark.piper@colorado.edu)

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


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


def plot_tabular_2d(tab_data, response_index=-1, title='Dakota Output', 
                    show=False, outfile='dakota_output.png'):
    '''
    Displays a surface plot of tabular output from a Dakota parameter
    study with two parameters and one or more response functions.
    '''
    x = tab_data['data'][1,]
    y = tab_data['data'][2,]
    z = tab_data['data'][response_index,]

    m = len(set(x))
    n = len(set(y))

    X = x.reshape(m,n)
    Y = y.reshape(m,n)
    Z = z.reshape(m,n)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1)
    ax.set_xlabel(tab_data['names'][1])
    ax.set_ylabel(tab_data['names'][2])
    ax.set_zlabel(tab_data['names'][response_index])
    plt.title(title)

    # Either show plot or save it to a PNG file.
    if show == True:
        plt.show(block=False)
    else:
        plt.savefig(outfile, dpi=96)
        plt.close()
