#! /usr/bin/env python
# Brokers communication between Delft3D and Dakota through files.
# Mark Piper (mark.piper@colorado.edu)

import sys
import os
import shutil
from subprocess import call

def main():
    '''
    Brokers communication between Delft3D and Dakota through files.
    '''
    start_dir = os.path.dirname(os.path.realpath(__file__))
    initialize_dir = os.path.join(start_dir, 'initialize')
    input_template = 'WLD.sed.template'
    input_file = 'WLD.sed'
    fake_file = 'fake.out'
    real_file = 'results.out'

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

    # file Delft3D, using the updated input file. Note that `qsub`
    # returns immediately with the PBS job id.
    job_name = 'D3D-Dakota' + os.path.splitext(os.getcwd())[1]
    wall_time = 'walltime=96:00:00'
    priority = '-50'
    call(['qsub', '-N', job_name, '-l', wall_time, '-p', priority, \
              'run_delft3d_wave.sh'])

    # Copy in a dummy results file to advance Dakota.
    shutil.copy(os.path.join(start_dir, fake_file), real_file)

if __name__ == '__main__':
    main()
