import pytest

from src import sistema_locacao


pytestmark = pytest.mark.acceptance


def test_cliente_nao_consegue_cadastrar_mesmo_cpf_duas_vezes(client):
    client.post(
        "/cadastrar_cliente",
        data={
            "nome": "Carlos",
            "email": "carlos@teste.com",
            "cpf": "22233344455",
        },
    )

    response = client.post(
        "/cadastrar_cliente",
        data={
            "nome": "Carlos Clone",
            "email": "clone@teste.com",
            "cpf": "22233344455",
        },
    )

    assert response.status_code == 400
    assert b"CPF" in response.data
    assert len(sistema_locacao.clientes) == 1


def test_cliente_nao_consegue_locar_um_veiculo_ja_indisponivel(client):
    response = client.post("/locar/IJK7L89")

    assert response.status_code == 400
    assert b"Erro ao locar" in response.data
    assert sistema_locacao.verificar_disponibilidade("IJK7L89") is False
