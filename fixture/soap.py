from suds.client import Client
from suds import WebFault
from model.project import Project

class SoapHelper:

    def __init__(self,app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost:8080/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return  False

    def get_user_projects(self):
        client = Client(self.app.config['soap']['url'])
        try:
            return [Project(project.id, project.name, project.description)
                    for project in client.service.mc_projects_get_user_accessible(self.app.config['webadmin']['user'], self.app.config['webadmin']['password'])]
            # response = list(client.service.mc_projects_get_user_accessible(self.app.config['webadmin']['user'], self.app.config['webadmin']['password']))
            # return response
        except WebFault:
            return False

    def add_projects(self, username, password, pr):
        client = Client("http://localhost:8080/mantisbt-2.15.0/api/soap/mantisconnect.php?wsdl")
        project = client.factory.create('ProjectData')
        project.name = pr.name
        project.description = pr.description
        client.service.mc_project_add(username, password, project)

    def del_projects(self, username, password, project_id):
        client = Client("http://localhost:8080/mantisbt-2.15.0/api/soap/mantisconnect.php?wsdl")
        client.service.mc_project_delete(username, password, project_id)
