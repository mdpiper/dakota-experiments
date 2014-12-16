#! /usr/bin/env python
#
# Dakota utility programs for gridding output.
#
# Mark Piper (mark.piper@colorado.edu)

import numpy as np
from scipy.interpolate import griddata

def grid_lhs(tab_data, nxy, boundsx, boundsy, response_index=-1):
    '''
    Interpolates a response function defined at a set of irregular 
    LHS locations to a regular grid.
    '''
    xy = tab_data['data'][1:3,]
    xy_t = np.transpose(xy)
    z = tab_data['data'][response_index,]
    
    # np.mgrid is tricky.
    grid_x, grid_y = np.mgrid[boundsx[0]:boundsx[1]:complex(nxy[0]), \
                              boundsy[0]:boundsy[1]:complex(nxy[1])]
    grid_z = griddata(xy_t, z, (grid_x, grid_y), method='cubic')

    return(grid_z, grid_x, grid_y)
