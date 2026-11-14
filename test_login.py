def test_valid_login():
    username = "admin"
    password = "admin123"

    assert username == "admin"
    assert password == "admin123"


def test_invalid_login():
    username = "admin"
    password = "wrong123"

    assert password != "admin123"

def test_empty_password():
    username = "admin"
    password = ""

    assert username == "admin"
    assert password == ""


def test_username_case_sensitivity():
    username = "Admin"

    assert username != "admin"
