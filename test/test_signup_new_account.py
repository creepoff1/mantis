import string
import random

def random_username():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))


def test_signup_new_account(app):
    username = random_username()
    email = username + "@localhost"
    password = "test"
    app.james.ensure_user_exists(username, password)
    app.signup.new_user(username, email, password)
    assert app.soap.can_login(username, password)
