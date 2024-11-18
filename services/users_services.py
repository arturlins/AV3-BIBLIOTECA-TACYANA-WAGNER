from os import system
from config.db import start_connection
from config.security import check_password, encrypt_password
import pwinput

def add_student():
    try:
        registration = input("Digite a matrícula do aluno: ")
        name = input("Digite o nome do aluno: ")
        email = input("Digite o e-mail do aluno: ")
        course = input("Digite o curso do aluno: ")
        password = pwinput.pwinput("Digite a senha do aluno: ")
        hashed_password = encrypt_password(password)
        conn = start_connection()
        cursor = conn.cursor()

        sql = "INSERT INTO alunos (matricula_aluno, nome_aluno, email_aluno, curso_aluno, senha_aluno, privilegio_admin) VALUES (%s, %s, %s, %s, %s, FALSE)"        
        cursor.execute(sql, (registration, name, email, course, hashed_password))
        conn.commit()
        
        system('cls')
        print("Usuário criado com sucesso!")
    except Exception as e:
        print(f"Erro ao criar usuário: {e}")
    finally:
        conn.close()

def login(email, password):
    try:
        conn = start_connection()
        cursor = conn.cursor()

        #sql = "SELECT alunos.email_aluno FROM alunos WHERE alunos.email_aluno = %s";
        sql = "SELECT * FROM alunos WHERE email_aluno = %s"
        cursor.execute(sql, (email,))
        resultado = cursor.fetchone()
        
    except Exception as e:
        print(f"Erro ao realizar login: {e}")
        return False
    finally:
        conn.close()
    if resultado:
        senha_hash = resultado[5]        
        if isinstance(senha_hash, memoryview):
            senha_hash = bytes(senha_hash)

        if check_password(password, senha_hash):
            return resultado 
    return False
