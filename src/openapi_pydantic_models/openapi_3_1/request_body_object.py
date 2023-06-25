from .media_type_object import MediaTypeObject
from .specification_extensions import SpecificationExtendable


class RequestBodyObject(SpecificationExtendable):
    description: str | None = None
    content: dict[str, MediaTypeObject] | None = None
    required: bool | None = None
