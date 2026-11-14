sumanth@Sumanths-MacBook-Air qa-git-practice-clone % cat test_login.py
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

def test_locked_account():
    username = "locked_user"

    assert username == "locked_user"


def test_login_with_empty_password():
    username = "admin"
    password = ""

    assert username == "admin"
    assert password != ""
sumanth@Sumanths-MacBook-Air qa-git-practice-clone %     username = "admin"
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

def test_locked_account():
    username = "locked_user"

    assert username == "locked_user"


def test_login_with_empty_password():
    username = "admin"
    password = ""

    assert username == "admin"
    assert password != ""
