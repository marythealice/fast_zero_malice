from http import HTTPStatus

from jwt import decode

from fast_zero.security import ALGORITHM, SECRET_KEY, create_access_token


def test_jwt():
    data = {'sub': 'nantesmalice@gmail.com'}
    token = create_access_token(data)

    decoded = decode(token, SECRET_KEY, algorithms=[ALGORITHM])

    assert decoded['sub'] == data['sub']
    # testa se o valor exp foi add ao token
    assert decoded['exp']


def test_jwt_invalid_token(client):
    response = client.delete(
        '/users/1', headers={'Authorization': 'Bearer token invalido'}
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}
