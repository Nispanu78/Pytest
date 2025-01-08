# It is better to run the test with the -v flag in order to check that the script has
# tested all parameters

import pytest

def get_data():
    return [("test@mail.com", "testpassword1"), ("test2@mail.com", "testpassword2"),
            ("test3@mail.com", "testpassword3")]

# Here we define a parametrized marker
@pytest.mark.parametrize("username, password", get_data())
def test_do_login(username, password):
    print(username, "---", password)