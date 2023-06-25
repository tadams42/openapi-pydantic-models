from .header_object import HeaderObject
from .link_object import LinkObject
from .media_type_object import MediaTypeObject
from .reference_object import ReferenceObject
from .specification_extensions import SpecificationExtendable


class ResponseObject(SpecificationExtendable):
    description: str | None = None
    headers: dict[str, HeaderObject | ReferenceObject] | None = None
    content: dict[str, MediaTypeObject] | None = None
    links: dict[str, LinkObject | ReferenceObject] | None = None
