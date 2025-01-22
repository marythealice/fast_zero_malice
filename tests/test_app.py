from http import HTTPStatus


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
