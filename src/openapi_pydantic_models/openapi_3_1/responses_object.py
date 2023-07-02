from __future__ import annotations

import itertools
from collections.abc import MutableMapping
from typing import Any, Iterator

from pydantic import PrivateAttr, Field, model_serializer

from ..commons import BaseModel, exclude_blanks
from .reference_object import ReferenceObject
from .response_object import ResponseObject
from .specification_extensions import ExtensionsStorage


class ResponsesObject(BaseModel, MutableMapping[str, ResponseObject | ReferenceObject]):
    """
    Model for OpenAPI ResponsesObject. This object is mapping of HTTP status codes
    with responses.

    This object MAY be extended with with [4.9 Specification
    Extensions](https://spec.openapis.org/oas/v3.1.0#specificationExtensions).
    """

    default_: ResponseObject | ReferenceObject | None = Field(
        default=None, alias="default"
    )
    _data: dict[str, ResponseObject | ReferenceObject] = PrivateAttr(
        default_factory=dict
    )
    _ext: ExtensionsStorage = PrivateAttr(default_factory=ExtensionsStorage)

    def __init__(self, **kwargs):
        super().__init__(**{k: v for k, v in kwargs.items() if k == "default"})
        raw_data = dict(**{k: v for k, v in kwargs.items() if k != "default"})
        self._ext = ExtensionsStorage(raw_data)
        for k, v in raw_data.items():
            if not ExtensionsStorage.is_key(str(k)):
                self.__setitem__(k, v)

    @property
    def extensions(self) -> ExtensionsStorage:
        return self._ext

    def __getitem__(self, key: str):
        if ExtensionsStorage.is_key(str(key)):
            raise KeyError(f'Extensions must be accessed via self.extensions["{key}"]!')

        try:
            return self._data.__getitem__(key)
        except KeyError:
            raise KeyError(key)

    def __setitem__(self, key: str, value):
        if ExtensionsStorage.is_key(str(key)):
            raise KeyError(f'Extensions must be accessed via self.extensions["{key}"]!')

        v = None
        for typ in [ReferenceObject, ResponseObject]:
            if v is None:
                try:
                    v = typ.model_validate(value)
                except Exception:
                    pass
        if v is None:
            raise ValueError(v)

        self._data.__setitem__(str(key), v)

    def __delitem__(self, key: str):
        if ExtensionsStorage.is_key(str(key)):
            raise KeyError(f'Extensions must be accessed via self.extensions["{key}"]!')

        try:
            self._data.__delitem__(key)
        except KeyError:
            raise KeyError(key)

    def __iter__(self) -> Iterator[str]:
        return self._data.__iter__()

    def __len__(self) -> int:
        return self._data.__len__()

    def __str__(self) -> str:
        data = {
            k: v.model_dump(by_alias=True, exclude_none=False)
            if isinstance(v, (ReferenceObject, ResponseObject))
            else v
            for k, v in self._data.items()
        }

        if self.default_:
            data["default"] = self.default_.model_dump(
                by_alias=True, exclude_none=False
            )

        return str(data)

    def __repr__(self) -> str:
        data = {
            k: v.model_dump(by_alias=True, exclude_none=False)
            if isinstance(v, (ReferenceObject, ResponseObject))
            else v
            for k, v in self._data.items()
        }
        if self.default_:
            data["default"] = self.default_.model_dump(
                by_alias=True, exclude_none=False
            )

        return f"{self.__class__.__name__}({repr(data)})"

    @model_serializer
    def ser_model(self) -> dict[str, Any]:
        retv = {
            "default": (self.default_.model_dump(by_alias=True, exclude_none=True))
            if self.default_
            else None
        }
        for k, v in itertools.chain(self._data.items(), self._ext.items()):
            retv[k] = (
                v.model_dump(by_alias=True, exclude_none=True)
                if isinstance(v, (ReferenceObject, ResponseObject))
                else v
            )

        retv = exclude_blanks(retv)

        return retv or dict()
