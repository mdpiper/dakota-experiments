#! /usr/bin/env python
#
# Dakota utility programs for plotting output.
#
# Mark Piper (mark.piper@colorado.edu)

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


default_title = 'Dakota Output'
default_outfile = 'dakota_output.png'


def plot_surface(tab_data, response_index=-1, title=default_title,
                 show=False, outfile=default_outfile):
    '''
    Displays a surface plot of tabular output from a Dakota parameter
    study with two parameters and one or more response functions.
    '''
    x = tab_data['data'][1,]
    y = tab_data['data'][2,]
    z = tab_data['data'][response_index,]

    m = len(set(x))
    n = len(set(y))

    X = x.reshape(n,m)
    Y = y.reshape(n,m)
    Z = z.reshape(n,m)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1)
    ax.set_xlabel(tab_data['names'][1])
    ax.set_ylabel(tab_data['names'][2])
    ax.set_zlabel(tab_data['names'][response_index])
    plt.title(title)

    # Either show plot or save it to a PNG file.
    if show:
        plt.show(block=False)
    else:
        plt.savefig(outfile, dpi=96)
        plt.close()


def plot_samples(tab_data, show=False, outfile=default_outfile):
    '''
    Displays a scatterplot of 2D Latin Hypercube samples.
    '''
    x = tab_data['data'][1,]
    y = tab_data['data'][2,]
    n = len(x)

    plt.figure()
    plt.plot(x, y, marker='+', linestyle='')
    plt.xlabel(tab_data['names'][1])
    plt.ylabel(tab_data['names'][2])
    plt.title('LHS: ' + str(n) + ' samples, uniform distribution')

    if show:
        plt.show(block=False)
    else:
        plt.savefig(outfile, dpi=96)
        plt.close()


def plot_irregular_surface(tab_data, response_index=-1,
                           title=default_title, show=False,
                           outfile=default_outfile):
    '''
    Displays a surface plot of irregular Dakota tabular output (such as
    from a DACE experiment) interpolated to a regular grid.
    '''
    from .grid import grid_lhs

    # TODO
    gz, gx, gy = grid_lhs(tab_data, 40, 30, None, None, response_index)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(gx, gy, gz, rstride=1, cstride=1)
    ax.set_xlabel(tab_data['names'][1])
    ax.set_ylabel(tab_data['names'][2])
    ax.set_zlabel(tab_data['names'][response_index])
    plt.title(title)

    if show:
        plt.show(block=False)
    else:
        plt.savefig(outfile, dpi=96)
        plt.close()
