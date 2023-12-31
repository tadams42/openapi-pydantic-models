from openapi_pydantic_models import OpenAPIObject


class DescribeOpenAPIObject:
    def it_loads_openapi_specification_data(self, petstore_extended):
        exception = False

        try:
            obj = OpenAPIObject.model_validate(petstore_extended)

        except Exception:
            exception = True

        assert (
            not exception
        ), "Failed to load OpenAPI specification from petstore_extended.yaml"

        assert (
            obj.paths is not None
        ), "Failed to load OpenAPI specification from petstore_extended.yaml"
