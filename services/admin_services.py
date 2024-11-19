from os import system
from config.db import start_connection
from config.security import check_password, encrypt_password

def add_admin(registration, name, email, password):
    try:
        hashed_password = encrypt_password(password)
        conn = start_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO alunos (matricula_aluno, nome_aluno, email_aluno, curso_aluno, senha_aluno, privilegio_admin) VALUES (%s, %s, %s, 'ADMIN', %s, TRUE)"
        cursor.execute(sql, (registration, name, email, hashed_password))
        conn.commit()
        system('cls')
        print("Administrador adicionado com sucesso!")
    except Exception as error_admin:
        print(f"Erro ao adicionar o administrador: {error_admin}")
    finally:
        conn.close()

def list_books():
    conn = start_connection()
    cursor = conn.cursor()
    sql = "SELECT livros.titulo_livro, autores.nome_autor, autores.sobrenome_autor, editoras.nome_editora, categorias.nome_categoria, livros.ano_livro, livros.idioma_livro, livros.quantidade from livros JOIN autores ON livros.id_autor = autores.id_autor JOIN editoras ON livros.id_editora = editoras.id_editora JOIN categorias ON livros.id_categoria = categorias.id_categoria ORDER BY livros.titulo_livro"
    cursor.execute(sql)
    result = cursor.fetchall()
    print("Lista de todos os livros cadastrados (em ordem alfabética): ")
    counter = 0
    for titulo_livro, nome_autor, sobrenome_autor, nome_editora, nome_categoria, ano_livro, idioma_livro, quantidade in result:
        counter = counter + 1
        print(f"- ID: {counter}")
        print(f"- TÍTULO: {titulo_livro}")
        print(f"- AUTOR: {nome_autor} {sobrenome_autor}")
        print(f"- EDITORA: {nome_editora}")
        print(f"- CATEGORIA: {nome_categoria}")
        print(f"- ANO DA EDIÇÃO: {ano_livro}")
        print(f"- IDIOMA DO LIVRO: {idioma_livro}")
        print(f"- QUANTIDADE DE VOLUMES NO CATÁLOGO: {quantidade}")
        print(f"-----------------------------------------------------------------------------------------------------------\n")

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