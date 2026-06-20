import pytest
from fastapi.testclient import TestClient

from pythando.app import app


@pytest.fixture
def client():
    return TestClient(app)
