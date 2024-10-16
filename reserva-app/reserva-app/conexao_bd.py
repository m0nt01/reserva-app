import mysql.connector

def conexao_abrir(host, user, password, database):
    return mysql.connector.connect(
        host= "localhost",
        user= "root",
        password= "aluno",
        database= "reservas_db"
    )
#Vamos fazer em sala o Banco de Dados :)
def conexao_fechar(con):
    con.close()
