from http import HTTPStatus


# ====================
#       DELETES
# ====================
def test_delete_user_success(client, user):
    response = client.delete("/users/1")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "user deleted"}


def test_delete_user_fail(client, user):
    response = client.delete("/users/-1")

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "user not found"}
