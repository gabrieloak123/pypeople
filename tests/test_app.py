from http import HTTPStatus


def test_post_user(client):
    response = client.post(
        "/users/",
        json={
            "username": "gabrieloak",
            "email": "gabriel@oak.com",
            "password": "saopaulo",
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "id": 1,
        "username": "gabrieloak",
        "email": "gabriel@oak.com",
    }


def test_get_user_success(client):
    response = client.get("/users/1")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "id": 1,
        "username": "gabrieloak",
        "email": "gabriel@oak.com",
    }


def test_get_user_fail(client):
    response = client.get("/users/-1")

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "user not found"}


def test_get_users(client):
    response = client.get("/users/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "users": [
            {
                "id": 1,
                "username": "gabrieloak",
                "email": "gabriel@oak.com",
            }
        ]
    }


def test_put_user_success(client):
    response = client.put(
        "/users/1",
        json={
            "username": "gabrieleucaliptus",
            "email": "gabriel@eucaliptus.com",
            "password": "saopaulo",
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "id": 1,
        "username": "gabrieleucaliptus",
        "email": "gabriel@eucaliptus.com",
    }


def test_put_user_fail(client):
    response = client.put(
        "/users/-1",
        json={
            "username": "gabrieleucaliptus",
            "email": "gabriel@eucaliptus.com",
            "password": "saopaulo",
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "user not found"}


def test_delete_user_success(client):
    response = client.delete("/users/1")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "user deleted"}


def test_delete_user_fail(client):
    response = client.delete("/users/-1")

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "user not found"}
