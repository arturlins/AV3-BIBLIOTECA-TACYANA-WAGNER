from config.db import start_connection

def get_book_id():
    conn = start_connection()
    cursor = conn.cursor()
    sql = "SELECT * FROM biblioteca.livros"
    cursor.execute(sql)
    result = cursor.fetchall()
    max_id = []
    for id_livro, _, _, _, _, _, _, _, _, _, _ in result:
        max_id.append(id_livro)
    max_id.sort()
    conn.close()
    if max_id:
        return max_id[-1]
    else:
        return 0

def list_books_authors_only(id_livro):
    conn = start_connection()
    cursor = conn.cursor()
    sql = "SELECT * FROM biblioteca.autores_do_livro JOIN biblioteca.autores ON autores.id_autor = autores_do_livro.id_autor WHERE autores_do_livro.id_livro = %s"
    cursor.execute(sql, [id_livro])
    result = cursor.fetchall()
    for _, _, _, _, nome_autor in result:
        print(f"- AUTORIA: {nome_autor}")  

def list_books():
    conn = start_connection()
    #cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cursor = conn.cursor()
    #sql = "SELECT livros.id_livro, titulo_livro, nome_autor, nome_editora, nome_categoria, ano_livro, idioma_livro, isbn_livro, quantidade_catalogo, quantidade_reservado, quantidade_locado FROM biblioteca.livros JOIN biblioteca.autores_do_livro ON autores_do_livro.id_livro = livros.id_livro JOIN biblioteca.autores ON autores_do_livro.id_autor = autores.id_autor JOIN biblioteca.editoras ON livros.id_editora = editoras.id_editora JOIN biblioteca.categorias ON livros.id_categoria = categorias.id_categoria ORDER BY biblioteca.livros.titulo_livro"
    sql = "SELECT livros.id_livro, titulo_livro, nome_editora, nome_categoria, ano_livro, idioma_livro, isbn_livro, quantidade_catalogo, quantidade_reservado, quantidade_locado FROM biblioteca.livros JOIN biblioteca.autores_do_livro ON autores_do_livro.id_livro = livros.id_livro JOIN biblioteca.autores ON autores_do_livro.id_autor = autores.id_autor JOIN biblioteca.editoras ON livros.id_editora = editoras.id_editora JOIN biblioteca.categorias ON livros.id_categoria = categorias.id_categoria GROUP BY livros.id_livro, biblioteca.livros.titulo_livro, editoras.nome_editora, categorias.nome_categoria ORDER BY biblioteca.livros.titulo_livro"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    print("Lista de todos os livros cadastrados (em ordem alfabética): ")
    max_id = []
    for id_livro, titulo_livro, nome_editora, nome_categoria, ano_livro, idioma_livro, isbn_livro, quantidade_catalogo, quantidade_reservado, quantidade_locado in result:
                max_id.append(id_livro)
                print(f"- TÍTULO: {titulo_livro}")
                list_books_authors_only(id_livro)
                print(f"- ID DO LIVRO: {id_livro}")
                print(f"- EDITORA: {nome_editora}")
                print(f"- CATEGORIA: {nome_categoria}")
                if ano_livro:
                    print(f"- ANO DA EDIÇÃO: {ano_livro}")
                else:
                    print(f"- ANO DA EDIÇÃO: (não cadastrado)")
                if idioma_livro:
                    print(f"- IDIOMA DO LIVRO: {idioma_livro}")
                else:
                    print(f"- IDIOMA DO LIVRO: (não cadastrado)")
                if isbn_livro == '                 ':
                     print(f"- ISBN DO LIVRO: (não cadastrado)")
                elif isbn_livro:
                    print(f"- ISBN DO LIVRO: {isbn_livro}")
                else:
                    print(f"- ISBN DO LIVRO: (não cadastrado)")
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

# def get_limited_input(prompt, max_length=100):
#     while True:
#         user_input = input(prompt)
#         if len(user_input) <= max_length:
#             return user_input
#         else:
#             print(f"Input exceeds {max_length} characters. Please try again.")