import re
from collections.abc import MutableMapping
from typing import Any, Iterator

from pydantic import PrivateAttr

from ..commons import BaseModel, exclude_blanks


class ExtensionsStorage(MutableMapping[str, Any]):
    _RE_KEYS = re.compile(r"^x-")

    @classmethod
    def is_key(cls, key: str) -> bool:
        return bool(cls._RE_KEYS.match(key))

    def __init__(self, *args, **kwargs):
        self._data = {
            str(k): v for k, v in dict(*args, **kwargs).items() if self.is_key(str(k))
        }

    def __getitem__(self, key: str) -> Any:
        try:
            return self._data.__getitem__(str(key))
        except KeyError:
            raise KeyError(key)

    def __setitem__(self, key: str, value: Any):
        if self.is_key(str(key)):
            self._data.__setitem__(str(key), value)
        else:
            raise KeyError(key)

    def __delitem__(self, key: str):
        try:
            self._data.__delitem__(str(key))
        except KeyError:
            raise KeyError(key)

    def __iter__(self) -> Iterator[str]:
        return self._data.__iter__()

    def __len__(self) -> int:
        return self._data.__len__()

    def __str__(self) -> str:
        return str({str(k): v for k, v in self._data.items()})

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            + repr({k: v for k, v in self._data.items()})
            + ")"
        )


class SpecificationExtendable(BaseModel):
    """
    Base model class for models that can be extended via OpenAPI specification
    extensions.

    Inheriting from this class will:

    - add property ``extensions``
    - correctly parse extended object
    - correctly convert extended object to dict

    Example::

        data = {
            "attr": "...",
            "x-foo": 42,
            "x-bar": ["baz"]
        }

        class SomeModel(SpecificationExtendable):
            attr: str

        obj = SomeModel(**data)

        repr(obj)
        >>> SomeModel(attr='...')
        repr(obj.extensions)
        >>> "ExtensionsStorage({'x-foo': 42, 'x-bar': ['baz']})"
        obj.dict()
        >>> {'attr': '...', 'x-foo': 42, 'x-bar': ['baz']}

        obj = SomeModel.parse_obj(data)

        repr(obj)
        >>> SomeModel(attr='...')
        repr(obj.extensions)
        >>> "ExtensionsStorage({'x-foo': 42, 'x-bar': ['baz']})"
        obj.dict()
        >>> {'attr': '...', 'x-foo': 42, 'x-bar': ['baz']}
    """

    _ext: ExtensionsStorage = PrivateAttr(default_factory=ExtensionsStorage)

    def __init__(self, **data):
        super().__init__(
            **{k: v for k, v in data.items() if not ExtensionsStorage.is_key(str(k))}
        )
        self._ext = ExtensionsStorage(data)

    @property
    def extensions(self) -> ExtensionsStorage:
        return self._ext

    def dict(
        self, *, by_alias: bool = True, exclude_none: bool = True, **kwargs
    ) -> dict[str, Any]:
        retv = (
            super().dict(exclude_none=exclude_none, by_alias=by_alias, **kwargs)
            or dict()
        )

        for k, v in self._ext.items():
            retv[str(k)] = v

        if exclude_none:
            retv = exclude_blanks(retv)

        return retv or dict()
