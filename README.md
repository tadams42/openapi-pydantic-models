# openapi-pydantic-models

[![PyPI Status](https://badge.fury.io/py/openapi-pydantic-models.svg)](https://badge.fury.io/py/openapi-pydantic-models)
[![license](https://img.shields.io/pypi/l/openapi-pydantic-models.svg)](https://opensource.org/licenses/MIT)
[![python_versions](https://img.shields.io/pypi/pyversions/openapi-pydantic-models.svg)](https://pypi.org/project/openapi-pydantic-models/)

[OpenAPI Specification v3.1.0](https://spec.openapis.org/oas/v3.1.0) objects implemented
as [pydantic](https://docs.pydantic.dev/) models.

## Install

```sh
pip install openapi-pydantic-models
```

## Usage

It can load whole OpenAPI specification:

```py
import requests
import yaml

from openapi_pydantic_models import OpenAPIObject

url = "https://rapidocweb.com/specs/petstore_extended.yaml"
response = requests.get(url)
data = yaml.full_load(response.text)
spec = OpenAPIObject.parse_obj(data)
```

All parts of OpenAPI object tree are represented by Python classes with static type
infos:

```py
repr(spec.paths["/pet/{petId}/uploadImage"].post.responses["200"])

ResponseObject(
    description='successful operation',
    headers=None,
    content={
        'application/json': MediaTypeObject(
            schema_={
                '$ref': '#/components/schemas/ApiResponse'
            },
            example=None,
            examples=None,
            encoding=None
        )
    },
    links=None
)
```

Any object from object tree can always be exported back to OpenaAPI data (`dict`) via
`dict()` method:

```py
spec.paths["/pet/{petId}/uploadImage"].post.responses["200"].dict()

{
    'description': 'successful operation',
     'content': {
        'application/json': {
            'schema': {
                '$ref': '#/components/schemas/ApiResponse'
            }
        }
    }
}
```

Loading specification performs minimal (unavoidable) validation: it rises exception for
unknown fields:

```py
from openapi_pydantic_models import ResponseObject

data = {
    "description": 'successful operation',
    "foo": "bar"
}

obj = ResponseObject.parse_obj(data)

# ValidationError: 1 validation error for ResponseObject
# foo
#   extra fields not permitted (type=value_error.extra)
```

Any other validations defined by OpenAPI Specification are not implemented.
`openapi-pydantic-models` intends to make programmatic editing of OpenAPI specifications easier
and developer friendly (compared to working with "raw" `dict`-s). Complex spec
validations are already implemented in other packages.

Even though "extra" fields in input are not allowed, [4.9 Specification
Extensions](https://spec.openapis.org/oas/v3.1.0#specificationExtensions) are fully and
transparently supported for objects that allow them:

```py
data = {
    "description": 'successful operation',
    "x-foo": "bar",
    "x-bar": [42]
}
obj = ResponseObject.parse_obj(data)

obj.extensions
ExtensionsStorage({'x-foo': 'bar', 'x-bar': [42]})

obj.dict()
{'description': 'successful operation', 'x-foo': 'bar', 'x-bar': [42]}
```

And of course, all objects can be edited:

```py
obj.description = "ZOMG!"
obj.extensions["x-baz"] = {1: {2: 3}}
obj.dict()
{'description': 'ZOMG!', 'x-foo': 'bar', 'x-bar': [42], 'x-baz': {1: {2: 3}}}
```

where specification extensions are protected from invalid keys:

```py
obj.extensions["baz"] = 34
# KeyError: 'baz'

obj.extensions["x-baz"] = 34
# OK
```

## Where are the docs for this thing?

Makes no sense writing them since [OpenAPI
Specification](https://spec.openapis.org/oas/v3.1.0) is already fully and excellently
documented.

In OpenAPI docs, wherever you see "Foo Object" you can find `class FooObject` in
`openapi-pydantic-models`. Reverse works too: if you want to know what is
`openapi_pydantic_models.ServerObject` check [4.8.5 Server
Object](https://spec.openapis.org/oas/v3.1.0#server-object)

## Where are the tests?

There is one!

I know :-( !

This was written during one lazy weekend afternoon. When I get one of those again, I
might add more tests.
