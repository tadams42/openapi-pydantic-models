from __future__ import annotations

from pydantic import Field
from ..commons import BaseModel


class ReferenceObject(BaseModel):
    ref: str | None = Field(default=None, alias="$ref")
    summary: str | None = None
    description: str | None = None
