from __future__ import annotations

from pydantic import Field

from .operation_object import OperationObject
from .parameter_object import ParameterObject
from .reference_object import ReferenceObject
from .server_object import ServerObject
from .specification_extensions import SpecificationExtendable


class PathItemObject(SpecificationExtendable):
    ref: str | None = Field(default=None, alias="$ref")
    summary: str | None = None
    description: str | None = None
    get: OperationObject | None = None
    put: OperationObject | None = None
    post: OperationObject | None = None
    delete_: OperationObject | None = Field(default=None, alias="delete")
    options: OperationObject | None = None
    head: OperationObject | None = None
    patch: OperationObject | None = None
    trace: OperationObject | None = None
    servers: list[ServerObject] | None = None
    parameters: list[ParameterObject | ReferenceObject] | None = None
