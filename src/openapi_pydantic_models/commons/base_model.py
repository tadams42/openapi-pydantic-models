from typing import Any

from pydantic import BaseModel as PydanticBaseModel

from .utilities import exclude_blanks


class BaseModel(PydanticBaseModel):
    class Config:
        anystr_strip_whitespace = True
        extra = "forbid"
        use_enum_values = True

    def dict(
        self, *, by_alias: bool = True, exclude_none: bool = True, **kwargs
    ) -> dict[str, Any]:
        retv = super().dict(exclude_none=exclude_none, by_alias=by_alias, **kwargs)

        if exclude_none:
            retv = exclude_blanks(retv)

        return retv or dict()
