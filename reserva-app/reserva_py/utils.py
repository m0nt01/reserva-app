import csv

def obter_salas():
    with open("salas.csv", "r") as file:
        lista_salas = []
        reader = csv.DictReader(file)
        for row in reader:
            sala = {
                "id": row['id'],
                "tipo": row['tipo'],
                "descricao": row['descricao'],
                "capacidade": int(row['capacidade']),
            }
            lista_salas.append(sala)
        return lista_salas
    
def cadastrar_sala(sala):
    with open("salas.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([sala['id'], sala['tipo'], sala['descricao'], sala['capacidade']])
        
def cadastrar_usuario(usuario):
    with open("usuarios.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([usuario['nome'], usuario['email'], usuario['senha']])

# Todas as funções que manipulam os arquivos csv foram movidas para este arqv para tentar organizar :/ 