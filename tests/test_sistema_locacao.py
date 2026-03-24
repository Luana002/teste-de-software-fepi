from src.sistema_locacao import cadastrar_cliente

def test_cadastrar_cliente():
    cliente = cadastrar_cliente("Maria", "12345678900")

    assert cliente["nome"] == "Maria"
    assert cliente["cpf"] == "12345678900"