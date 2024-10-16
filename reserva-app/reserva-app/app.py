from flask import Flask, render_template, request, redirect, url_for
from conexao_bd import conexao_abrir, conexao_fechar

app = Flask(__name__)

# Conectar ao banco de dados
def conectar_bd():
    return conexao_abrir("localhost", "root", "", "reservas")

@app.route("/")
def home(): 
    return render_template('home.html')

@app.route("/cadastrar-sala", methods=["GET", "POST"])
def cadastrarSala(): 
    if request.method == "POST":
        tipo = request.form['tipo']
        capacidade = request.form['capacidade']
        descricao = request.form['descricao']

        con = conectar_bd()
        cursor = con.cursor()
        cursor.execute("INSERT INTO salas (tipo, capacidade, descricao) VALUES (%s, %s, %s)", (tipo, capacidade, descricao))
        con.commit()
        cursor.close()
        conexao_fechar(con)

        return redirect(url_for("listarSalas"))

    return render_template("/cadastrar-sala.html")

@app.route("/salas")
def listarSalas(): 
    con = conectar_bd()
    cursor = con.cursor(dictionary=True)
    cursor.execute("SELECT * FROM salas")
    salas = cursor.fetchall()
    cursor.close()
    conexao_fechar(con)
    
    return render_template("/salas.html", salas=salas)

@app.route("/principal")
def Principal(): 
    return render_template("/principal.html")

@app.route("/reservas", methods=["GET", "POST"])
def Reservas(): 
    if request.method == "POST":
        nome = request.form['nome']
        sala_id = request.form['sala_id']
        inicio = request.form['inicio']
        fim = request.form['fim']

        con = conectar_bd()
        cursor = con.cursor()
        cursor.execute("INSERT INTO reservas (nome, sala_id, inicio, fim) VALUES (%s, %s, %s, %s)", (nome, sala_id, inicio, fim))
        con.commit()
        cursor.close()
        conexao_fechar(con)

        return redirect(url_for("Reservas"))

    return render_template("/reservas.html")

@app.route("/usuarios", methods=["GET", "POST"])
def Usuario(): 
    if request.method == "POST":
        email = request.form['email']
        senha = request.form['senha']

        con = conectar_bd()
        cursor = con.cursor()
        cursor.execute("INSERT INTO usuario (login, senha) VALUES (%s, %s)", (email, senha))
        con.commit()
        cursor.close()
        conexao_fechar(con)

        return redirect(url_for("principal"))

    return render_template("/usuarios.html")

@app.route("/cadastro")
def Cadastro(): 
    return render_template("/cadastro.html")

@app.route("/login")
def Login(): 
    return render_template("/login.html")

if __name__ == "__main__":
    app.run(port=5001)
