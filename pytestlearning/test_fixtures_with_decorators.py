# To run tests in verbose mode, run the tests with the -s flag
# To have even more verbosity, run the tests with the -v flag

import pytest

# Here we define decorators and import the fixtures present in test_fixtures.py file

@pytest.fixture(scope="module")
def fixture_at_module_level():
    print("Creating DB connection")
    # Here "yield" will act as a teardown
    yield
    print("Closing DB connection")

@pytest.fixture(scope="function")
def fixture_at_function_level():
    print("Launching browser")

    yield
    print(" Closing browser")

# # Here we call the fixture_at_function_level fixture which is implemented at function level
# def test_do_login(fixture_at_function_level):
#     print("Executing login test")
#
# def test_do_signin(fixture_at_function_level):
#     print("Executing Sign-in test")
#
# # Here we call the fixture_at_module_level fixture which is implemented at module level
# def test_do_another_login(fixture_at_module_level):
#     print("Executing login test")
#
# def test_do_another_signin(fixture_at_module_level):
#     print("Executing Sign-in test")

# Here we call the fixture_at_module_level and fixture_at_function_level fixtures in the same function parameter
# def test_do_another_login(fixture_at_module_level, fixture_at_function_level):
#     print("Executing login test")
#
#
# def test_do_another_signin(fixture_at_module_level, fixture_at_function_level):
#     print("Executing Sign-in test")

# Still another way is to use pytest.mark.usefixtures
@pytest.mark.usefixtures("fixture_at_module_level", "fixture_at_function_level")
def test_do_another_login():
    print("Executing login test")

# @pytest.mark.usefixtures("fixture_at_module_level", "fixture_at_function_level")
# def test_do_another_signin():
#     print("Executing Sign-in test")