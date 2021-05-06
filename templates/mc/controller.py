from app.{{package_name}}.model.{{package_name}}_model import {{package_name_class}}
from app import db

class {{package_name_class}}Controller:
    @staticmethod
    def get_{{package_name}}_data({{package_name}}_id):
        """Get a specific {{package_name}} with his username
        """
        {{package_name}}_r = {{package_name_class}}.query.filter_by(id={{package_name}}_id).first()
        if {{package_name}}_r:
            
            return {{package_name}}_r
        else:
            return False
    
    @staticmethod
    def delete_{{package_name}}_data({{package_name}}_id):
        """Delete an {{package_name}} with his ID
        """
        try:
            {{package_name_class}}.query.filter_by(id={{package_name}}_id).delete()
            db.session.commit()
            return True
        except Exception as exc:
            return False
        
    @staticmethod
    def get_all_{{package_name}}({{package_name}}_id):
        """Delete an {{package_name}} with his ID
        """
        try:
            return {{package_name_class}}.query.all()
        except Exception as exc:
            return False