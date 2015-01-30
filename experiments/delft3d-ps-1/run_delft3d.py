#! /usr/bin/env python
# Brokers communication between Delft3D and Dakota through files.
# Mark Piper (mark.piper@colorado.edu)

import sys
import os
import shutil
from subprocess import call


def main():
    '''
    Brokers communication between Delft3D, MATLAB and Dakota through files.
    '''

    # Files and directories.
    start_dir = os.path.dirname(os.path.realpath(__file__))
    initialize_dir = os.path.join(start_dir, 'initialize')
    input_template = 'WLD.sed.template'
    input_file = 'WLD.sed'
    cells_file = 'nesting.txt'
    analysis_program_file = 'total_sed_cal.m'
    analysis_results_file = 'results.out'

    # Copy the contents of the initialize directory into the current
    # run directory. (Don't use shutil.copytree because the
    # destination directory exists.)
    for f in os.listdir(initialize_dir):
        shutil.copy(os.path.join(initialize_dir, f), os.getcwd())

    # Use the parsing utility `dprepro` (from $DAKOTA_DIR/bin) to
    # substitute the parameters from Dakota into the input template,
    # creating a new Delft3D input file.
    shutil.copy(os.path.join(start_dir, input_template), os.getcwd())
    call(['dprepro', sys.argv[1], input_template, input_file])

    # Call Delft3D, using the updated input file.
    call(['qsub', 'run_delft3d_wave.sh'])

    # Call a MATLAB script to read the Delft3D output, calculate the
    # desired responses, and write the Dakota results file.
    shutil.copy(os.path.join(start_dir, cells_file), os.getcwd())
    shutil.copy(os.path.join(start_dir, analysis_program_file), os.getcwd())
    matlab_call = '"' + os.path.splitext(analysis_program_file)[0] + '; exit"'
    call(['matlab', '-nojvm', '-nodisplay', '-nosplash', '-r', matlab_call])
    # shutil.move(analysis_results_file, sys.argv[2])

if __name__ == '__main__':
    main()
