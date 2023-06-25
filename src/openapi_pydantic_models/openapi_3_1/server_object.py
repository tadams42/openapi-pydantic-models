from __future__ import annotations

from .server_variable_object import ServerVariableObject
from .specification_extensions import SpecificationExtendable


class ServerObject(SpecificationExtendable):
    url: str | None = None
    description: str | None = None
    variables: dict[str, ServerVariableObject] | None = None
