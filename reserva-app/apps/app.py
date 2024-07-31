from flask import Flask, render_template

app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para a página de login
@app.route('/login')
def login():
    return render_template('login.html')

# Rota para a página de cadastro
@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

# Rota para a página de cadastro de salas
@app.route('/cadastrar-sala')
def cadastrar_sala():
    return render_template('cadastrar-sala.html')

# Rota para a página de listagem de salas
@app.route('/listar-salas')
def listar_salas():
    return render_template('listar-salas.html')

# Rota para a página de reserva de salas
@app.route('/reservar-sala')
def reservar_sala():
    return render_template('reservar-sala.html')

# Rota para a página de listagem de reservas
@app.route('/reservas')
def reservas():
    return render_template('reservas.html')

if __name__ == '__main__':
    app.run(debug=True)