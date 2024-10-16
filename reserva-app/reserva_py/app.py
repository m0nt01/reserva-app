from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
# tem que instalar o Sql Alchemy
app = Flask(__name__)

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reserva.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelos do banco de dados
class Sala(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(200), nullable=False)
    capacidade = db.Column(db.Integer, nullable=False)

class Reserva(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    data = db.Column(db.String(100), nullable=False)
    sala_id = db.Column(db.Integer, db.ForeignKey('sala.id'), nullable=False)
    acoes = db.Column(db.String(100), nullable=False)

# Inicializando o banco de dados
with app.app_context():
    db.create_all()

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para a página de cadastro de salas
@app.route('/cadastrar-sala', methods=['GET', 'POST'])
def cadastrar_sala_route():
    if request.method == 'POST':
        sala = Sala(
            tipo=request.form['tipo'],
            descricao=request.form['descricao'],
            capacidade=request.form['capacidade']
        )
        db.session.add(sala)
        db.session.commit()
        return render_template('cadastrar-sala.html', sucesso=True)
    return render_template('cadastrar-sala.html')

# Rota para a página de reserva de salas
@app.route('/reservar-sala', methods=['GET', 'POST'])
def reservar_sala():
    if request.method == 'POST':
        reserva = Reserva(
            nome=request.form['nome'],
            data=request.form['data'],
            sala_id=request.form['sala'],
            acoes=request.form['acoes']
        )
        db.session.add(reserva)
        db.session.commit()
        return render_template('reservar-sala.html', sucesso=True)
    return render_template('reservar-sala.html')

if __name__ == '__main__':
    app.run(debug=True)
