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

@raises(TypeError)
def test_load_series_no_input():
    '''
    Tests for no input parameter to load_series().
    '''
    load_series()

def test_load_series_file_does_not_exist():
    '''
    Tests for nonexistent input to load_series().
    '''
    r = load_series(nonfile)
    assert_is_none(r)
