#! /usr/bin/python

from nose.tools import *
import os
import tempfile
import shutil
from utils.dakota_utils.run import *

def setup_module():
    os.environ['_test_tmp_dir'] = tempfile.mkdtemp()

def teardown_module():
    shutil.rmtree(os.environ['_test_tmp_dir'])

@raises(TypeError)
def test_no_experiment():
    '''
    Tests for no input parameter.
    '''
    run_experiment()

def test_no_experiment_content():
    err_str = 'Error: DAKOTA input file not found.'
    r = run_experiment(os.environ['_test_tmp_dir'])
    assert_equal(r, err_str)

def test_no_input_file():
    r = get_input_file(os.environ['_test_tmp_dir'])
    assert_is_none(r)
