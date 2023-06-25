from .specification_extensions import SpecificationExtendable


class ExternalDocumentationObject(SpecificationExtendable):
    description: str | None = None
    url: str | None = None
