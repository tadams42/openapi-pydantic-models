from __future__ import annotations

import itertools
from typing import Any, Iterator, MutableMapping

from pydantic import PrivateAttr

from ..commons import BaseModel, exclude_blanks
from .path_item_object import PathItemObject
from .reference_object import ReferenceObject
from .specification_extensions import ExtensionsStorage


class CallbackObject(MutableMapping[str, PathItemObject | ReferenceObject], BaseModel):
    """
    Model for OpenAPI CallbackObject.

    This object MAY be extended with with [4.9 Specification
    Extensions](https://spec.openapis.org/oas/v3.1.0#specificationExtensions).
    """

    _data: dict[str, ReferenceObject | PathItemObject] = PrivateAttr(
        default_factory=dict
    )
    _ext: ExtensionsStorage = PrivateAttr(default_factory=ExtensionsStorage)

    def __init__(self, *args, **kwargs):
        super().__init__()
        raw_data = dict(*args, **kwargs)
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
        for typ in [ReferenceObject, PathItemObject]:
            if v is None:
                try:
                    v = typ.parse_obj(value)
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
        return str(
            {
                k: v.dict(by_alias=True, exclude_none=False)
                if isinstance(v, (ReferenceObject, PathItemObject))
                else v
                for k, v in self._data.items()
            }
        )

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            + repr(
                {
                    k: v.dict(by_alias=True, exclude_none=False)
                    if isinstance(v, (ReferenceObject, PathItemObject))
                    else v
                    for k, v in self._data.items()
                }
            )
            + ")"
        )

    def dict(
        self, *, by_alias: bool = True, exclude_none: bool = True, **kwargs
    ) -> dict[str, Any]:
        retv = {
            k: (
                v.dict(by_alias=by_alias, exclude_none=exclude_none, **kwargs)
                if isinstance(v, (ReferenceObject, PathItemObject))
                else v
            )
            for k, v in itertools.chain(self._data.items(), self._ext.items())
        }

        if exclude_none:
            retv = exclude_blanks(retv)

        return retv or dict()
