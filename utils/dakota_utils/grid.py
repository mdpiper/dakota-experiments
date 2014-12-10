#! /usr/bin/env python
#
# Dakota utility programs for gridding output.
#
# Mark Piper (mark.piper@colorado.edu)

import numpy as np
from scipy.interpolate import griddata

def grid_lhs(tab_data, nx, ny, boundsx, boundsy, response_index=-1):
    '''
    Grids...
    '''
    xy = tab_data['data'][1:3,]
    xy_t = np.transpose(xy)
    z = tab_data['data'][response_index,]
    
    # TODO
    grid_x, grid_y = np.mgrid[-10:30:40j, 0.1:6.1:30j]
    grid_z = griddata(xy_t, z, (grid_x, grid_y), method='cubic')

    return(grid_z, grid_x, grid_y)
