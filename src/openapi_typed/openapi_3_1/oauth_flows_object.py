from .oauth_flow_object import OAuthFlowObject
from .specification_extensions import SpecificationExtendable


class OAuthFlowsObject(SpecificationExtendable):
    implicit: OAuthFlowObject | None = None
    password: OAuthFlowObject | None = None
    clientCredentials: OAuthFlowObject | None = None
    authorizationCode: OAuthFlowObject | None = None
