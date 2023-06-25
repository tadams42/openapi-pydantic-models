from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .reference_object import ReferenceObject
from .specification_extensions import SpecificationExtendable
from .styles import Styles

if TYPE_CHECKING:
    from .header_object import HeaderObject


class EncodingObject(SpecificationExtendable):
    contentType: str | None = None
    headers: dict[str, HeaderObject | ReferenceObject] | None = None
    style: Styles | None = None
    explode: bool | None = None
    allowReserved: bool | None = None
