#! /usr/bin/env python
#
# Dakota utility programs for converting output.
#
# Mark Piper (mark.piper@colorado.edu)

import shutil
from subprocess import check_call, CalledProcessError


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
