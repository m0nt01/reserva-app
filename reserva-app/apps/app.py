from flask import Flask, render_template
import csv

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