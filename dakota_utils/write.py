#! /usr/bin/env python
#
# Dakota utility programs for writing output.
#
# Mark Piper (mark.piper@colorado.edu)

import shutil
from subprocess import check_call, CalledProcessError

def write_results(results_file, array, labels):
    '''
    Writes a Dakota results file from an input array.
    '''
    try:
        fp = open(results_file, 'w')
        for i in range(len(array)):
            fp.write(str(array[i]) + '\t' + labels[i] + '\n')
    except IOError:
        raise
    finally:
        fp.close()


def strip_interface_column(tab_file):
    '''
    Strips the 'interface' column from a Dakota 6.1 tabular output file.
    '''
    try:
        bak_file = tab_file + '.orig'
        shutil.copyfile(tab_file, bak_file)
        cmd = 'cat ' + bak_file +' | colrm 9 18 > ' + tab_file
        check_call(cmd, shell=True)
    except (IOError, CalledProcessError):
        raise
