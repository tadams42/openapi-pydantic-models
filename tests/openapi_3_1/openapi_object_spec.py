from openapi_typed import OpenAPIObject


class DescribeOpenAPIObject:
    def it_loads_openapi_specification_data(self, petstore_extended):
        exception = False

        try:
            obj = OpenAPIObject.parse_obj(petstore_extended)

        except Exception:
            exception = True

        assert (
            not exception
        ), "Failed to load OpenAPI specification from petstore_extended.yaml"

        assert (
            obj.paths is not None
        ), "Failed to load OpenAPI specification from petstore_extended.yaml"
