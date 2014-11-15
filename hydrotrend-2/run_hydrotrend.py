#! /usr/bin/env python
# Brokers communication between HydroTrend and Dakota through files.
# Mark Piper (mark.piper@colorado.edu)

import sys
import os
import shutil
from subprocess import call
import numpy as np


def read(file):
    '''
    Reads a column of text containing HydroTrend output. Returns a numpy array.
    '''
    with open(file, 'r') as f:
        values = f.read().split('\n')

    return np.array(values[2:-1], dtype=np.float) # Remove header lines and EOF.


def write(file, array):
    '''
    Writes a Dakota results file from an input array.
    '''
    labels = ['Qs_mean', 'Qs_stdev']
    f = open(file, 'w')
    for i in range(len(array)):
        f.write(str(array[i]) + '\t' + labels[i] + '\n')
    f.close()


# Files and directories.
start_dir = os.path.dirname(os.path.realpath(__file__))
input_dir = os.path.join(start_dir, 'HYDRO_IN')
if not os.path.exists(input_dir): os.mkdir(input_dir)
output_dir = os.path.join(start_dir, 'HYDRO_OUTPUT')
if not os.path.exists(output_dir): os.mkdir(output_dir)
input_template = 'HYDRO.IN.template'
input_file = 'HYDRO.IN'
output_file = 'HYDROASCII.QS'

# Use the parsing utility `dprepro` (from $DAKOTA_DIR/bin) to
# incorporate the parameters from Dakota into the HydroTrend input
# template, creating a new HydroTrend input file.
shutil.copy(os.path.join(start_dir, input_template), os.curdir)
call(['dprepro', sys.argv[1], input_template, input_file])
shutil.copy(input_file, input_dir)

# Call HydroTrend, using the updated input file.
call(['hydrotrend', '--in-dir', input_dir, '--out-dir', output_dir])

# Calculate mean and standard deviation of Qs for the simulation
# time. Write the results to a Dakota results file.
shutil.copy(os.path.join(output_dir, output_file), os.curdir)
Qs = read(output_file)
m_Qs = [np.mean(Qs), np.std(Qs)]
write(sys.argv[2], m_Qs)

