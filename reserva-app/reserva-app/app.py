from flask import Flask , render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home(): 
    return render_template('home.html')

@app.route("/cadastrar-sala")
def cadastrarSala(): 
    return render_template("/cadastrar-sala.html")

@app.route("/salas")
def Salas(): 
    return render_template("/salas.html", sala = cadastrar_sala())

@app.route("/principal")
def Principal(): 
    return render_template("/principal.html")

@app.route("/reservas")
def Reservas(): 
    return render_template("/reservas.html", reserva = reservar_sala())

@app.route("/reservar-sala")
def ReservarSala(): 
    return render_template("/reservar-sala.html")

@app.route("/usuarios")
def Usuario(): 
    return render_template("/usuarios.html", user = cadastrar_usuario())

@app.route("/cadastro")
def Cadastro(): 
    return render_template("/cadastro.html")

@app.route("/listar-salas")
def ListarSalas(): 
    return render_template("/listar-salas.html")

@app.route("/login")
def Login(): 
    return render_template("/login.html")

# Fazer método GET do Login

@app.route("/cadastro", methods=["POST"])
def cadastrar_usuario():
   with open("usuarios.csv", 'r') as file:
    lista_usuarios = []
    for linha in file:
        email, senha = linha.split(",")
        usuario = {
            "email": email,
            "senha": senha
        }
        lista_usuarios.append(usuario)
    return redirect(url_for("principal"))

@app.route("/cadastrar-sala", methods=["POST"])
def cadastrar_sala():
   with open("salas.csv", 'r') as file:
    lista_salas = []
    for linha in file:
        tipo, capacidade, descricao = linha.split(",")
        sala = {
            "tipo": tipo,
            "capacidade": int(capacidade),
            "descricao": descricao
        }
        lista_salas.append(sala)
    return redirect(url_for("salas"))
   
@app.route("/reservar-sala", methods=["POST"])
def reservar_sala():
   with open("salasReservadas.csv", 'r') as file:
    lista_salas_reservadas = []
    for linha in file:
        sala, inicio, fim = linha.split(",")
        salaReservada = {
            "sala": sala,
            "inicio": inicio,
            "fim": fim
        }
        lista_salas_reservadas.append(salaReservada)
    return redirect(url_for("reservas"))


app.run(port=5001)