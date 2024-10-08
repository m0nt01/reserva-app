
from flask import Flask, render_template
import csv
from flask import Flask, render_template, request

app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def index():
    with open('data.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Route', 'Data'])
        writer.writerow(['Index', 'Sample data for index page'])
    return render_template('index.html')

# Rota para a página de login
@app.route('/login')
def login():
    with open('data.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Login', 'Sample data for login page'])
    return render_template('login.html')

# Rota para a página de cadastro
@app.route('/cadastro')
def cadastro():
    with open('data.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Cadastro', 'Sample data for cadastro page'])
    return render_template('cadastro.html')

# Rota para a página de cadastro de salas
@app.route('/cadastrar-sala')
def cadastrar_sala():
    with open('data.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Cadastrar Sala', 'Sample data for cadastrar sala page'])
    return render_template('cadastrar-sala.html')

# Rota para a página de listagem de salas
@app.route('/listar-salas')
def listar_salas():
    with open('data.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Listar Salas', 'Sample data for listar salas page'])
    return render_template('listar-salas.html')

# Rota para a página de reserva de salas
@app.route('/reservar-sala')
def reservar_sala():
    with open('data.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Reservar Sala', 'Sample data for reservar sala page'])
    return render_template('reservar-sala.html')

# Rota para a página de listagem de reservas
@app.route('/reservas')
def reservas():
    with open('data.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Reservas', 'Sample data for reservas page'])
    return render_template('reservas.html')

if __name__ == '__main__':
    app.run(debug=True)
    
def obter_salas():
    with open("salas.csv", "r") as file:
        lista_salas = []
        for linha in file:
            id, tipo, descricao, capacidade = linha.strip().split(",")
            sala = {
                "id": id,
                "tipo": tipo,
                "descricao": descricao,
                "capacidade": int(capacidade),
            }
            lista_salas.append(sala)
        
        return lista_salas
    
def cadastrar_sala(sala):
    linha = f"\n{sala['id']},{sala['tipo']},{sala['descricao']},{sala['capacidade']}"
    with open("salas.csv", "a") as file:
        file.write(linha)

@app.route('/reservar-sala', methods=['POST'])
def reservar_sala(reserva):
    linha = f"\n{reserva['nome']},{reserva['data']},{reserva['sala']},{reserva['acoes']}"
    with open("reservas.csv", "a") as file:
        file.write(linha)
    
def cadastrar_usuario(usuario):
    linha = f"\n{usuario['nome']},{usuario['email']},{usuario['senha']}"
    with open("usuarios.csv", "a") as file:
        file.write(linha)