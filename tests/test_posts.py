from http import HTTPStatus


# ====================
#        POSTS
# ====================
def test_post_user_success(client):
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


def test_post_username_already_in_use(client, user):
    client.post(
        "/users/",
        json={
            "username": user.username,
            "email": "gabriel@oak.com",
            "password": "saopaulo",
        },
    )

    response = client.post(
        "/users/",
        json={
            "username": "gabrieloak",
            "email": "gabriel@gmail.com",
            "password": "saopaulo",
        },
    )

    assert response.status_code == HTTPStatus.CONFLICT
    assert response.json() == {"detail": "username already in use"}


def test_post_email_already_in_use(client, user):
    client.post(
        "/users/",
        json={
            "username": "gabrieloak",
            "email": user.email,
            "password": "saopaulo",
        },
    )

    response = client.post(
        "/users/",
        json={
            "username": "gabrieloak1",
            "email": "gabriel@oak.com",
            "password": "saopaulo",
        },
    )

    assert response.status_code == HTTPStatus.CONFLICT
    assert response.json() == {"detail": "email already in use"}
