from config.db import start_connection
from config.security import check_password, encrypt_password

def add_student(registration, name, email, course, password):
    
    try:
        hashed_password = encrypt_password(password)
        conn = start_connection()
        cursor = conn.cursor()

        sql = "INSERT INTO alunos (matricula_aluno, nome_aluno, email_aluno, curso_aluno, senha_aluno) VALUES (%s, %s, %s, %s, %s)"        
        cursor.execute(sql, (registration, name, email, course, hashed_password))
        conn.commit()

        print("Usuário criado com sucesso!")
    except Exception as e:
        print(f"Erro ao criar usuário: {e}")
    finally:
        conn.close()

# def login(email, password):
#     try:
#         conn = start_connection()
#         cursor = conn.cursor()

#         sql = "SELECT * FROM usuarios WHERE email = %s"
#         cursor.execute(sql, (email,))
#         resultado = cursor.fetchone()
        
#     except Exception as e:
#         print(f"Erro ao realizar login: {e}")
#         return False
#     finally:
#         conn.close()
#     if resultado:
#         senha_hash = resultado[2]        
#         if isinstance(senha_hash, memoryview):
#             senha_hash = bytes(senha_hash)

#         if check_password(password, senha_hash):
#             return resultado 
#     return False
