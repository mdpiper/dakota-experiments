#! /usr/bin/env python
# Brokers communication between Delft3D and Dakota through files.
# Mark Piper (mark.piper@colorado.edu)

import sys
import shutil
from subprocess import call


def main():

    print('In run_delft3d.main()')

    # Files and directories.
    # start_dir = os.path.dirname(os.path.realpath(__file__))
    # input_dir = os.path.join(start_dir, 'HYDRO_IN')
    # if not os.path.exists(input_dir): os.mkdir(input_dir)
    # output_dir = os.path.join(start_dir, 'HYDRO_OUTPUT')
    # if not os.path.exists(output_dir): os.mkdir(output_dir)
    input_template = 'WLD.sed.template'
    input_file = 'WLD.sed'
    # output_file = 'HYDROASCII.QS'

    # Use the parsing utility `dprepro` (from $DAKOTA_DIR/bin) to
    # incorporate the parameters from Dakota into the input
    # template, creating a new Delft3D input file.
    # shutil.copy(os.path.join(start_dir, input_template), os.curdir)
    call(['dprepro', sys.argv[1], input_template, input_file])
    # shutil.copy(input_file, input_dir)

    # Call Delft3D, using the updated input file.
    call(['qsub', 'run_delft3d_wave.sh'])

    # Calculate mean and standard deviation of a HydroTrend output time
    # series for the simulation. Write the output to a Dakota results file.
    # shutil.copy(os.path.join(output_dir, output_file), os.curdir)
    # labels = get_labels(sys.argv[1])
    # series = read(output_file)
    # if series != None:
    #     m_series = [np.mean(series), np.std(series)]
    # else:
    #     m_series = [float('nan'), float('nan')]
    # write_results(sys.argv[2], m_series, labels)
    call(['matlab', '-nojvm', '-nodisplay', '-nosplash', '-r', \
          '"total_sed_cal; exit"'])
    shutil.move('results.out', sys.argv[2])

if __name__ == '__main__':
    main()
