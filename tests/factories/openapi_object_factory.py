import pytest
import yaml

from importlib.resources import files
from . import blobs


@pytest.fixture(scope="session")
def petstore_extended():
    with files(blobs).joinpath("petstore_extended.yaml").open("r") as f:
        data = yaml.full_load("\n".join(f.readlines()))

    return data
