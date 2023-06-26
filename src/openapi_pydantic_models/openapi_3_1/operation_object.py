from __future__ import annotations

from typing import TYPE_CHECKING

from .external_documentation_object import ExternalDocumentationObject
from .parameter_object import ParameterObject
from .reference_object import ReferenceObject
from .request_body_object import RequestBodyObject
from .responses_object import ResponsesObject
from .security_requirement_object import SecurityRequirementObject
from .server_object import ServerObject
from .specification_extensions import SpecificationExtendable

if TYPE_CHECKING:
    from .callback_object import CallbackObject


class OperationObject(SpecificationExtendable):
    tags: list[str] | None = None
    summary: str | None = None
    description: str | None = None
    externalDocs: ExternalDocumentationObject | None = None
    operationId: str | None = None
    parameters: list[ParameterObject | ReferenceObject] | None = None
    requestBody: RequestBodyObject | ReferenceObject | None = None
    responses: ResponsesObject | None = None
    callbacks: dict[str, CallbackObject | ReferenceObject] | None = None
    deprecated: bool | None = None
    security: list[SecurityRequirementObject] | None = None
    servers: list[ServerObject] | None = None
