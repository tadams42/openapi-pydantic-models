from typing import Any


def is_blank(data: Any) -> bool:
    if data is None:
        return True

    if data == False or data == 0:
        return False

    if isinstance(data, (str, bytes)):
        return not bool(data.strip())

    retv = None

    # Mapping
    try:
        retv = all(is_blank(v) for v in data.values())
    except AttributeError:
        pass
    if retv is not None:
        return retv

    # Iterable
    try:
        retv = all(is_blank(v) for v in data)
    except TypeError:
        pass
    if retv is not None:
        return retv

    return not bool(data)


def strip_whitespace(data: Any) -> Any:
    if isinstance(data, (str, bytes)):
        return data.strip()

    # Mapping
    try:
        return type(data)(
            (
                strip_whitespace(k),
                strip_whitespace(v),
            )
            for k, v in data.items()
        )
    except (AttributeError, TypeError):
        pass

    # Iterable
    try:
        return type(data)(strip_whitespace(v) for v in data)
    except (AttributeError, TypeError):
        pass

    return data


def exclude_blanks(data: Any):
    retv = strip_whitespace(data)

    if isinstance(retv, (str, bytes)):
        return retv if not is_blank(retv) else None

    # Mapping
    try:
        retv = type(data)(
            (k, v) for k, v in retv.items() if not is_blank(k) and not is_blank(v)
        )
        return retv or None
    except (AttributeError, TypeError):
        pass

    # Iterable
    try:
        retv = type(data)(v for v in retv if not is_blank(v))
        return retv or None
    except (AttributeError, TypeError):
        pass

    return retv if not is_blank(retv) else None
