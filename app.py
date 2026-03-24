from flask import Flask, render_template, request
from src.sistema_locacao import cadastrar_cliente

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/cadastrar_cliente", methods=["POST"])
def cadastrar():
    nome = request.form["nome"]
    cpf = request.form["cpf"]

    cliente = cadastrar_cliente(nome, cpf)

    return f"Cliente {cliente['nome']} cadastrado com sucesso!"


if __name__ == "__main__":
    app.run(debug=True)