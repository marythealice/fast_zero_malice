from http import HTTPStatus

"""nomear cada função de teste relacionado ao que ela está testando
no caso abaixo, ler a url do site """


def test_read_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')  # act (ação, execução de um bloco de test)
    print(response)

    assert response.status_code == HTTPStatus.OK
    """
    assert (making sure that the answer's status code is ok
    """
    assert response.json() == {'message': 'Hello World'}
    """
    assert (but now making sure that the
    expected response was the same as the received one
    """


def test_create_user(client):
    response = client.post(  # testando UserSchema
        '/users/',
        json={
            'username': 'testusername',
            'email': 'test@test.com',
            'password': 'password',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    # voltou o status correto? se sim..
    # agora vamos validar o UserPublic
    assert response.json() == {
        'id': 1,
        'username': 'testusername',
        'email': 'test@test.com',
    }


def test_update_users(client):
    response = client.put(
        '/users/1',
        json={
            'password': '123',
            'id': 1,
            'username': 'testusername2',
            'email': 'test@test.com',
        },
    )
    assert response.json() == {
        'id': 1,
        'username': 'testusername2',
        'email': 'test@test.com',
    }


def test_update_users_return_not_found(client):
    response = client.put(
        '/users/200',  # 200 numero aleat. de usuario n existente
        json={
            'password': 'mynewpassword',
            'username': 'newusername',
            'email': 'new@test.com',
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND

    assert response.json() == {'detail': 'User not found'}


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {'id': 1, 'username': 'testusername2', 'email': 'test@test.com'}
        ]
    }


def test_get_user_return_not_found(client):
    response = client.get('/users/200')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_get_user_id(client):
    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'testusername2',
        'email': 'test@test.com',
    }


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.json() == {'message': 'User deleted!'}


def test_delete_user_return_not_found(client):
    response = client.delete('/users/200')

    assert response.status_code == HTTPStatus.NOT_FOUND

    assert response.json() == {'detail': 'User not found'}
