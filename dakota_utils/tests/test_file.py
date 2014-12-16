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

nondir = 'vwbwguv00240cnwuncdsv'
nonfile = nondir + '.pro'
bname = 'delete_me'

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

def test_remove_file_does_not_exist():
    '''
    Tests deleting a nonexistent file with remove_file().
    '''    
    remove_file(os.path.join(os.environ['_test_tmp_dir'], nonfile))

def test_remove_directory_does_not_exist():
    '''
    Tests deleting a nonexistent directory with remove_directory().
    '''    
    remove_directory(os.path.join(os.environ['_test_tmp_dir'], nondir))

def test_remove_does_not_exist():
    '''
    Tests deleting a nonexistent file or directory with remove().
    '''    
    remove(os.path.join(os.environ['_test_tmp_dir'], nonfile))
    remove(os.path.join(os.environ['_test_tmp_dir'], nondir))

def test_remove_file():
    '''
    Tests that remove_file() deletes a file.
    '''    
    fname = os.path.join(os.environ['_test_tmp_dir'], bname)
    touch(fname)
    remove_file(fname)
    assert_false(os.path.exists(fname))

def test_remove_directory():
    '''
    Tests that remove_directory() deletes a directory.
    '''    
    dname = os.path.join(os.environ['_test_tmp_dir'], bname)
    os.mkdir(dname)
    remove_directory(dname)
    assert_false(os.path.exists(dname))

def test_remove_a_file():
    '''
    Tests that remove() deletes a file. (Uses touch)
    '''
    fname = os.path.join(os.environ['_test_tmp_dir'], bname)
    touch(fname)
    remove(fname)
    assert_false(os.path.exists(fname))

def test_remove_a_directory():
    '''
    Tests that remove() deletes a directory.
    '''    
    dname = os.path.join(os.environ['_test_tmp_dir'], bname)
    os.mkdir(dname)
    remove(dname)
    assert_false(os.path.exists(dname))

def test_touch():
    '''
    Tests that touch() makes a file. (Uses remove)
    '''
    fname = os.path.join(os.environ['_test_tmp_dir'], 'a_file')
    touch(fname)
    assert_true(os.path.exists(fname))
    remove(fname)
