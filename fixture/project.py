from model.project import Project
import time


class ProjectHelper:

    def __init__(self, app):
        self.app = app


    def go_to_create_project_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()

    def go_to_project_list_page(self):
        wd = self.app.wd
        wd.get("http://localhost:8080/mantisbt-1.2.20/manage_proj_page.php")

    def go_back_to_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span/a").click()

    def fill_project_fields(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.name)
        self.change_field_value("description", project.description)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def create_new_project(self, project):
        wd = self.app.wd
        self.go_to_project_list_page()
        self.go_to_create_project_page()
        self.fill_project_fields(project)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        self.go_back_to_projects_page()

    def get_project_list(self):
        wd = self.app.wd
        self.go_to_project_list_page()
        self.project_cache = []
        for element in (wd.find_elements_by_xpath("(//tr[@class = 'row-category'])[1]/following-sibling::tr")):
            cells = element.find_elements_by_tag_name('td')
            name = cells[0].text
            description = cells[4].text
            self.project_cache.append(Project(name = name, description = description))
        return list(self.project_cache)

    def delete_project(self, name):
        wd = self.app.wd
        self.go_to_project_list_page()
        wd.find_element_by_xpath("//a[contains(text(), '%s')]" % name).click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()



