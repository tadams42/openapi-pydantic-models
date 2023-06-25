from .specification_extensions import SpecificationExtendable


class LicenseObject(SpecificationExtendable):
    name: str | None = None
    identifier: str | None = None
    url: str | None = None
