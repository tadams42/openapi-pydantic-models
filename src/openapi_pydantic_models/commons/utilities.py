from typing import Any


def is_blank(data: Any) -> bool:
    if data is None:
        return True

    if data == False or data == 0:
        return False

    if isinstance(data, (str, bytes)):
        return not bool(data.strip())

    retv = None

    # security: list[SecurityRequirementObject] | None = None
    #
    # example:
    #
    #     data = {
    #         "security": [{"refresh_token": []}]
    #     }
    #
    # Is non-blank object in context of OpenAPI, although
    #
    #     is_blank(data) == True

    # Mapping
    try:
        found_non_blank = False
        for k, v in data.items():
            if k == "security":
                found_non_blank = bool(v and any(_.keys() for _ in v))
            else:
                found_non_blank = not is_blank(v)

            if found_non_blank:
                break

        retv = not found_non_blank
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
        tuples = []
        for k, v in retv.items():
            if k == "security" and v:
                tuples.append(
                    (
                        k,
                        [_ for _ in v if _ and _.keys()],
                    )
                )
            elif not is_blank(k) and not is_blank(v):
                tuples.append(
                    (
                        k,
                        v,
                    )
                )

        retv = type(data)(_ for _ in tuples)
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
