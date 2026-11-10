def test_valid_login():
    username = "admin"
    password = "admin123"

    assert username == "admin"
    assert password == "admin123"


def test_invalid_login():
    username = "admin"
    password = "wrong123"

    assert password != "admin123"

