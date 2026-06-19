from http import HTTPStatus

from fastapi.testclient import TestClient

from src.pythando.app import app


def test_root():
    client = TestClient(app)  # Arrange
    response = client.get("/")  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {"message": "hello world"}  # Assert
