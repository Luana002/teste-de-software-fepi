clientes = []
veiculos = []

def cadastrar_cliente(nome, email, cpf):
    cliente = {
        "nome": nome,
        "email": email,
        "cpf": cpf
    }
    clientes.append(cliente)
    return cliente


def cadastrar_veiculo(modelo, placa):
    veiculo = {
        "modelo": modelo,
        "placa": placa,
        "disponivel": True
    }
    veiculos.append(veiculo)
    return veiculo


def verificar_disponibilidade(placa):
    for veiculo in veiculos:
        if veiculo["placa"] == placa:
            return veiculo["disponivel"]
    return False