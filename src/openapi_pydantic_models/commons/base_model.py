from typing import Any

from pydantic import BaseModel as PydanticBaseModel
from pydantic import ConfigDict

from .utilities import exclude_blanks


class BaseModel(PydanticBaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        str_strip_whitespace=True,
        extra="forbid",
        use_enum_values=True,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def model_dump(
        self, *, by_alias: bool = True, exclude_none: bool = True, **kwargs
    ) -> dict[str, Any]:
        retv = (
            super().model_dump(by_alias=by_alias, exclude_none=exclude_none, **kwargs)
            or dict()
        )

        if exclude_none:
            retv = exclude_blanks(retv)

        return retv or dict()
