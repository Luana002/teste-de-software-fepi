from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# "Banco de dados" em memória
clientes = []
veiculos = [
    {"modelo": "Onix 1.0", "placa": "ABC1D23", "disponivel": True},
    {"modelo": "HB20 1.6", "placa": "EFG4H56", "disponivel": True},
    {"modelo": "Corolla XEi", "placa": "IJK7L89", "disponivel": False},
    {"modelo": "Fiat Argo", "placa": "MNO2P34", "disponivel": True}
]

# Funções do sistema
def cadastrar_cliente(nome, email, cpf):

    for c in clientes:
        if c["cpf"] == cpf:
            return None

    novo_cliente = {
        "nome": nome,
        "email": email,
        "cpf": cpf
    }

    clientes.append(novo_cliente)
    return novo_cliente


def cadastrar_veiculo(modelo, placa):

    for v in veiculos:
        if v["placa"] == placa:
            return None

    novo_veiculo = {
        "modelo": modelo,
        "placa": placa,
        "disponivel": True
    }

    veiculos.append(novo_veiculo)
    return novo_veiculo


def devolver_veiculo(placa):

    for veiculo in veiculos:
        if veiculo["placa"] == placa:
            veiculo["disponivel"] = True
            return True

    return False

# Rotas do sistema
@app.route('/')
def index():
    return render_template('index.html')

# LOGIN CLIENTE
@app.route('/login_cliente', methods=['POST'])
def login_cliente():

    nome = request.form.get('nome')
    cpf = request.form.get('cpf')

    for c in clientes:
        if c['nome'] == nome and c['cpf'] == cpf:
            return redirect(url_for('tela_home'))

    return "Falha no login: Cliente não encontrado ou dados incorretos.", 401

# CADASTRO CLIENTE
@app.route('/cadastrar_cliente', methods=['POST'])
def rota_cadastrar_cliente():

    nome = request.form.get('nome')
    email = request.form.get('email')
    cpf = request.form.get('cpf')

    resultado = cadastrar_cliente(nome, email, cpf)

    if resultado:
        return redirect(url_for('index'))
    else:
        return "Erro: Este CPF já está cadastrado!", 400

# TELA HOME (VEÍCULOS)
@app.route('/home')
def tela_home():
    return render_template('home.html', lista=veiculos)

# LOCAR VEÍCULO
@app.route('/locar/<placa>', methods=['POST'])
def locar(placa):

    for veiculo in veiculos:
        if veiculo["placa"] == placa:

            if veiculo["disponivel"]:
                veiculo["disponivel"] = False

                return redirect(url_for('tela_home'))

    return "Erro ao locar veículo", 400

# TELA CADASTRO VEÍCULO
@app.route("/cadastroVeiculo")
def tela_cadastro_veiculo():
    return render_template("cadastroVeiculo.html")

# CADASTRAR VEÍCULO
@app.route("/cadastrar_veiculo", methods=["POST"])
def cadastrar_veiculo_rota():

    modelo = request.form["modelo"]
    placa = request.form["placa"]

    veiculo = cadastrar_veiculo(modelo, placa)

    if veiculo:
        return redirect(url_for('tela_home'))
    else:
        return "Erro: Veículo já cadastrado!", 400

# TELA DEVOLUÇÃO
@app.route("/devolucao")
def tela_devolucao():
    return render_template("devolucao.html")

# DEVOLVER VEÍCULO
@app.route("/devolver_veiculo", methods=["POST"])
def devolver_veiculo_rota():

    placa = request.form["placa"]

    resultado = devolver_veiculo(placa)

    if resultado:
        return redirect(url_for('tela_home'))
    else:
        return "Veículo não encontrado."

# EXECUTAR SERVIDOR
if __name__ == '__main__':
    app.run(debug=True)