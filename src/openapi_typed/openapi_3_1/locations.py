import enum


class Locations(str, enum.Enum):
    query = "query"
    header = "header"
    path = "path"
    cookie = "cookie"
