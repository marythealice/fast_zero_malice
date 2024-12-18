from sqlalchemy import select

from models import User


def test_create_user(session):
    user = User(
        username='ba',
        email='ba@ba.com',
        password='ba',
    )

    session.add(user)
    session.commit()  # commiting all changes made

    result = session.scalar(
        select(User).where(User.email == 'ba@ba.com')
    )  # returns a python obj from db

    assert result.username == 'ba'
