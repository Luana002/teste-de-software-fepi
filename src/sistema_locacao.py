clientes = []
veiculos = []

def cadastrar_cliente(nome, email, cpf):
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            return None

    cliente = {
        "nome": nome,
        "email": email,
        "cpf": cpf
    }

    clientes.append(cliente)
    return cliente


def cadastrar_veiculo(modelo, placa):

    for v in veiculos:
        if v["placa"] == placa:
            return None

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


def locar_veiculo(placa):

    for veiculo in veiculos:
        if veiculo["placa"] == placa and veiculo["disponivel"]:
            veiculo["disponivel"] = False
            return True

    return False


def devolver_veiculo(placa):

    for veiculo in veiculos:
        if veiculo["placa"] == placa:
            veiculo["disponivel"] = True
            return True

    return False
