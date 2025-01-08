# Install pyetst soft assertions with the following command:
# pip install pytest-soft-assertions
# The run the tests with the --soft-asserts flag

# Example

#

import pytest

def test_validate_titles():
    expected_title = "Google.com"
    actual_title = "Gmail.com"
    title = "This is a Gmail website"

    # Here it is how we use assertions in Pytest which compare two variables and define
    # a custom error message
    assert expected_title == actual_title, "Titles are not matching"

    # Here it is how we use assertions in Pytest which check the presence of a string
    # in a variable and define a custom error message
    assert "Gmails" in title, "Gmail does not exist in the title"

    # Here is is how we make an assertion based on a specific condition
    assert False, "Forcefully failing the test"