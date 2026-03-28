import pytest

from src import sistema_locacao


pytestmark = pytest.mark.system


def test_fluxo_principal_do_cliente_no_sistema(client):
    index = client.get("/")
    assert index.status_code == 200
    assert b"Entrar" in index.data

    cadastro = client.post(
        "/cadastrar_cliente",
        data={
            "nome": "Ana",
            "email": "ana@teste.com",
            "cpf": "11122233344",
        },
    )
    assert cadastro.status_code == 302

    login = client.post(
        "/login_cliente",
        data={
            "nome": "Ana",
            "cpf": "11122233344",
        },
        follow_redirects=True,
    )
    assert login.status_code == 200
    assert b"Onix 1.0" in login.data

    locacao = client.post("/locar/ABC1D23", follow_redirects=True)
    assert locacao.status_code == 200
    assert b"Locado" in locacao.data
    assert sistema_locacao.verificar_disponibilidade("ABC1D23") is False

    devolucao = client.post(
        "/devolver_veiculo",
        data={"placa": "ABC1D23"},
        follow_redirects=True,
    )
    assert devolucao.status_code == 200
    assert b"Onix 1.0" in devolucao.data
    assert sistema_locacao.verificar_disponibilidade("ABC1D23") is True
