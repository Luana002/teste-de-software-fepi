from flask import Flask, redirect, render_template, request, url_for

from src import sistema_locacao

app = Flask(__name__)

# "Banco de dados" em memoria
DEFAULT_VEHICLES = [
    {"modelo": "Onix 1.0", "placa": "ABC1D23", "disponivel": True},
    {"modelo": "HB20 1.6", "placa": "EFG4H56", "disponivel": True},
    {"modelo": "Corolla XEi", "placa": "IJK7L89", "disponivel": False},
    {"modelo": "Fiat Argo", "placa": "MNO2P34", "disponivel": True},
]

clientes = sistema_locacao.clientes
veiculos = sistema_locacao.veiculos


def resetar_dados():
    clientes.clear()
    veiculos.clear()
    veiculos.extend([veiculo.copy() for veiculo in DEFAULT_VEHICLES])


resetar_dados()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login_cliente", methods=["POST"])
def login_cliente():
    nome = request.form.get("nome")
    cpf = request.form.get("cpf")

    for cliente in clientes:
        if cliente["nome"] == nome and cliente["cpf"] == cpf:
            return redirect(url_for("tela_home"))

    return "Falha no login: Cliente nao encontrado ou dados incorretos.", 401


@app.route("/cadastrar_cliente", methods=["POST"])
def rota_cadastrar_cliente():
    nome = request.form.get("nome")
    email = request.form.get("email")
    cpf = request.form.get("cpf")

    resultado = sistema_locacao.cadastrar_cliente(nome, email, cpf)

    if resultado:
        return redirect(url_for("index"))

    return "Erro: Este CPF ja esta cadastrado!", 400


@app.route("/home")
def tela_home():
    return render_template("home.html", lista=veiculos)


@app.route("/locar/<placa>", methods=["POST"])
def locar(placa):
    if sistema_locacao.locar_veiculo(placa):
        return redirect(url_for("tela_home"))

    return "Erro ao locar veiculo", 400


@app.route("/cadastroVeiculo")
def tela_cadastro_veiculo():
    return render_template("cadastroVeiculo.html")


@app.route("/cadastrar_veiculo", methods=["POST"])
def cadastrar_veiculo_rota():
    modelo = request.form["modelo"]
    placa = request.form["placa"]

    veiculo = sistema_locacao.cadastrar_veiculo(modelo, placa)

    if veiculo:
        return redirect(url_for("tela_home"))

    return "Erro: Veiculo ja cadastrado!", 400


@app.route("/devolucao")
def tela_devolucao():
    return render_template("devolucao.html")


@app.route("/devolver_veiculo", methods=["POST"])
def devolver_veiculo_rota():
    placa = request.form["placa"]

    resultado = sistema_locacao.devolver_veiculo(placa)

    if resultado:
        return redirect(url_for("tela_home"))

    return "Veiculo nao encontrado."


if __name__ == "__main__":
    app.run(debug=True)
