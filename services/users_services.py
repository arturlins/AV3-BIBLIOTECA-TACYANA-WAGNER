from os import system
from config.db import start_connection
from config.security import check_password, encrypt_password
import pwinput

def add_student():
    try:
        registration = input("Digite a matrícula do aluno: ")
        system('cls')
        name = input("Digite o nome do aluno: ")
        system('cls')
        email = input("Digite o e-mail do aluno: ")
        system('cls')
        course = input("Digite o curso do aluno: ")
        system('cls')
        password = pwinput.pwinput("Digite a senha do aluno: ")
        hashed_password = encrypt_password(password)
        conn = start_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO biblioteca.alunos (matricula_aluno, nome_aluno, email_aluno, curso_aluno, reservas, emprestimos, senha_aluno) VALUES (%s, %s, %s, %s, 0, 0, %s)"        
        cursor.execute(sql, (registration, name, email, course, hashed_password))
        conn.commit()
        system('cls')
        print("Usuário criado com sucesso!")
    except Exception as add_error:
        print(f"Erro ao criar usuário: {add_error}")
    finally:
        conn.close()

def login_student(email, password):
    try:
        conn = start_connection()
        cursor = conn.cursor()
        sql = "SELECT * FROM biblioteca.alunos WHERE email_aluno = %s"
        cursor.execute(sql, (email,))
        result = cursor.fetchone()
    except Exception as login_error:
        print(f"Erro ao realizar login: {login_error}")
        return False
    finally:
        conn.close()
    if result:
        hash_password = result[7]        
        if isinstance(hash_password, memoryview):
            hash_password = bytes(hash_password)
        if check_password(password, hash_password):
            return result
    return False

def login_worker(email, password):
    try:
        conn = start_connection()
        cursor = conn.cursor()
        sql = "SELECT * FROM biblioteca.funcionarios WHERE email_funcionario = %s"
        cursor.execute(sql, (email,))
        result = cursor.fetchone()
    except Exception as login_error:
        print(f"Erro ao realizar login: {login_error}")
        return False
    finally:
        conn.close()
    if result:
        hash_password = result[4]        
        if isinstance(hash_password, memoryview):
            hash_password = bytes(hash_password)
        if check_password(password, hash_password):
            return result
    return False