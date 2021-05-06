from flask_restx import Namespace, fields


class {{package_name_class}}Dto:
    """DTO for Data Transfert Object will represent data validation.
    """
    api = Namespace("{{package_name}}", description=" {{package_name_class}} related operations.")
    {{package_name}} = api.model(
        "{{package_name}} object",
        {
            
        },
    )

    success_response = api.model(
        "Data Response",
        {
            
        },
    )
    
    error_response = api.model(
        "Data Response not found",
        {
            
        },
    )
