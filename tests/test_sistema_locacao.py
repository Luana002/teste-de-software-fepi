from src.sistema_locacao import cadastrar_cliente

def test_cadastrar_cliente():
    cliente = cadastrar_cliente("Maria", "maria@com","12345678900")

    assert cliente["nome"] == "Maria"
    assert cliente["email"] == "maria@com"
    assert cliente["cpf"] == "12345678900"