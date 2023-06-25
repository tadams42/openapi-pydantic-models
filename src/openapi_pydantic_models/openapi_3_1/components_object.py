from .callback_object import CallbackObject
from .example_object import ExampleObject
from .header_object import HeaderObject
from .link_object import LinkObject
from .parameter_object import ParameterObject
from .path_item_object import PathItemObject
from .reference_object import ReferenceObject
from .request_body_object import RequestBodyObject
from .response_object import ResponseObject
from .schema_object import SchemaObject
from .security_scheme_object import SecuritySchemeObject
from .specification_extensions import SpecificationExtendable


class ComponentsObject(SpecificationExtendable):
    schemas: dict[str, SchemaObject] | None = None
    responses: dict[str, ResponseObject | ReferenceObject] | None = None
    parameters: dict[str, ParameterObject | ReferenceObject] | None = None
    examples: dict[str, ExampleObject | ReferenceObject] | None = None
    requestBodies: dict[str, RequestBodyObject | ReferenceObject] | None = None
    headers: dict[str, HeaderObject | ReferenceObject] | None = None
    securitySchemes: dict[str, SecuritySchemeObject | ReferenceObject] | None = None
    links: dict[str, LinkObject | ReferenceObject] | None = None
    callbacks: dict[str, CallbackObject | ReferenceObject] | None = None
    pathItems: dict[str, PathItemObject | ReferenceObject] | None = None
