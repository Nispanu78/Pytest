# To run a specific test use markers by relying on the -k flag followed by the name of the test

import pytest

def test_login():
    print("Executing login test")

def test_user_reg():
    print("Executing user registration test")

def test_compose_email():
    print("Executing compose email test")