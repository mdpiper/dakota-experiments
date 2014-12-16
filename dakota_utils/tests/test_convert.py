#!/usr/bin/env python
#
# Tests for dakota_utils.convert.
#
# Call with:
#   $ nosetests -sv
#
# Mark Piper (mark.piper@colorado.edu)

from nose.tools import *
import os
import tempfile
import shutil
from dakota_utils.convert import *

nonfile = 'fbwiBVBVFVBvVB.txt'

def setup_module():
    print('Convert tests:')
    os.environ['_test_tmp_dir'] = tempfile.mkdtemp()

def teardown_module():
    shutil.rmtree(os.environ['_test_tmp_dir'])

@raises(TypeError)
def test_strip_interface_column_no_input():
    '''
    Tests for no input parameter to strip_interface_column().
    '''
    strip_interface_column()

@raises(IOError)
def test_strip_interface_column_file_does_not_exist():
    '''
    Tests for nonexistent input to strip_interface_column().
    '''
    strip_interface_column(nonfile)
