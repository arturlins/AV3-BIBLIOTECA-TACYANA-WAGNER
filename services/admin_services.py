from config.db import start_connection
from config.security import check_password, encrypt_password
import pwinput

def add_admin(registration, name, email, password):
    try:
        hashed_password = encrypt_password(password)
        conn = start_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO administradores (matricula_administrador, nome_administrador, email_administrador, senha_administrador) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (registration, name, email, hashed_password))
        conn.commit()
        print("Administrador adicionado com sucesso!")
    except Exception as e:
        print(f"Erro ao adicionar o administrador: {e}")
    finally:
        conn.close()

# def create_task(user_id, title):
#     conn = criar_conexao()
#     cursor = conn.cursor()
#     sql = 'INSERT INTO TASKS (title, user_id) VALUES (%s, %s)'
#     cursor.execute(sql, [title, user_id])
#     conn.commit()


# def list_tasks(user_id):
#     conn = criar_conexao()
#     cursor = conn.cursor()
#     sql = 'SELECT * FROM TASKS WHERE user_id = %s'
#     cursor.execute(sql, [user_id])
#     tasks = cursor.fetchall()
#     return tasks

# def delete_task(user_id, task_id):
#     conn = criar_conexao()
#     cursor = conn.cursor()
#     sql = 'DELETE FROM TASKS WHERE user_id = %s AND id = %s'
#     cursor.execute(sql, [user_id, task_id])
#     conn.commit()
#     # return cursor.rowcount


# def update_task(user_id, task_id, title):
#     conn = criar_conexao()
#     cursor = conn.cursor()
#     sql = 'UPDATE TASKS SET title = %s WHERE user_id = %s AND id = %s'
#     cursor.execute(sql, [title, user_id, task_id])
#     conn.commit()
#     # return cursor.rowcount