import pytest

from src import sistema_locacao


pytestmark = pytest.mark.integration


def test_cadastro_pela_rota_persiste_cliente_no_estado_compartilhado(client):
    response = client.post(
        "/cadastrar_cliente",
        data={
            "nome": "Maria",
            "email": "maria@teste.com",
            "cpf": "12345678900",
        },
    )

    assert response.status_code == 302
    assert response.headers["Location"].endswith("/")
    assert sistema_locacao.clientes == [
        {
            "nome": "Maria",
            "email": "maria@teste.com",
            "cpf": "12345678900",
        }
    ]


def test_locacao_pela_rota_reflete_na_regra_de_disponibilidade(client):
    response = client.post("/locar/ABC1D23")

    assert response.status_code == 302
    assert response.headers["Location"].endswith("/home")
    assert sistema_locacao.verificar_disponibilidade("ABC1D23") is False


def test_fluxo_cadastro_e_login_compartilha_o_mesmo_estado(client):
    client.post(
        "/cadastrar_cliente",
        data={
            "nome": "Joao",
            "email": "joao@teste.com",
            "cpf": "99999999999",
        },
    )

    response = client.post(
        "/login_cliente",
        data={
            "nome": "Joao",
            "cpf": "99999999999",
        },
    )

    assert response.status_code == 302
    assert response.headers["Location"].endswith("/home")
