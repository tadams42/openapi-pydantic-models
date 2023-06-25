from .external_documentation_object import ExternalDocumentationObject
from .specification_extensions import SpecificationExtendable


class TagObject(SpecificationExtendable):
    name: str | None = None
    description: str | None = None
    externalDocs: ExternalDocumentationObject | None = None
