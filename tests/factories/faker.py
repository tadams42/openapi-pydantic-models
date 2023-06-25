import json
from dataclasses import dataclass
from importlib.resources import files

from faker import Faker
from faker.providers import BaseProvider

from . import blobs

fake = Faker()


class CustomProviders(BaseProvider):
    def spdx_licence(self):
        return fake.random_element(_spdx_licenses())

    def open_api_extension_key(self, cnt=1):
        if cnt == 1:
            return fake.random_element(_OPENAPI_EXTENSION_FIELDS)

        keys = set()
        while len(keys) < cnt:
            keys.add(fake.random_element(_OPENAPI_EXTENSION_FIELDS))

        return list(keys)

    def open_api_extension_value(self):
        return fake.random_element(_OPENAPI_EXTENSION_VALUES)


fake.add_provider(CustomProviders)


_OPENAPI_EXTENSION_FIELDS = [
    f"{k}{idx}"
    for k in {
        "x-ignoredHeaderParameters",
        "x-servers",
        "x-tagGroups",
        "x-webhooks",
        "x-logo",
        "x-displayName",
        "x-traitTag",
        "x-codeSamples",
        "x-hideTryItPanel",
        "x-meta",
        "x-example",
        "x-examples",
        "x-summary",
        "x-additionalPropertiesName",
        "x-enumDescriptions",
        "x-extendedDiscriminator",
        "x-nullable",
        "x-tags",
        "x-defaultClientId",
        "x-usePkce",
    }
    for idx in range(10)
]


_OPENAPI_EXTENSION_VALUES = [
    42,
    True,
    False,
    0,
    3.42,
    ["Foo", "Bar", "Baz"],
    {1: 2, 3: 4, 5: 6},
    ["Foo", "Bar", "Baz", {1: 2, 3: 4, 5: 6}],
    {1: 2, 3: 4, 5: 6, 7: ["Foo", "Bar", "Baz"]},
]


@dataclass
class SpdxLicense:
    id: str
    name: str
    reference: str


_SPDX_LICENSES: list[SpdxLicense] = []


def _spdx_licenses():
    global _SPDX_LICENSES

    if not _SPDX_LICENSES:
        with files(blobs).joinpath("spdx_licenses.json").open("r") as f:
            data = json.load(f)
        _SPDX_LICENSES.extend(
            SpdxLicense(
                id=_["licenseId"],
                name=_["name"],
                reference=_["reference"],
            )
            for _ in data["licenses"]
        )

    return _SPDX_LICENSES
