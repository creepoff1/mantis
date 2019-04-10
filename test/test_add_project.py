from testdata.projects import Project
import random, string



def test_create_new_project(app):
    app.session.login("administrator", "root")
    old_projects = app.soap.get_user_projects()
    app.project.create_new_project(Project(name = randomword(), description="description1"))
    new_projects = app.soap.get_user_projects()
    assert len(new_projects) == len(old_projects)+1






def randomword():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))