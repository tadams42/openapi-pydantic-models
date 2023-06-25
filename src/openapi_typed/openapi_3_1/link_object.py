from typing import Any

from .server_object import ServerObject
from .specification_extensions import SpecificationExtendable


class LinkObject(SpecificationExtendable):
    operationRef: str | None = None
    operationId: str | None = None
    parameters: dict[str, Any] | None = None
    requestBody: Any | None = None
    description: str | None = None
    server: ServerObject | None = None
