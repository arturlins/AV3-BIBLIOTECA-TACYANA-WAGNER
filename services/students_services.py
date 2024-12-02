from os import system
from config.db import start_connection
from services.admin_services import list_books
from utils.utils import get_book_id
from datetime import date, datetime, timedelta

#def book_reservation(user):
def book_reservation():
    #max_id = (get_book_id() - 1)
    system('cls')
    list_books()
    while True:
        try:
            book_id = input("Digite o ID do livro a ser reservado: ")
            conn = start_connection()
            cursor = conn.cursor()
            sql = "SELECT quantidade_catalogo, quantidade_reservado, quantidade_locado FROM biblioteca.livros WHERE id_livro = %s"
            cursor.execute(sql, (book_id))
            result = cursor.fetchone()
            #sql2 = "SELECT * FROM biblioteca.reservas WHERE id_aluno = %s"
            sql2 = "SELECT * FROM biblioteca.reservas WHERE id_aluno = 1"
            #cursor.execute(sql, (user[0]))
            cursor.execute(sql2)
            result2 = cursor.fetchall()
            list_reservations = []
            for _, id_livro, _, _, _ in result2:
                list_reservations.append(id_livro)
            #print(list_reservations)
            if book_id in list_reservations:
                print("Você já fez uma reserva desse livro")
            elif result[1] + result [2] >= result[0]:
                print("Livro indisponível para reserva")
            else:
                print("Livro disponível para reserva")
                date_reservation = date.today()
                deadline_reservation = date_reservation + timedelta(days=2)
                sql = "INSERT INTO biblioteca.reservas(id_livro, id_aluno, data_reserva, prazo_reserva) VALUES (%s, '1', %s, %s) RETURNING id_reserva"
                #sql = "INSERT INTO biblioteca.reservas(id_livro, id_aluno, data_reserva, prazo_reserva) VALUES (%s, %s, %s, %s) RETURNING id_reserva"
                cursor.execute(sql, (book_id, date_reservation, deadline_reservation))
                #cursor.execute(sql, (book_id, user[0], date_reservation, deadline_reservation))
                reservation_id = cursor.fetchone()[0]
                sql2 = "UPDATE biblioteca.livros SET quantidade_reservado = quantidade_reservado + 1 WHERE id_livro = %s"
                cursor.execute(sql2, (book_id))
                conn.commit()
                cursor.close()
                conn.close()
                print(f"Reserva efetuada com sucesso. Você tem dois dias para ir buscar o livro na biblioteca | ID da reserva: {reservation_id}")
                break
        except ValueError:
            print("Valor inválido")
        except Exception as reservation_error:
            print(f"Erro ao realizar login: {reservation_error}")

#def list_user_reservations(user):
def list_user_reservations():
    conn = start_connection()
    cursor = conn.cursor()
    #sql = "SELECT id_reserva, titulo_livro, data_reserva, prazo_reserva FROM biblioteca.reservas JOIN biblioteca.livros ON reservas.id_livro = livros.id_livro WHERE id_aluno = %s"
    sql = "SELECT id_reserva, titulo_livro, data_reserva, prazo_reserva FROM biblioteca.reservas JOIN biblioteca.livros ON reservas.id_livro = livros.id_livro WHERE id_aluno = 1"
    cursor.execute(sql)
    #cursor.execute(sql, (user[0]))
    result = cursor.fetchall()
    for id_reserva, titulo_livro, data_reserva, prazo_reserva in result:
        print(f"ID da reserva: {id_reserva}")
        print(f"Título do livro: {titulo_livro}")
        print(f"Data da reserva: {data_reserva}")
        print(f"Prazo em que a reserva estará disponível: {prazo_reserva}")
        print("-------------------------------------------------------------------------------------------------------------\n")
    conn.close()   

#def cancel_book_reservation(user):
def cancel_book_reservation():
    #max_id = (get_book_id() - 1)
    system('cls')
    list_user_reservations()
    while True:
        try:
            reservation_id = input("Digite o ID da reserva a ser cancelada: ")
            conn = start_connection()
            cursor = conn.cursor()
            #sql = "DELETE FROM biblioteca.reservas WHERE id_aluno = %s AND id_reserva = %s"
            sql = "DELETE FROM biblioteca.reservas WHERE id_aluno = 1 AND id_reserva = 1"
            #cursor.execute(sql, (user[0], reservation_id))
            cursor.execute(sql)
            conn.commit()
            conn.close()
            print(f"Reserva de ID {reservation_id} cancelada com sucesso")
            break
        except ValueError:
            print("Valor inválido")
        except Exception as reservation_error:
            print(f"Erro ao cancelar a reserva: {reservation_error}")

# def list_tasks(user_id):
#     conn = start_connection()
#     cursor = conn.cursor()
#     sql = 'SELECT * FROM TASKS WHERE user_id = %s'
#     cursor.execute(sql, [user_id])
#     tasks = cursor.fetchall()
#     return tasks



# def rent_book():
#     max_id = list_books()
#     while True:
#         try:
#             option = int(input("Digite o ID do livro a ser locado"))
#             if option < 0 or option > max_id:
#                 print("Valor inválido")
#             elif option in (1, max_id + 1):
#                 conn = start_connection()
#                 cursor = conn.cursor()
#                 sql = ''
#             elif option not in (1, max_id + 1):
#                 print("Valor inválido")
#         except ValueError:
#             print("Valor inválido")
#         except Exception as rent_error:
#             print(f"Erro ao locar livro: {rent_error}")

# def edit_student_data(name, email, password):
#     while True:
#         try:
#             print('teste')
#         except ValueError:
#             print("Valor inválido")

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