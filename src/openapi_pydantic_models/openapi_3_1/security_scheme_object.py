import enum

from pydantic import Field

from .oauth_flows_object import OAuthFlowsObject
from .specification_extensions import SpecificationExtendable


class SecuritySchemeTypes(str, enum.Enum):
    apiKey = "apiKey"
    http = "http"
    mutualTLS = "mutualTLS"
    oauth2 = "oauth2"
    openIdConnect = "openIdConnect"


class SecuritySchemeLocations(str, enum.Enum):
    query = "query"
    header = "header"
    cookie = "cookie"


class SecuritySchemeObject(SpecificationExtendable):
    type_: SecuritySchemeTypes | None = Field(default=None, alias="type")
    description: str | None = None
    name: str | None = None
    in_: SecuritySchemeLocations | None = Field(default=None, alias="in")
    scheme_: str | None = Field(default=None, alias="scheme")
    bearerFormat: str | None = None
    flows: OAuthFlowsObject | None = None
    openIdConnectUrl: str | None = None
