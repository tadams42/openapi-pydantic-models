from .specification_extensions import SpecificationExtendable


class ContactObject(SpecificationExtendable):
    name: str | None = None
    url: str | None = None
    email: str | None = None
