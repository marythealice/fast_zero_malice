from http import HTTPStatus

from jwt import decode

from fast_zero.security import create_access_token, settings


def test_jwt():
    data = {'sub': 'nantesmalice@gmail.com'}
    token = create_access_token(data)

    decoded = decode(
        token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
    )

    assert decoded['sub'] == data['sub']
    # testa se o valor exp foi add ao token
    assert decoded['exp']


def test_jwt_invalid_token(client):
    response = client.delete(
        '/users/1', headers={'Authorization': 'Bearer token invalido'}
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}


def test_get_current_user_not_found_through_email(client):
    data = {'sub': 'test@test'}
    token = create_access_token(data)

    response = client.put(
        '/users/1',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}
