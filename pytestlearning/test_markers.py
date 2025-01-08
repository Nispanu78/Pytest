# To use markers, use -m followed by the marker name

# Example:

# pytest test_markers.py -s -v -m functional

import pytest

@pytest.mark.functional
def test_login():
    print("Executing login test")

@pytest.mark.regression
def test_user_reg():
    print("Executing user registration test")

@pytest.mark.functional
def test_compose_email():
    print("Executing compose email test")

# By adding this marker, the test is skipped
@pytest.mark.skip
def test_skip():
    print("skipping test")