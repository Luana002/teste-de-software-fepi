import time

import pytest

from src import sistema_locacao


pytestmark = pytest.mark.performance


def test_home_renderiza_lista_grande_em_tempo_aceitavel(client):
    for indice in range(500):
        sistema_locacao.cadastrar_veiculo(
            f"Modelo {indice}",
            f"TST{indice:04d}",
        )

    inicio = time.perf_counter()
    response = client.get("/home")
    duracao = time.perf_counter() - inicio

    assert response.status_code == 200
    assert b"Modelo 499" in response.data
    assert duracao < 1.5
