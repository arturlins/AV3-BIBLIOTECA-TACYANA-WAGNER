from config.db import start_connection
from services.admin_services import list_books
from datetime import date

def rent_book():
    max_id = list_books()
    while True:
        try:
            option = int(input("Digite o ID do livro a ser locado"))
            if option < 0 or option > max_id:
                print("Valor inválido")
            elif option in (1, max_id + 1):
                conn = start_connection()
                cursor = conn.cursor()
                sql = ''
            elif option not in (1, max_id + 1):
                print("Valor inválido")
        except ValueError:
            print("Valor inválido")
        except Exception as rent_error:
            print(f"Erro ao locar livro: {rent_error}")

def edit_student_data(name, email, password):
    while True:
        try:
            print('teste')
        except ValueError:
            print("Valor inválido")

# def edit_student_data():
#     while True:
#         try:
#             conn = start_connection()
#             cursor = conn.cursor()
#             registration = input("Matrícula do aluno: ")
#             cursor.execute("SELECT * FROM alunos WHERE matricula_aluno = %s", (registration,))
#             student = cursor.fetchone()
#             if student:
#                 name = input("Novo nome (Enter para manter): ") or student[1]
#                 email = input("Novo e-mail (Enter para manter): ") or student[2]
#                 course = input("Novo curso (Enter para manter): ") or student[3]
#                 cursor.execute(
#                     "UPDATE alunos SET nome_aluno = %s, email_aluno = %s, curso_aluno = %s WHERE matricula_aluno = %s",
#                     (name, email, course, registration)
#                 conn.commit()
#                 print("Aluno atualizado.")
#             else:
#                 print("Aluno não encontrado.")
#         except ValueError:
#             print("Valor inválido")

# def create_task(user_id, title):
#     conn = start_connection()
#     cursor = conn.cursor()
#     sql = 'INSERT INTO TASKS (title, user_id) VALUES (%s, %s)'
#     cursor.execute(sql, [title, user_id])
#     conn.commit()


# def list_tasks(user_id):
#     conn = start_connection()
#     cursor = conn.cursor()
#     sql = 'SELECT * FROM TASKS WHERE user_id = %s'
#     cursor.execute(sql, [user_id])
#     tasks = cursor.fetchall()
#     return tasks

# def delete_task(user_id, task_id):
#     conn = start_connection()
#     cursor = conn.cursor()
#     sql = 'DELETE FROM TASKS WHERE user_id = %s AND id = %s'
#     cursor.execute(sql, [user_id, task_id])
#     conn.commit()
#     # return cursor.rowcount


# def update_task(user_id, task_id, title):
#     conn = start_connection()
#     cursor = conn.cursor()
#     sql = 'UPDATE TASKS SET title = %s WHERE user_id = %s AND id = %s'
#     cursor.execute(sql, [title, user_id, task_id])
#     conn.commit()
#     # return cursor.rowcount