# To run tests in verbose mode, run the tests with the -s flag
# To have even more verbosity, run the tests with the -v flag

import pytest

# Here we define fixtures at module level
def setup_module(module):
    print("Creating DB connection")

def teardown_module(module):
    print("Closing DB connection")

# Here we define fixtures at function level
def setup_function(function):
    print("launching browser")

def teardown_function(function):
    print(" closing browser")

def test_do_login():
    print("Executing login test")

def test_do_signin():
    print("Executing Sign-in test")