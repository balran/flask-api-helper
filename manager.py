import os
from os import path
from templating import templating_model, templating_controller, templating_dto, templating_routes
CURRENT_PATH = os.path.abspath(os.getcwd())
PARENT_PATH = os.path.abspath(os.path.join(CURRENT_PATH, os.pardir))
PROJECT_NAME = os.path.join('flask-api-boilerplate-main copy','app')
PROJECT_PATH = os.path.join(PARENT_PATH, PROJECT_NAME)
#PROJECT_PATH = os.path.join()

PROTECTED_KEYWORD = ["test", "lib", "os"]

def main(package_name):
    package_name = package_name.lower()
    full_path = os.path.join(PROJECT_PATH, package_name)
    if not check_name_is_available(full_path, package_name):
        print("Creating Controller and Model for {}".format(package_name))
        create_ctrl_model(full_path, package_name)
        create_api_ressource(PROJECT_PATH, package_name)
    else:
        print("impossible to create Controller and Model for {}".format(package_name))

def check_name_is_available(fully_path, package_name):
    """Check if folder already exist
    
        Args : package_name(str) : package name for the new endpoint
               fully_path(str) : full path with the package name
    """
    if package_name not in PROTECTED_KEYWORD:
        return path.exists(fully_path)  
    else: 
        return False

def create_ctrl_model(fully_path,package_name):
    """Create the controller and the model for new service endpoint
    
        Args : package_name(str) : package name for the new endpoint
               fully_path(str) : full path with the package name
    """

    os.mkdir(fully_path)
    try:
        pass
        os.mkdir(os.path.join(fully_path,"controller"))
        os.mkdir(os.path.join(fully_path,"model"))

        a = open(os.path.join(fully_path,"controller",package_name+".py"), "w")
        b = open(os.path.join(fully_path,"model",package_name+"_model.py"), "w")
        
        a.write(templating_controller(package_name))
        a.close()
        
        b.write(templating_model(package_name))
        b.close()
    except OSError as errorOS:
        print ("Creation of the directory %s failed %s" % fully_path, errorOS)
    else:
        print ("Successfully created the directory %s " % fully_path)

def create_api_ressource(fully_path, package_name):
    """Create the endpoint and the dto of the new package
    
        Args : package_name(str) : package name for the new endpoint
               fully_path(str) : full path with the package name
    """
    api_path = os.path.join(fully_path, "api")
    api_final_directory = os.path.join(api_path, package_name)
    dto_file = os.path.join(api_final_directory,"dto.py")
    routes_file = os.path.join(api_final_directory,"routes.py")
    try: 
        os.makedirs(api_final_directory)
       
        a = open(dto_file, "w")
        b = open(routes_file, "w")
        
        a.write(templating_dto(package_name))
        a.close()
        
        b.write(templating_routes(package_name))
        b.close()
    except OSError as errorOS:
        print ("Creation of the directory %s failed %s" % fully_path, errorOS)
    else:
        print ("Successfully created the directory %s " % fully_path)

if __name__ == '__main__':
   
    main("tested")
    