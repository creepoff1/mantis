from model.project import Project
import random, string
from random import randrange


def test_delete_project (app):
    if not app.session.is_logged_in():
        app.session.login("administrator", "root")
    if len(app.soap.get_user_projects()) == 0:
        app.project.create_new_project(Project(name=randomword(), description="description1"))
    old_list = app.soap.get_user_projects()
    index = randrange (len(old_list))
    app.project.delete_project(old_list[index].name)
    new_list = app.soap.get_user_projects()
    assert len(old_list) - 1 == len(new_list)


def randomword():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))


