from __future__ import annotations

from .specification_extensions import SpecificationExtendable


class ServerVariableObject(SpecificationExtendable):
    enum: list[str] | None = None
    default: str | None = None
    description: str | None = None
