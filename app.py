from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

clientes = []
veiculos = []

def cadastrar_cliente(nome, email, cpf):
    
    for c in clientes:
        if c["cpf"] == cpf:
            return None 
    
    novo_cliente = {"nome": nome, "email": email, "cpf": cpf}
    clientes.append(novo_cliente)
    return novo_cliente

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login_cliente', methods=['POST'])
def login_cliente():
    nome = request.form.get('nome')
    cpf = request.form.get('cpf')
    
    for c in clientes:
        if c['nome'] == nome and c['cpf'] == cpf:
            
            return redirect(url_for('tela_home'))
            
    return "Falha no login: Cliente não encontrado ou dados incorretos.", 401

@app.route('/cadastrar_cliente', methods=['POST'])
def rota_cadastrar_cliente():
    nome = request.form.get('nome')
    email = request.form.get('email')
    cpf = request.form.get('CPF')
    
    resultado = cadastrar_cliente(nome, email, cpf)
    
    if resultado:
        return redirect(url_for('index'))
    else:
        return "Erro: Este CPF já está cadastrado!", 400


@app.route('/home')
def tela_home():
    return render_template('home.html', lista=veiculos)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/locar/<placa>', methods=['POST'])
def locar(placa):
    for veiculo in veiculos:
        if veiculo["placa"] == placa:
            if veiculo["disponivel"]:
                veiculo["disponivel"] = False 
                return redirect(url_for('tela_veiculos'))
    return "Erro ao locar veículo", 400