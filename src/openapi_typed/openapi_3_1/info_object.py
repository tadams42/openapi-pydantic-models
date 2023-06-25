from __future__ import annotations

from .contact_object import ContactObject
from .license_object import LicenseObject
from .specification_extensions import SpecificationExtendable


class InfoObject(SpecificationExtendable):
    title: str | None = None
    summary: str | None = None
    description: str | None = None
    termsOfService: str | None = None
    contact: ContactObject | None = None
    license: LicenseObject | None = None
    version: str | None = None
