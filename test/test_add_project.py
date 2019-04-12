from testdata.projects import Project
import random, string


def test_create_new_project(app):
    app.session.login("administrator", "root")

    old_projects = sorted(app.soap.get_user_projects(), key=Project.id_or_max)
    project = Project(name = randomword(), description="description1")
    app.project.create_new_project(project)
    new_projects = sorted(app.soap.get_user_projects(), key=Project.id_or_max)
    assert len(new_projects) == len(old_projects)+1
    old_projects.append(new_projects[len(new_projects)-1])

    for x in range(len(new_projects)):
        assert old_projects[x].id == new_projects[x].id
        assert old_projects[x].name == new_projects[x].name
        assert old_projects[x].description == new_projects[x].description




def randomword():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))