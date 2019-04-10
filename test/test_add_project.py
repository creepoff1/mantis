from testdata.projects import Project
import random, string



def test_create_new_project(app):
    user_config = app.config['webadmin']
    app.session.login(user_config['user'], user_config['password'])
    # if len(app.project.get_project_list()) == 0:
    #     app.project.create_new_project(Project(name = randomword(), description="description1"))
    old_projects = app.soap.get_user_projects(user_config['user'], user_config['password'])
    app.project.create_new_project(Project(name = randomword(), description="description1"))
    new_projects = app.soap.get_user_projects(user_config['user'], user_config['password'])
    assert len(new_projects) == len(old_projects)+1






def randomword():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))