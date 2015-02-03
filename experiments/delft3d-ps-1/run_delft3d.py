#! /usr/bin/env python
# Brokers communication between Delft3D and Dakota through files.
# Mark Piper (mark.piper@colorado.edu)

import sys
import os
import shutil
from subprocess import call, check_output
import time

def job_is_running(job_id):
    '''
    Returns True if the PBS job with the given id is running.
    '''
    return call(['qstat', job_id]) == 0

def main():
    '''
    Brokers communication between Delft3D, MATLAB and Dakota through files.
    '''

    # Files and directories.
    start_dir = os.path.dirname(os.path.realpath(__file__))
    initialize_dir = os.path.join(start_dir, 'initialize')
    input_template = 'WLD.sed.template'
    input_file = 'WLD.sed'
    output_file = 'trim-WLD.dat'
    cells_file = 'nesting.txt'
    analysis_program = 'total_sed_cal'
    analysis_program_file = analysis_program + '.m'
    analysis_results_file = analysis_program + '.out'

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

    # Call Delft3D, using the updated input file. Note that `qsub`
    # returns immediately with the PBS job id.
    r = check_output(['qsub', 'run_delft3d_wave.sh'])
    job_id = r.rstrip('\n')

    # Poll the Delft3D job every 10 min. Proceed when it's finished.
    while job_is_running(job_id):
        time.sleep(600)

    # Call a MATLAB script to read the Delft3D output, calculate the
    # desired responses, and write the Dakota results file.
    shutil.copy(os.path.join(start_dir, cells_file), os.getcwd())
    shutil.copy(os.path.join(start_dir, analysis_program_file), os.getcwd())
    print('Current directory: ' + os.getcwd())
    matlab_call = '-r "' + analysis_program + '; exit"'
    r = call(['matlab', '-nodisplay', '-nosplash', matlab_call])
    print('MATLAB exit status code = ' + str(r))
    shutil.move(analysis_results_file, sys.argv[2])

if __name__ == '__main__':
    main()
