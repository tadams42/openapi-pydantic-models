import enum


class Styles(str, enum.Enum):
    matrix = "matrix"
    label = "label"
    form = "form"
    simple = "simple"
    spaceDelimited = "spaceDelimited"
    pipeDelimited = "pipeDelimited"
    deepObject = "deepObject"
