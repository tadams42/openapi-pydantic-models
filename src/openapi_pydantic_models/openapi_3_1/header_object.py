from __future__ import annotations

from typing import Any

from pydantic import Field

from .example_object import ExampleObject
from .media_type_object import MediaTypeObject
from .reference_object import ReferenceObject
from .schema_object import SchemaObject
from .specification_extensions import SpecificationExtendable
from .styles import Styles


class HeaderObject(SpecificationExtendable):
    description: str | None = None
    required: bool | None = None
    deprecated: bool | None = None
    allowEmptyValue: bool | None = None
    style: Styles | None = None
    explode: bool | None = None
    allowReserved: bool | None = None
    schema_: SchemaObject | None = Field(default=None, alias="schema")
    example: Any = None
    examples: dict[str, ExampleObject | ReferenceObject] | None = None
    content: dict[str, MediaTypeObject] | None = None
