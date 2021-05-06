from flask_restx import Resource

from app.{{package_name}}.controller.{{package_name}} import  {{package_name_class}}Controller
from .dto import {{package_name_class}}Dto

api =  {{package_name_class}}Dto.api

@api.route("/<int:{{package_name}}_id>")
class {{package_name_class}}Ops(Resource):  
    @api.doc(
        "Get a specific  {{package_name_class}} with id",
        responses={
            200: ("{{package_name_class}} data successfully sent", {{package_name_class}}Dto.success_response),
            204: ("{{package_name_class}} not found and no body returned",{{package_name_class}}Dto.success_response),
            404: ("{{package_name_class}} not found with message",{{package_name_class}}Dto.error_response),
        },
    )
  
    def get(self, {{package_name}}_id):
        return {{package_name_class}}Controller.get_{{package_name}}_data({{package_name}}_id)

    @api.doc(
        "Delete a specific {{package_name_class}} with his id",
        responses={
            200: ("{{package_name_class}} data successfully deleted", {{package_name_class}}Dto.success_response),
            404: ("{{package_name_class}} not found with message",{{package_name_class}}Dto.error_response),
        },
    )
    
    def delete(self, {{package_name}}_id):
        return {{package_name_class}}Controller.delete_{{package_name}}_data({{package_name}}_id)




@api.route("/")
class {{package_name_class}}List(Resource):
    @api.doc(
        "Get all {{package_name_class}}",
        responses={
            200: ("{{package_name_class}} found", {{package_name_class}}Dto.success_response),
            404: ("{{package_name_class}} not found",{{package_name_class}}Dto.error_response),
        },
    )
    
    def get(self):
        return {{package_name_class}}Controller.delete_{{package_name}}_data({{package_name}}_id)

