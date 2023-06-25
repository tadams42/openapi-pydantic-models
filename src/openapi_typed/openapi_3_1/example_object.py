from __future__ import annotations

from typing import Any

from .specification_extensions import SpecificationExtendable


class ExampleObject(SpecificationExtendable):
    summary: str | None = None
    description: str | None = None
    value: Any = None
    externalValue: str | None = None
