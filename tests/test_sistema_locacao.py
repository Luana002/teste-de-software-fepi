import pytest

from src import sistema_locacao


pytestmark = pytest.mark.unit


def test_cadastrar_cliente():
    cliente = sistema_locacao.cadastrar_cliente("Maria", "maria@com", "12345678900")

    assert cliente["nome"] == "Maria"
    assert cliente["email"] == "maria@com"
    assert cliente["cpf"] == "12345678900"
    assert sistema_locacao.clientes == [cliente]


def test_nao_cadastra_cliente_com_cpf_duplicado():
    sistema_locacao.cadastrar_cliente("Maria", "maria@com", "12345678900")

    cliente_duplicado = sistema_locacao.cadastrar_cliente(
        "Maria 2",
        "maria2@com",
        "12345678900",
    )

    assert cliente_duplicado is None
    assert len(sistema_locacao.clientes) == 1


def test_locar_veiculo_altera_disponibilidade():
    sistema_locacao.cadastrar_veiculo("Onix 1.0", "ABC1D23")

    resultado = sistema_locacao.locar_veiculo("ABC1D23")

    assert resultado is True
    assert sistema_locacao.verificar_disponibilidade("ABC1D23") is False


def test_devolver_veiculo_torna_item_disponivel_novamente():
    sistema_locacao.cadastrar_veiculo("Onix 1.0", "ABC1D23")
    sistema_locacao.locar_veiculo("ABC1D23")

    resultado = sistema_locacao.devolver_veiculo("ABC1D23")

    assert resultado is True
    assert sistema_locacao.verificar_disponibilidade("ABC1D23") is True
