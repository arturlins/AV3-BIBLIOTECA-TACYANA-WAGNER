from os import system
import psycopg2.extras
from config.db import start_connection
from config.security import check_password, encrypt_password
from utils.utils import get_book_id, get_author_id, get_category_id, get_publisher_id, list_books, list_books_authors_only, list_all_book_authors, list_books_simpler, list_book_publisher, list_book_category, get_title_by_id, get_quantity_by_id, get_author_by_id, get_worker_name_by_id, get_worker_email_by_id
import pwinput
from datetime import date, timedelta

def add_admin(registration, name, email, password):
    try:
        hashed_password = encrypt_password(password)
        conn = start_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO biblioteca.funcionarios (matricula_funcionario, nome_funcionario, email_funcionario, senha_funcionario) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (registration, name, email, hashed_password))
        conn.commit()
        system('cls')
        print("Administrador adicionado com sucesso!")
    except Exception as error_admin:
        print(f"Erro ao adicionar o administrador: {error_admin}")
    finally:
        conn.close()

def add_book_author():
    list_all_book_authors()
    while True:
        try:
            author_name = input("Digite o nome do novo autor: ")
            conn = start_connection()
            cursor = conn.cursor()
            sql = "INSERT INTO biblioteca.autores(nome_autor) VALUES (%s)"
            cursor.execute(sql, [author_name])
            conn.commit()
            conn.close()
            print(f"Autor '{author_name}' adicionado com sucesso!")
            break
        except ValueError:
            print("Valor inválido")
        except Exception as author_error:
            print(f"Erro ao tentar adicionar o autor: {author_error}")

def remove_book_author():
    max_id = get_author_id() - 1
    while True:
        try:
            id_delete = int(input("Digite o ID do autor que você quer remover ou digite 0 para cancelar: "))
            if id_delete < 0 or id_delete > max_id:
                print("Valor inválido")
            elif id_delete == 0:
                break
            elif id_delete in range (1, max_id + 1):
                conn = start_connection()
                cursor = conn.cursor()
                sql = "DELETE FROM biblioteca.autores WHERE id_autor = %s"
                cursor.execute(sql, [id_delete])
                conn.commit()
                conn.close()
                print("Autor removido com sucesso")
                break
            elif id_delete not in range (1, max_id + 1):
                print("Valor inválido")
        except ValueError:
            print("Valor inválido")
        except Exception as remove_author_error:
            print(f"Erro ao tentar remover o autor: {remove_author_error}")

def add_new_category():
    while True:
        try:
            category = input("Digite o nome da nova categoria: ")
            if category == '':
                system('cls')
                print("É obrigatório informar o nome da categoria")
            else:
                conn = start_connection()
                cursor = conn.cursor()
                sql = "INSERT INTO biblioteca.categorias(nome_categoria) VALUES (%s)"
                cursor.execute(sql, [category])
                conn.commit()
                conn.close()
                break
        except:
            print("Erro ao tentar adicionar uma nova categoria")

#def add_new_book(user):
def add_new_book():
    next = 0
    authors = []
    while next == 0:
        while True:
            try:
                counter = get_author_id()
                system('cls')
                max_author = int(input("Quantos autores escreveram o livro a ser cadastrado?: "))
                list_all_book_authors()
                if max_author == 1:
                    try:
                        id_author = int(input(f"Digite o ID do autor ou digite {counter} para adicionar um novo: "))
                        if id_author <= 0 or id_author > counter:
                                print("Valor inválido")
                        elif id_author == counter:
                            authors.append(id_author)
                            add_book_author()                                   
                            next = 1
                            break
                        elif id_author in range(1, (counter + 1)):
                            authors.append(id_author)
                            next = 1
                            break
                    except ValueError:
                        print("Valor inválido")
                        system('cls')
                elif max_author > 1:
                    for i in range(1, max_author + 1):
                        try:                            
                            id_author = int(input(f"Digite o ID do autor {i}/{max_author} ou digite {counter} para adicionar um novo: "))
                            if id_author <= 0 or id_author > counter:
                                print("Valor inválido")
                            elif id_author == counter:
                                add_book_author()   
                                authors.append(id_author)
                                counter += 1
                            elif id_author in range(1, (counter + 1)):
                                authors.append(id_author)
                        except ValueError:
                            print("Valor inválido")
                    break
                elif max_author <= 0:
                    system('cls')
                    print("Valor inválido")
            except ValueError:
                system('cls')
                print("Valor inválido")
            except Exception as author_error:
                print(f"Erro ao tentar adicionar o autor: {author_error}")
        next = 1
        break
    
    system('cls')
    while next == 1:
        try:
            book_title = input(f"Digite o título do livro: ")
            if book_title == '':
                system('cls')
                print("É obrigatório informar o título do livro")
            else:
                next = 2
                break
        except Exception as title_error:
            print(f"Erro ao tentar adicionar o livro: {title_error}")

    system('cls')
    counter = get_publisher_id()
    system('cls')
    list_book_publisher()
    while next == 2:
        try:
            id_publisher = int(input(f"Digite o ID da editora ou digite {counter} para adicionar uma nova: "))
            if id_publisher <= 0 or id_publisher > counter:
                print("Valor inválido")
            elif id_publisher == counter:
                publisher_name = input("Digite o nome da editora: ")
                if publisher_name == '':
                    print("É obrigatório informar o nome da editora")
                else:
                    system('cls')
                    publisher_location = input("Digite o local da editora (ou aperte enter para deixar em branco): ")
                    conn = start_connection()
                    cursor = conn.cursor()
                    sql = "INSERT INTO biblioteca.editoras(nome_editora, local_editora) VALUES (%s, %s)"
                    cursor.execute(sql, [publisher_name, publisher_location])
                    conn.commit()
                    conn.close()
                    next = 3
                    break
            elif id_publisher in range(1, (counter + 1)):
                next = 3
                break
        except ValueError:
            print("Valor inválido")
        except Exception as publisher_error:
            print(f"Erro ao tentar adicionar a editora: {publisher_error}")
    
    system('cls')
    while next == 3:
        try:
            book_isbn = input(f"Digite o ISBN do livro (ou aperte enter para deixar em branco): ")
            next = 4
            break
        except Exception as isbn_error:
            print(f"Erro ao tentar adicionar o ISBN do livro: {isbn_error}")

    system('cls')
    while next == 4:
        try:
            book_year = input(f"Digite o ano da edição do livro (ou aperte enter para deixar em branco): ")
            next = 5
            break
        except Exception as year_error:
            print(f"Erro ao tentar adicionar o ano da edição do livro: {year_error}")

    system('cls')
    while next == 5:
        try:
            book_language = input(f"Digite o idioma em que o livro foi publicado (ou aperte enter para deixar em branco): ")
            next = 6
            break
        except Exception as language_error:
            print(f"Erro ao tentar adicionar o ISBN do livro: {language_error}")

    system('cls')
    counter = get_category_id()
    system('cls')
    list_book_category()
    while next == 6:
        try:
            id_category = int(input(f"Digite o ID da categoria ou digite {counter} para adicionar uma nova: "))
            if id_category <= 0 or id_category > counter:
                print("Valor inválido")
            elif id_category == counter:
                add_new_category()
                next = 7
                break
            elif id_category in range(1, (counter + 1)):
                next = 7
                break
        except ValueError:
            print("Valor inválido")
        except Exception as category_error:
            print(f"Erro ao tentar adicionar a categoria: {category_error}")
        
    system('cls')
    current_book_id = get_book_id()
    system('cls')
    while next == 7:
        try:
            book_quantity = int(input(f"Digite a quantidade de volumes a serem disponibilizados: "))
            if book_quantity == '' or book_quantity <= 0:
                system('cls')
                print("É preciso informar um valor que seja maior que zero")
            else:
                conn = start_connection()
                cursor = conn.cursor()
                sql = "INSERT INTO biblioteca.livros(titulo_livro, id_editora, isbn_livro, ano_livro, idioma_livro, id_categoria, quantidade_catalogo, id_funcionario, quantidade_reservado, quantidade_locado) VALUES (%s, %s, %s, %s, %s, %s, %s, 1, 0, 0)"
                #sql = "INSERT INTO biblioteca.livros(titulo_livro, id_editora, isbn_livro, ano_livro, idioma_livro, id_categoria, quantidade_catalogo, id_funcionario, quantidade_reservado, quantidade_locado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, 0, 0)"
                #cursor.execute(sql, [id_author, book_title, id_publisher, book_isbn, book_year, book_language, id_category, book_quantity, user[0]])
                cursor.execute(sql, [book_title, id_publisher, book_isbn, book_year, book_language, id_category, book_quantity])
                conn.commit()
                conn.close()
                index = 0
                author_index = authors[index]
                for i in range(max_author):
                    conn = start_connection()
                    cursor = conn.cursor()
                    sql = "INSERT INTO biblioteca.autores_do_livro(id_livro, id_autor) VALUES (%s, %s)"
                    cursor.execute(sql, [current_book_id, author_index])
                    conn.commit()
                    conn.close()
                    index += 1
                system('cls')
                print("Livro adicionado com sucesso")
                break
        except ValueError:
            system('cls')
            print("Valor inválido")
        except Exception as quantity_error:
            print(f"Erro ao tentar adicionar a quantidade de volumes disponíveis: {quantity_error}")

def remove_book():
    max_id = get_book_id()
    system('cls')
    list_books_simpler()
    while True:
        try:
            id_delete = int(input("Digite o ID do livro que você quer remover do banco de dados: "))
            if id_delete < 0 or id_delete > max_id:
                print("Valor inválido")
            elif id_delete in range (1, max_id + 1):
                conn = start_connection()
                cursor = conn.cursor()
                sql_fk = "DELETE FROM biblioteca.autores_do_livro WHERE autores_do_livro.id_livro = %s"
                cursor.execute(sql_fk, [id_delete])
                sql = "DELETE FROM biblioteca.livros WHERE livros.id_livro = %s"
                cursor.execute(sql, [id_delete])
                conn.commit()
                conn.close()
                print("Livro removido com sucesso")
                break
            elif id_delete not in range (1, max_id + 1):
                print("Valor inválido")
        except ValueError:
            print("Valor inválido")
        except Exception as remove_book_error:
            print(f"Erro ao tentar remover o livro: {remove_book_error}")

def edit_books_titles():
    max_id = int(get_book_id() - 1)
    system('cls')
    list_books_simpler()
    while True:
        try:
            id_edit = int(input("Digite o ID do livro que você quer editar: "))
            current_title = get_title_by_id(id_edit)
            if id_edit < 0 or id_edit > max_id:
                print("Valor inválido")
            elif id_edit in range (1, max_id + 1):
                new_title = input(f"Digite o novo título para '{current_title}': ")
                conn = start_connection()
                cursor = conn.cursor()
                sql = "UPDATE biblioteca.livros SET titulo_livro = %s WHERE id_livro = %s"
                cursor.execute(sql, [new_title, id_edit])
                conn.commit()
                conn.close()
                print(f"Título do livro editado com sucesso de '{current_title}' para '{new_title}'")
                break
            elif id_edit not in range (1, max_id + 1):
                print("ID inexistente")
        except (ValueError, AttributeError, TypeError):
            print("ID inexistente")
        except Exception as edit_book_error:
            print(f"Erro ao tentar editar o livro: {edit_book_error}")

def edit_books_authors():
    max_id = int(get_author_id() - 1)
    system('cls')
    list_all_book_authors()
    while True:
        try:
            id_edit = int(input("Digite o ID do autor que você quer editar: "))
            current_name = get_author_by_id(id_edit)
            if id_edit < 0 or id_edit > max_id:
                print("Valor inválido")
            elif id_edit in range (1, max_id + 1):
                new_name = input(f"Digite o novo título para '{current_name}': ")
                conn = start_connection()
                cursor = conn.cursor()
                sql = "UPDATE biblioteca.autores SET nome_autor = %s WHERE autores.id_autor = %s"
                cursor.execute(sql, [new_name, id_edit])
                conn.commit()
                conn.close()
                print(f"Nome do autor editado com sucesso de '{current_name}' para '{new_name}'")
                break
            elif id_edit not in range (1, max_id + 1):
                print("ID inexistente")
        except (ValueError, AttributeError, TypeError):
            print("ID inexistente")
        except Exception as edit_author_error:
            print(f"Erro ao tentar editar o livro: {edit_author_error}")

def remove_author():
    max_id = get_author_id()
    system('cls')
    list_all_book_authors()
    while True:
        try:
            id_delete = int(input("Digite o ID do autor a ser excluído: "))
            if id_delete < 0 or id_delete > max_id:
                print("Valor inválido")
            elif id_delete in range (1, max_id + 1):
                conn = start_connection()
                cursor = conn.cursor()
                sql_fk = "DELETE FROM biblioteca.autores_do_livro WHERE autores_do_livro.id_autor = %s"
                cursor.execute(sql_fk, [id_delete])
                sql = "DELETE FROM biblioteca.autores WHERE id_autor = %s"
                cursor.execute(sql, [id_delete])
                conn.commit()
                conn.close()
                print("Autor removido com sucesso")
                break
            elif id_delete not in range (1, max_id + 1):
                print("Valor inválido")
        except ValueError:
            print("Valor inválido")
        except Exception as remove_author_error:
            print(f"Erro ao tentar remover o livro: {remove_author_error}")

def edit_books_quantities():
    max_id = int(get_book_id() - 1)
    system('cls')
    list_books()
    while True:
        try:
            id_edit = int(input("Digite o ID do livro que você quer modificar a quantidade no catálogo: "))
            current_quantity = get_quantity_by_id(id_edit)
            if id_edit < 0 or id_edit > max_id:
                print("Valor inválido")
            elif id_edit in range (1, max_id + 1):
                new_quantity = input(f"Digite a nova quantidade, atualmente em '{current_quantity}': ")
                conn = start_connection()
                cursor = conn.cursor()
                sql = "UPDATE biblioteca.livros SET quantidade_catalogo = %s WHERE id_livro = %s"
                cursor.execute(sql, [new_quantity, id_edit])
                conn.commit()
                conn.close()
                print(f"Quantidade editada com sucesso de '{current_quantity}' para '{new_quantity}'")
                break
            elif id_edit not in range (1, max_id + 1):
                print("ID inexistente")
        except (ValueError, AttributeError, TypeError):
            print("ID inexistente")
        except Exception as edit_book_error:
            print(f"Erro ao tentar editar a quantidade: {edit_book_error}")

#def edit_worker_name(user):
def edit_worker_name():
    system('cls')
    while True:
        try:
            #id_edit = user[0]
            id_edit = 1
            current_name = get_worker_name_by_id(id_edit)
            new_name = input(f"Digite o novo nome para '{current_name}' (ou aperte enter para cancelar): ")
            if new_name == '':
                break
            else:
                conn = start_connection()
                cursor = conn.cursor()
                #sql = "UPDATE biblioteca.funcionarios SET nome_funcionario = %s WHERE funcionarios.id_funcionario = %s"
                sql = "UPDATE biblioteca.funcionarios SET nome_funcionario = %s WHERE funcionarios.id_funcionario = 1"
                cursor.execute(sql, [new_name])
                #cursor.execute(sql, [new_name, id_edit])
                conn.commit()
                conn.close()
                print(f"Nome atualizado com sucesso de '{current_name}' para '{new_name}'")
                break
        except (ValueError, AttributeError, TypeError):
            print("Erro")
        except Exception as edit_author_error:
            print(f"Erro ao tentar editar o nome: {edit_author_error}")

#def edit_worker_email(user):
def edit_worker_email():
    system('cls')
    while True:
        try:
            #id_edit = user[0]
            id_edit = 1
            current_email = get_worker_email_by_id(id_edit)
            new_email = input(f"Digite o novo email para '{current_email}' (ou aperte enter para cancelar): ")
            if new_email == '':
                break
            else:
                conn = start_connection()
                cursor = conn.cursor()
                #sql = "UPDATE biblioteca.funcionarios SET email_funcionario = %s WHERE funcionarios.id_funcionario = %s"
                sql = "UPDATE biblioteca.funcionarios SET email_funcionario = %s WHERE funcionarios.id_funcionario = 1"
                cursor.execute(sql, [new_email])
                #cursor.execute(sql, [new_email, id_edit])
                conn.commit()
                conn.close()
                print(f"E-mail atualizado com sucesso de '{current_email}' para '{new_email}'")
                break
        except (ValueError, AttributeError, TypeError):
            print("Erro")
        except Exception as edit_email_error:
            print(f"Erro ao tentar editar o e-mail: {edit_email_error}")

#def edit_worker_password(user):
def edit_worker_password():
    system('cls')
    while True:
        try:
            #id_edit = user[0]
            id_edit = 1
            new_password = pwinput.pwinput(f"Digite a nova senha ou aperte enter para cancelar: ")
            if new_password == '':
                break
            else:
                hashed_password = encrypt_password(new_password)
                conn = start_connection()
                cursor = conn.cursor()
                #sql = "UPDATE biblioteca.funcionarios SET senha_funcionario = %s WHERE funcionarios.id_funcionario = %s"
                sql = "UPDATE biblioteca.funcionarios SET senha_funcionario = %s WHERE funcionarios.id_funcionario = 1"
                cursor.execute(sql, [hashed_password])
                #cursor.execute(sql, [hashed_password, id_edit])
                conn.commit()
                conn.close()
                print(f"Senha atualizada com sucesso")
                break
        except (ValueError, AttributeError, TypeError):
            print("Erro")
        except Exception as edit_password_error:
            print(f"Erro ao tentar editar o livro: {edit_password_error}")

def book_rent():
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