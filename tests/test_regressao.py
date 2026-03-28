import pytest

from src import sistema_locacao


pytestmark = pytest.mark.regression


def test_cadastrar_veiculo_pela_rota_nao_quebra_e_exibe_item_na_home(client):
    response = client.post(
        "/cadastrar_veiculo",
        data={
            "modelo": "Civic Touring",
            "placa": "QWE1R23",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Civic Touring" in response.data
    assert any(veiculo["placa"] == "QWE1R23" for veiculo in sistema_locacao.veiculos)
