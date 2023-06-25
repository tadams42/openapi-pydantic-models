from .specification_extensions import SpecificationExtendable


class OAuthFlowObject(SpecificationExtendable):
    authorizationUrl: str | None = None
    tokenUrl: str | None = None
    refreshUrl: str | None = None
    scopes: dict[str, str] | None = None
