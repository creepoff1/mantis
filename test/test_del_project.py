from model.project import Project
import random, string
from random import randrange


def test_delete_project (app):
    user_config = app.config['webadmin']
    if not app.session.is_logged_in():
        app.session.login(user_config['username'], user_config['password'])
    if len(app.soap.get_user_projects(user_config['user'], user_config['password'])) == 0:
        app.project.create_new_project(Project(name=randomword(), description="description1"))
    old_list = app.soap.get_user_projects(user_config['user'], user_config['password'])
    index = randrange (len(old_list))
    app.project.delete_project(old_list[index].name)
    new_list = app.soap.get_user_projects(user_config['user'], user_config['password'])
    assert len(old_list) - 1 == len(new_list)


def randomword():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))


