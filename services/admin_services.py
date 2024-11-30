from os import system
from config.db import start_connection
from config.security import check_password, encrypt_password

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

def get_book_id():
    conn = start_connection()
    cursor = conn.cursor()
    sql = "SELECT * FROM biblioteca.livros"
    cursor.execute(sql)
    result = cursor.fetchall()
    max_id = []
    for id_livro, _, _, _, _, _, _, _, _, _, _, _ in result:
        max_id.append(id_livro)
    max_id.sort()
    conn.close()
    if max_id:
        return max_id[-1]
    else:
        return 0
    

def list_books():
    conn = start_connection()
    cursor = conn.cursor()
    sql = "SELECT id_livro, titulo_livro, nome_autor, nome_editora, nome_categoria, ano_livro, idioma_livro, isbn_livro, quantidade_catalogo, quantidade_reservado, quantidade_locado from biblioteca.livros JOIN biblioteca.autores ON livros.id_autor = autores.id_autor JOIN biblioteca.editoras ON livros.id_editora = editoras.id_editora JOIN biblioteca.categorias ON livros.id_categoria = categorias.id_categoria ORDER BY biblioteca.livros.titulo_livro"
    cursor.execute(sql)
    result = cursor.fetchall()
    print("Lista de todos os livros cadastrados (em ordem alfabética): ")
    max_id = []
    for id_livro, titulo_livro, nome_autor, nome_editora, nome_categoria, ano_livro, idioma_livro, isbn_livro, quantidade_catalogo, quantidade_reservado, quantidade_locado in result:
        max_id.append(id_livro)
        print(f"- TÍTULO: {titulo_livro}")
        print(f"- AUTOR: {nome_autor}")
        print(f"- ID DO LIVRO: {id_livro}")
        print(f"- EDITORA: {nome_editora}")
        print(f"- CATEGORIA: {nome_categoria}")
        print(f"- ANO DA EDIÇÃO: {ano_livro}")
        print(f"- IDIOMA DO LIVRO: {idioma_livro}")
        print(f"- ISBN DO LIVRO: {isbn_livro}")
        print(f"- QUANTIDADE DE VOLUMES NO CATÁLOGO: {quantidade_catalogo}")
        print(f"- QUANTIDADE DE VOLUMES RESERVADOS: {quantidade_reservado}")
        print(f"- QUANTIDADE DE VOLUMES LOCADOS: {quantidade_locado}")
        print(f"- QUANTIDADE DE VOLUMES DISPONÍVEIS PARA RESERVA: {quantidade_catalogo - (quantidade_reservado + quantidade_locado)}")
        print(f"\n-----------------------------------------------------------------------------------------------------------\n")
    max_id.sort()
    conn.close()
    if max_id:
        return max_id[-1]
    else:
        return 0

def list_books_simpler():
    conn = start_connection()
    cursor = conn.cursor()
    sql = "SELECT id_livro, titulo_livro, nome_autor FROM biblioteca.livros JOIN biblioteca.autores ON livros.id_autor = autores.id_autor ORDER BY biblioteca.livros.titulo_livro"
    cursor.execute(sql)
    result = cursor.fetchall()
    print("Lista de todos os livros cadastrados (em ordem alfabética): ")
    max_id = []
    for id_livro, titulo_livro, nome_autor in result:
        max_id.append(id_livro)
        print(f"- TÍTULO: {titulo_livro}")
        print(f"- AUTOR: {nome_autor}")
        print(f"- ID DO LIVRO: {id_livro}")
        print(f"\n-----------------------------------------------------------------------------------------------------------\n")
    max_id.sort()
    conn.close()
    if max_id:
        return max_id[-1]
    else:
        return 0

def list_book_author():
    conn = start_connection()
    cursor = conn.cursor()
    sql = "SELECT id_autor, nome_autor FROM biblioteca.autores ORDER BY nome_autor"
    cursor.execute(sql)
    result = cursor.fetchall()
    print("Lista de autores cadastrados (em ordem alfabética): ")
    max_id = []
    for id_autor, nome_autor in result:
        max_id.append(id_autor)
        print(f"- {nome_autor} - ID: {id_autor}")
    max_id.sort()
    conn.close()
    if max_id:
        return max_id[-1]
    else:
        return 0

def list_book_publisher():
    conn = start_connection()
    cursor = conn.cursor()
    sql = "SELECT id_editora, nome_editora, local_editora FROM biblioteca.editoras ORDER BY nome_editora"
    cursor.execute(sql)
    result = cursor.fetchall()
    print("Lista de editoras cadastradas (em ordem alfabética): ")
    max_id = []
    for id_editora, nome_editora, local_editora in result:
        max_id.append(id_editora)
        if local_editora:
            print(f"- {nome_editora} - ID: {id_editora}")
        else:
            print(f"- {nome_editora} (local não cadastrado) - ID: {id_editora}")
    max_id.sort()
    conn.close()
    if max_id:
        return max_id[-1]
    else:
        return 0

def list_book_category():
    conn = start_connection()
    cursor = conn.cursor()
    sql = "SELECT id_categoria, nome_categoria FROM biblioteca.categorias ORDER BY nome_categoria"
    cursor.execute(sql)
    result = cursor.fetchall()
    print("Lista de categorias cadastradas (em ordem alfabética): ")
    max_id = []
    for id_categoria, nome_categoria in result:
        max_id.append(id_categoria)
        print(f"- {nome_categoria} - ID: {id_categoria}")
    max_id.sort()
    conn.close()
    if max_id:
        return max_id[-1]
    else:
        return 0

def add_book_author():
    list_book_author()
    while True:
        try:
            author_name = input("Digite o nome do novo autor ou digite 0 para cancelar: ")
            if author_name == '0':
                break
            elif author_name != '0':
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
    max_id = list_book_author()
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

#def add_new_book(user):
def add_new_book():
    next = 0
    authors = []
    while next == 0:
        while True:
            try:
                max_author = int(input("Quantos autores escreveram o livro a ser cadastrado?: "))
                counter = (list_book_author() + 1)
                if max_author == 1:
                    try:
                        id_author = int(input(f"Digite o ID do autor ou digite {counter} para adicionar um novo: "))
                        if id_author <= 0 or id_author > counter:
                                print("Valor inválido")
                        elif id_author == counter:
                            author = input("Digite o nome do novo autor: ")
                            conn = start_connection()
                            cursor = conn.cursor()
                            sql = "INSERT INTO biblioteca.autores(nome_autor) VALUES (%s)"
                            cursor.execute(sql, [author])
                            conn.commit()
                            conn.close()
                            authors.append(id_author)
                            counter += 1
                        elif id_author in range(1, (counter + 1)):
                            next = 1
                            break
                    except ValueError:
                        print("Valor inválido")
                        system('cls')
                elif max_author > 1:
                    for i in range(1, max_author + 1):
                        try:
                            print(authors)
                            id_author = int(input(f"Digite o ID do autor {i}/{max_author} ou digite {counter} para adicionar um novo: "))
                            if id_author <= 0 or id_author > counter:
                                print("Valor inválido")
                            elif id_author == counter:
                                author = input("Digite o nome do novo autor: ")
                                conn = start_connection()
                                cursor = conn.cursor()
                                sql = "INSERT INTO biblioteca.autores(nome_autor) VALUES (%s)"
                                cursor.execute(sql, [author])
                                conn.commit()
                                conn.close()
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
    
    #system('cls')
    while next == 1:
        try:
            book_title = input(f"Digite o título do livro: ")
            next = 2
            break
        except Exception as title_error:
            print(f"Erro ao tentar adicionar o livro: {title_error}")

    system('cls')
    counter = (list_book_publisher() + 1)
    while next == 2:
        try:
            id_publisher = int(input(f"Digite o ID da editora ou digite {counter} para adicionar uma nova: "))
            if id_publisher <= 0 or id_publisher > counter:
                print("Valor inválido")
            elif id_publisher == counter:
                publisher_name = input("Digite o nome da editora: ")
                publisher_location = input("Digite o local da editora ou aperte enter para deixar em branco: ")
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
            book_isbn = input(f"Digite o ISBN do livro: ")
            next = 4
            break
        except Exception as isbn_error:
            print(f"Erro ao tentar adicionar o ISBN do livro: {isbn_error}")

    system('cls')
    while next == 4:
        try:
            book_year = input(f"Digite o ano da edição do livro: ")
            next = 5
            break
        except Exception as year_error:
            print(f"Erro ao tentar adicionar o ano da edição do livro: {year_error}")

    system('cls')
    while next == 5:
        try:
            book_language = input(f"Digite o idioma em que o livro foi publicado ou aperte enter para deixar em branco: ")
            next = 6
            break
        except Exception as language_error:
            print(f"Erro ao tentar adicionar o ISBN do livro: {language_error}")

    system('cls')
    counter = (list_book_category() + 1)
    while next == 6:
        try:
            id_category = int(input(f"Digite o ID da categoria ou digite {counter} para adicionar uma nova: "))
            if id_category <= 0 or id_category > counter:
                print("Valor inválido")
            elif id_category == counter:
                category = input("Digite o nome da nova categoria: ")
                conn = start_connection()
                cursor = conn.cursor()
                sql = "INSERT INTO biblioteca.categorias(nome_categoria) VALUES (%s)"
                cursor.execute(sql, [category])
                conn.commit()
                conn.close()
                next = 7
                break
            elif id_category in range(1, (counter + 1)):
                next = 7
                break
        except ValueError:
            print("Valor inválido")
        except Exception as category_error:
            print(f"Erro ao tentar adicionar a categoria: {category_error}")
        
    #system('cls')
    while next == 7:
        try:
            book_quantity = int(input(f"Digite a quantidade de volumes a serem disponibilizados: "))
            conn = start_connection()
            cursor = conn.cursor()
            sql = "INSERT INTO biblioteca.livros(id_autor, titulo_livro, id_editora, isbn_livro, ano_livro, idioma_livro, id_categoria, quantidade_catalogo, id_funcionario, quantidade_reservado, quantidade_locado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, 1, 0, 0)"
            #cursor.execute(sql, [id_author, book_title, id_publisher, book_isbn, book_year, book_language, id_category, book_quantity, user[0]])
            cursor.execute(sql, [id_author, book_title, id_publisher, book_isbn, book_year, book_language, id_category, book_quantity])
            conn.commit()
            conn.close()
            if max_author == 1:
                current_book_id = get_book_id()
                conn.close()
                conn = start_connection()
                cursor = conn.cursor()
                sql = "INSERT INTO biblioteca.autores_do_livro(id_livro, id_autor) VALUES ('%s', '%s')"
                cursor.execute(sql, [current_book_id, id_author])
                conn.commit()
                conn.close()
                #system('cls')
                print("Livro adicionado com sucesso")
                break
            elif max_author > 1:
                index = 0
                current_book_id = get_book_id()
                author_index = authors[index]
                print(f"current_book_id {current_book_id}")
                print(f"authors {authors}")
                print(f"authors[0] {authors[0]}")
                print(f"authors[index] {authors[index]}")
                print(f"author_index {author_index}")
                for i in range(max_author):
                    conn = start_connection()
                    cursor = conn.cursor()
                    sql = "INSERT INTO biblioteca.autores_do_livro(id_livro, id_autor) VALUES (%s, %s)"
                    cursor.execute(sql, [current_book_id, author_index])
                    conn.commit()
                    conn.close()
                    author_index += 1
                    #index += 1
                    print(max_author)
                    print(authors)
                    print(f"authors[index] {authors[index]}")
                    print(f"author_index {author_index}")
                #system('cls')
                print("Livro adicionado com sucesso")
                #break
        except ValueError:
            print("Valor inválido")
        except Exception as quantity_error:
            print(f"Erro ao tentar adicionar a quantidade de volumes disponíveis: {quantity_error}")
        finally:
            conn.close()
            break

def remove_book():
    counter = list_books_simpler()
    max_id = counter[-1]
    while True:
        try:
            id_delete = int(input("Digite o ID do livro que você quer remover do banco de dados: "))
            if id_delete < 0 or id_delete > max_id:
                print("Valor inválido")
            elif id_delete in range (1, max_id + 1):
                conn = start_connection()
                cursor = conn.cursor()
                sql = "DELETE FROM biblioteca.livros WHERE id_livro = %s"
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
            print(f"Erro ao tentar adicionar a quantidade de volumes disponíveis: {remove_book_error}")


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