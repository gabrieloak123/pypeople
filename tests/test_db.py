from dataclasses import asdict

from sqlalchemy import select

from pypeople.models import User


def test_create_user(session, mock_db_time):
    with mock_db_time(model=User) as time:
        new_user = User(
            username="bono", email="bono@gmail.com", password="bono"
        )
        session.add(new_user)
        session.commit()

    user = session.scalar(select(User).where(User.username == "bono"))

    assert asdict(user) == {
        "id": 1,
        "username": "bono",
        "email": "bono@gmail.com",
        "password": "bono",
        "created_at": time,
        "updated_at": time,
    }
