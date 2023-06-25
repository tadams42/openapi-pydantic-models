from __future__ import annotations

from typing import TYPE_CHECKING, Any

from pydantic import Field

from .example_object import ExampleObject
from .reference_object import ReferenceObject
from .schema_object import SchemaObject
from .specification_extensions import SpecificationExtendable

if TYPE_CHECKING:
    from .encoding_object import EncodingObject


class MediaTypeObject(SpecificationExtendable):
    schema_: SchemaObject | None = Field(default=None, alias="schema")
    example: Any = None
    examples: dict[str, ExampleObject | ReferenceObject] | None = None
    encoding: dict[str, EncodingObject] | None = None
