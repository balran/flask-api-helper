from jinja2 import Template
import os 


def templating_model(package_name):
    package_name_class = package_name.title()
    print(os.path.join(os.path.abspath(os.getcwd()),"templates","mc","model.py"))
    with open(os.path.join(os.path.abspath(os.getcwd()),"templates","mc","model.py")) as file_:
        template = Template(file_.read())
    msg = template.render(package_name=package_name,package_name_class=package_name_class)
    return msg



def templating_controller(package_name):
    package_name_class = package_name.title()
    print(os.path.join(os.path.abspath(os.getcwd()),"templates","mc","controller.py"))
    with open(os.path.join(os.path.abspath(os.getcwd()),"templates","mc","controller.py")) as file_:
        template = Template(file_.read())
    msg = template.render(package_name=package_name,package_name_class=package_name_class)
    return msg


def templating_dto(package_name):
    package_name_class = package_name.title()
    print(os.path.join(os.path.abspath(os.getcwd()),"templates","api","dto.py"))
    with open(os.path.join(os.path.abspath(os.getcwd()),"templates","api","dto.py")) as file_:
        template = Template(file_.read())
    msg = template.render(package_name=package_name,package_name_class=package_name_class)
    return msg

def templating_routes(package_name):
    package_name_class = package_name.title()
    print(os.path.join(os.path.abspath(os.getcwd()),"templates","api","routes.py"))
    with open(os.path.join(os.path.abspath(os.getcwd()),"templates","api","routes.py")) as file_:
        template = Template(file_.read())
    msg = template.render(package_name=package_name,package_name_class=package_name_class)
    return msg
