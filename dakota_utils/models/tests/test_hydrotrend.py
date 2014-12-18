#!/usr/bin/env python
#
# Tests for dakota_utils.models.hydrotrend.
#
# Call with:
#   $ nosetests -sv
#
# Mark Piper (mark.piper@colorado.edu)

from nose.tools import *
import os
import tempfile
import shutil
from dakota_utils.models.hydrotrend import *

nonfile = 'wvwbfb9vwvfnv.f'

def setup_module():
    print('HydroTrend tests:')
    os.environ['_test_tmp_dir'] = tempfile.mkdtemp()

def teardown_module():
    shutil.rmtree(os.environ['_test_tmp_dir'])

# @raises(TypeError)
# def test_load_no_arguments():
#     '''
#     Tests for no arguments to load().
#     '''
#     load()

# def test_load_file_does_not_exist():
#     '''
#     Tests for nonexistent input to load().
#     '''
#     r = load(nonfile)
#     assert_is_none(r)

# @raises(TypeError)
# def test_call_no_arguments():
#     '''
#     Tests for no arguments to call().
#     '''
#     call()


