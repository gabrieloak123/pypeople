from http import HTTPStatus


# ====================
#         PUTS
# ====================
def test_put_user_success(client, user):
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


def test_put_user_integrity_error(client, user):
    client.post(
        "/users",
        json={
            "username": "bono",
            "email": "bono@gmail.com",
            "password": "bono",
        },
    )

    response_update = client.put(
        f"/users/{user.id}",
        json={
            "username": "bono",
            "email": "bono@outlook.com",
            "password": "bono",
        },
    )

    assert response_update.status_code == HTTPStatus.CONFLICT
    assert response_update.json() == {"detail": "credentials already exist"}


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
