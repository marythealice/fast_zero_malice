from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app

"""nomear cada função de teste relacionado ao que ela está testando
no caso abaixo, ler a url do site """


def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange (organizando o teste)

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
