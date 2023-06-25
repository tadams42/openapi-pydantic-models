from .components_object import ComponentsObject
from .external_documentation_object import ExternalDocumentationObject
from .info_object import InfoObject
from .path_item_object import PathItemObject
from .paths_object import PathsObject
from .reference_object import ReferenceObject
from .security_requirement_object import SecurityRequirementObject
from .server_object import ServerObject
from .specification_extensions import SpecificationExtendable
from .tag_object import TagObject


class OpenAPIObject(SpecificationExtendable):
    openapi: str = "3.1.0"
    info: InfoObject | None = None
    # jsonSchemaDialect: str = "https://json-schema.org/draft/2020-12/schema"
    jsonSchemaDialect: str = "https://spec.openapis.org/oas/3.1/dialect/base"
    servers: list[ServerObject] | None = None
    paths: PathsObject | None = None
    webhooks: dict[str, ReferenceObject | PathItemObject] | None = None
    components: ComponentsObject | None = None
    security: list[SecurityRequirementObject] | None = None
    tags: list[TagObject] | None = None
    externalDocs: ExternalDocumentationObject | None = None
