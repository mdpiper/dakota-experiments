#! /usr/bin/env python
#
# Tests for dakota_utils.file.
#
# Call with:
#   $ nosetests -sv
#
# Mark Piper (mark.piper@colorado.edu)

from nose.tools import *
import os
import tempfile
import shutil
from dakota_utils.file import *

def setup_module():
    print('File tests:')
    os.environ['_test_tmp_dir'] = tempfile.mkdtemp()

def teardown_module():
    shutil.rmtree(os.environ['_test_tmp_dir'])

@raises(TypeError)
def test_remove_zero_arguments():
    '''
    Tests for no input parameter to remove().
    '''
    remove()

@raises(TypeError)
def test_remove_file_zero_arguments():
    '''
    Tests for no input parameter to remove_file().
    '''
    remove_file()

@raises(TypeError)
def test_remove_directory_zero_arguments():
    '''
    Tests for no input parameter to remove_directory().
    '''
    remove_directory()

@raises(TypeError)
def test_touch_zero_arguments():
    '''
    Tests for no input parameter to touch().
    '''
    touch()

