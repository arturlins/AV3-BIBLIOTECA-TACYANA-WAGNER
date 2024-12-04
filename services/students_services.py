from os import system
from config.db import start_connection
from services.admin_services import list_books
from utils.utils import get_book_id, get_student_name_by_id, get_student_email_by_id
from datetime import date, datetime, timedelta
import pwinput
from config.security import encrypt_password

def book_reservation(user):
    system('cls')
    list_books() 
    while True:
        try:
            book_id = input("Digite o ID do livro a ser reservado: ")
            if not book_id.isdigit():
                print("Por favor, insira um ID de livro válido.")
                continue            
            book_id = int(book_id)
            conn = start_connection()
            cursor = conn.cursor()
            sql = "SELECT quantidade_catalogo, quantidade_reservado, quantidade_locado FROM biblioteca.livros WHERE id_livro = %s"
            cursor.execute(sql, (book_id,))
            result = cursor.fetchone()
            if result is None:
                print("Livro não encontrado.")
                continue
            sql2 = "SELECT id_livro FROM biblioteca.reservas WHERE id_aluno = %s"
            cursor.execute(sql2, (user[0],))
            result2 = cursor.fetchall()
            list_reservations = [id_book[0] for id_book in result2]
            print(list_reservations)
            if book_id in list_reservations:
                print("Você já fez uma reserva desse livro.")
                break
            elif result[1] + result[2] >= result[0]:
                print("Livro indisponível para reserva.")
            else:
                print("Livro disponível para reserva.")
                date_reservation = date.today()
                deadline_reservation = date_reservation + timedelta(days=2)
                sql3 = "INSERT INTO biblioteca.reservas(id_livro, id_aluno, data_reserva, prazo_reserva) VALUES (%s, %s, %s, %s) RETURNING id_reserva"
                cursor.execute(sql3, (book_id, user[0], date_reservation, deadline_reservation))
                reservation_id = cursor.fetchone()[0]
                sql4 = "UPDATE biblioteca.livros SET quantidade_reservado = quantidade_reservado + 1 WHERE id_livro = %s"
                cursor.execute(sql4, (book_id,))
                conn.commit()
                print(f"Reserva efetuada com sucesso. Você tem dois dias para ir buscar o livro na biblioteca | ID da reserva: {reservation_id}")
                break
        except ValueError:
            print("Valor inválido.")
        except Exception as reservation_error:
            print(f"Erro ao realizar a reserva: {reservation_error}")
        finally:
                conn.close()

def list_user_reservations(user):
#def list_user_reservations():
    conn = start_connection()
    cursor = conn.cursor()
    sql = "SELECT id_reserva, titulo_livro, data_reserva, prazo_reserva FROM biblioteca.reservas JOIN biblioteca.livros ON reservas.id_livro = livros.id_livro WHERE id_aluno = %s"
    #sql = "SELECT id_reserva, titulo_livro, data_reserva, prazo_reserva FROM biblioteca.reservas JOIN biblioteca.livros ON reservas.id_livro = livros.id_livro WHERE id_aluno = 1"
    #cursor.execute(sql)
    cursor.execute(sql, (user[0],))
    result = cursor.fetchall()
    for id_reserva, titulo_livro, data_reserva, prazo_reserva in result:
        print(f"ID da reserva: {id_reserva}")
        print(f"Título do livro: {titulo_livro}")
        print(f"Data da reserva: {data_reserva}")
        print(f"Prazo em que a reserva estará disponível: {prazo_reserva}")
        print("-------------------------------------------------------------------------------------------------------------\n")
    conn.close()   

def cancel_book_reservation(user):
#def cancel_book_reservation():
    #max_id = (get_book_id() - 1)
    system('cls')
    list_user_reservations(user)
    while True:
        try:
            reservation_id = input("Digite o ID da reserva a ser cancelada: ")
            conn = start_connection()
            cursor = conn.cursor()
            sql = "DELETE FROM biblioteca.reservas WHERE id_aluno = %s AND id_reserva = %s"
            #sql = "DELETE FROM biblioteca.reservas WHERE id_aluno = 1 AND id_reserva = 1"
            cursor.execute(sql, (user[0], reservation_id))
            #cursor.execute(sql)
            conn.commit()
            conn.close()
            print(f"Reserva de ID {reservation_id} cancelada com sucesso")
            break
        except ValueError:
            print("Valor inválido")
        except Exception as reservation_error:
            print(f"Erro ao cancelar a reserva: {reservation_error}")

def list_user_rentings(user):
    conn = start_connection()
    cursor = conn.cursor()
    sql = "SELECT id_locacao, titulo_livro, data_emprestimo, prazo_emprestimo_devolucao FROM biblioteca.locacoes JOIN biblioteca.livros ON locacoes.id_livro = livros.id_livro WHERE id_aluno = %s AND status_devolucao = FALSE"
    cursor.execute(sql, (user[0],))
    result = cursor.fetchall()
    for id_locacao, titulo_livro, data_emprestimo, prazo_emprestimo_devolucao in result:
        print(f"ID da reserva: {id_locacao}")
        print(f"Título do livro: {titulo_livro}")
        print(f"Data da reserva: {data_emprestimo}")
        print(f"Prazo em que a reserva estará disponível: {prazo_emprestimo_devolucao}")
        print("-------------------------------------------------------------------------------------------------------------\n")
    conn.close() 

def edit_student_name(user):
#def edit_student_name():
    system('cls')
    while True:
        try:
            id_edit = user[0]
            #id_edit = 1
            current_name = get_student_name_by_id(id_edit)
            new_name = input(f"Digite o novo nome para '{current_name}' (ou aperte enter para cancelar): ")
            if new_name == '':
                break
            else:
                conn = start_connection()
                cursor = conn.cursor()
                sql = "UPDATE biblioteca.alunos SET nome_aluno = %s WHERE alunos.id_aluno = %s"
                #sql = "UPDATE biblioteca.alunos SET nome_aluno = %s WHERE alunos.id_aluno = 1"
                #cursor.execute(sql, [new_name])
                cursor.execute(sql, [new_name, id_edit])
                conn.commit()
                conn.close()
                print(f"Nome do aluno atualizado com sucesso de '{current_name}' para '{new_name}'")
                break
        except (ValueError, AttributeError, TypeError):
            print("Erro")
        except Exception as edit_author_error:
            print(f"Erro ao tentar editar o livro: {edit_author_error}")

def edit_student_email(user):
#def edit_student_email():
    system('cls')
    while True:
        try:
            id_edit = user[0]
            #id_edit = 1
            current_email = get_student_email_by_id(user[0])
            #current_email = get_student_email_by_id(id_edit)
            new_email = input(f"Digite o novo email para '{current_email}' (ou aperte enter para cancelar): ")
            if new_email == '':
                break
            else:
                conn = start_connection()
                cursor = conn.cursor()
                sql = "UPDATE biblioteca.alunos SET email_aluno = %s WHERE alunos.id_aluno = %s"
                #sql = "UPDATE biblioteca.alunos SET email_aluno = %s WHERE alunos.id_aluno = 1"
                #cursor.execute(sql, [new_email])
                cursor.execute(sql, [new_email, id_edit])
                conn.commit()
                conn.close()
                print(f"E-mail do aluno atualizado com sucesso de '{current_email}' para '{new_email}'")
                break
        except (ValueError, AttributeError, TypeError):
            print("Erro")
        except Exception as edit_author_error:
            print(f"Erro ao tentar editar o livro: {edit_author_error}")

def edit_student_password(user):
#def edit_student_password():
    system('cls')
    while True:
        try:
            id_edit = user[0]
            #id_edit = 1
            new_password = pwinput.pwinput(f"Digite a nova senha ou aperte enter para cancelar: ")
            if new_password == '':
                break
            else:
                hashed_password = encrypt_password(new_password)
                conn = start_connection()
                cursor = conn.cursor()
                sql = "UPDATE biblioteca.alunos SET senha_aluno = %s WHERE alunos.id_aluno = %s"
                #sql = "UPDATE biblioteca.alunos SET senha_aluno = %s WHERE alunos.id_aluno = 1"
                #cursor.execute(sql, [hashed_password])
                cursor.execute(sql, [hashed_password, id_edit])
                conn.commit()
                conn.close()
                print(f"Senha atualizada com sucesso")
                break
        except (ValueError, AttributeError, TypeError):
            print("Erro")
        except Exception as edit_password_error:
            print(f"Erro ao tentar editar o livro: {edit_password_error}")