from flask import Flask, render_template, request, redirect, url_for
import bisect

app = Flask("Reserva App")

# Dados fictícios de usuários e salas
usuarios = [{"id": 1, "nome": "usuario 1"}, {"id": 2, "nome": "usuario 2"}, {"id": 3, "nome": "usuario 3"}]
salas = [{"id": 1, "nome": "Sala 1"}, {"id": 2, "nome": "Sala 2"}, {"id": 3, "nome": "Sala 3"}]

# Página principal
@app.route("/")
def principal():
    return render_template("principal.html")

# Página de cadastro de usuários
@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        novo_id = len(usuarios) + 1
        nome = request.form["nome"]
        usuarios.append({"id": novo_id, "nome": nome})
        return redirect(url_for("listar_usuarios"))
    return render_template("cadastro.html")

# Página para listar usuários cadastrados
@app.route("/usuarios")
def listar_usuarios():
    return render_template("usuarios.html", usuarios=usuarios)

# Página para listar salas disponíveis
@app.route("/salas")
def listar_salas():
    return render_template("salas.html", salas=salas)

# Busca de usuários utilizando busca binária
@app.route("/search_user/<int:usuario_id>")
def search_user(usuario_id):
    index = bisect.bisect_left([user["id"] for user in usuarios], usuario_id)
    if index != len(usuarios) and usuarios[index]["id"] == usuario_id:
        return render_template("usuario_perfil.html", user=usuarios[index])
    else:
        return "Usuário não encontrado", 404

# Busca de salas utilizando busca binária
@app.route("/procurar_sala/<int:sala_id>")
def procurar_sala(sala_id):
    index = bisect.bisect_left([sala["id"] for sala in salas], sala_id)
    if index != len(salas) and salas[index]["id"] == sala_id:
        return render_template("sala_perfil.html", sala=salas[index])
    else:
        return "Sala não encontrada", 404

if __name__ == "__main__":
    app.run(debug=True)
