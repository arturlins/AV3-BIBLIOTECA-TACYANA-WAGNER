from config.db import start_connection
from datetime import date

def get_book_id():
    conn = start_connection()
    cursor = conn.cursor()
    sql = "SELECT last_value + 1 FROM pg_sequences WHERE schemaname = 'biblioteca' AND sequencename = 'livros_id_livro_seq'"
    cursor.execute(sql)
    next_id = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    if next_id:
        return next_id
    else:
        return 0

def get_author_id():
    conn = start_connection()
    cursor = conn.cursor()
    sql = "SELECT last_value + 1 FROM pg_sequences WHERE schemaname = 'biblioteca' AND sequencename = 'autores_id_autor_seq'"
    cursor.execute(sql)
    next_id = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    if next_id:
        return next_id
    else:
        return 0

def get_category_id():
    conn = start_connection()
    cursor = conn.cursor()
    sql = "SELECT last_value + 1 FROM pg_sequences WHERE schemaname = 'biblioteca' AND sequencename = 'categorias_id_categoria_seq'"
    cursor.execute(sql)
    next_id = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    if next_id:
        return next_id
    else:
        return 0
    
def get_publisher_id():
    conn = start_connection()
    cursor = conn.cursor()
    sql = "SELECT last_value + 1 FROM pg_sequences WHERE schemaname = 'biblioteca' AND sequencename = 'editoras_id_editora_seq'"
    cursor.execute(sql)
    next_id = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    if next_id:
        return next_id
    else:
        return 0

def get_title_by_id(id_edit):
    conn = start_connection()
    cursor = conn.cursor()
    sql = "SELECT titulo_livro FROM biblioteca.livros WHERE id_livro = %s"
    cursor.execute(sql, [id_edit])
    title = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    if title:
        return title
    else:
        return 0

def get_quantity_by_id(id_edit):
    conn = start_connection()
    cursor = conn.cursor()
    sql = "SELECT quantidade_catalogo FROM biblioteca.livros WHERE id_livro = %s"
    cursor.execute(sql, [id_edit])
    quantity = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    if quantity:
        return quantity
    else:
        return 0
    
def get_author_by_id(id_edit):
    conn = start_connection()
    cursor = conn.cursor()
    sql = "SELECT nome_autor FROM biblioteca.autores WHERE id_autor = %s"
    cursor.execute(sql, [id_edit])
    author = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    if author:
        return author
    else:
        return 0
    
def get_student_name_by_id(id_edit):
    conn = start_connection()
    cursor = conn.cursor()
    sql = "SELECT nome_aluno FROM biblioteca.alunos WHERE id_aluno = %s"
    cursor.execute(sql, [id_edit])
    student = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    if student:
        return student
    else:
        return 0
    
def get_student_email_by_id(id_edit):
    conn = start_connection()
    cursor = conn.cursor()
    sql = "SELECT email_aluno FROM biblioteca.alunos WHERE id_aluno = %s"
    cursor.execute(sql, [id_edit])
    student = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    if student:
        return student
    else:
        return 0

def get_worker_name_by_id(id_edit):
    conn = start_connection()
    cursor = conn.cursor()
    sql = "SELECT nome_funcionario FROM biblioteca.funcionarios WHERE id_funcionario = %s"
    cursor.execute(sql, [id_edit])
    worker = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    if worker:
        return worker
    else:
        return 0
    
def get_worker_email_by_id(id_edit):
    conn = start_connection()
    cursor = conn.cursor()
    sql = "SELECT email_funcionario FROM biblioteca.funcionarios WHERE id_funcionario = %s"
    cursor.execute(sql, [id_edit])
    worker = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    if worker:
        return worker
    else:
        return 0
    
def get_publisher_name_by_id(id_edit):
    conn = start_connection()
    cursor = conn.cursor()
    sql = "SELECT nome_editora FROM biblioteca.editoras WHERE id_editora = %s"
    cursor.execute(sql, [id_edit])
    publisher = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    if publisher:
        return publisher
    else:
        return 0
    
def get_category_name_by_id(id_edit):
    conn = start_connection()
    cursor = conn.cursor()
    sql = "SELECT nome_categoria FROM biblioteca.categorias WHERE id_categoria = %s"
    cursor.execute(sql, [id_edit])
    category = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    if category:
        return category
    else:
        return 0

def get_reservation_id_by_ids(student_id, book_id):
    conn = start_connection()
    cursor = conn.cursor()
    sql = "SELECT id_reserva FROM biblioteca.reservas WHERE id_aluno = %s AND id_livro = %s"
    cursor.execute(sql, [student_id, book_id])
    reservation = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    if reservation:
        return reservation
    else:
        return 0

def list_all_book_authors():
    conn = start_connection()
    cursor = conn.cursor()
    sql = "SELECT id_autor, nome_autor FROM biblioteca.autores ORDER BY nome_autor"
    cursor.execute(sql)
    result = cursor.fetchall()
    print("Lista de todos os autores cadastrados (em ordem alfabética): ")
    for id_autor, nome_autor in result:
        print(f"- {nome_autor} | ID: {id_autor}")
    conn.close()

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
    cursor = conn.cursor()
    sql = "SELECT livros.id_livro, titulo_livro, nome_editora, nome_categoria, ano_livro, idioma_livro, isbn_livro, quantidade_catalogo, quantidade_reservado, quantidade_locado FROM biblioteca.livros JOIN biblioteca.autores_do_livro ON autores_do_livro.id_livro = livros.id_livro JOIN biblioteca.autores ON autores_do_livro.id_autor = autores.id_autor JOIN biblioteca.editoras ON livros.id_editora = editoras.id_editora JOIN biblioteca.categorias ON livros.id_categoria = categorias.id_categoria GROUP BY livros.id_livro, biblioteca.livros.titulo_livro, editoras.nome_editora, categorias.nome_categoria ORDER BY biblioteca.livros.titulo_livro"
    cursor.execute(sql)
    result = cursor.fetchall()
    print("Lista de todos os livros cadastrados (em ordem alfabética): ")
    for id_livro, titulo_livro, nome_editora, nome_categoria, ano_livro, idioma_livro, isbn_livro, quantidade_catalogo, quantidade_reservado, quantidade_locado in result:
                print(f"- TÍTULO: {titulo_livro}")
                list_books_authors_only(id_livro)
                print(color.BOLD + f"- ID DO LIVRO: {id_livro}" + color.END)
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
    conn.close()

def list_books_simpler():
    conn = start_connection()
    cursor = conn.cursor()
    sql = "SELECT livros.id_livro, titulo_livro FROM biblioteca.livros JOIN biblioteca.autores_do_livro ON autores_do_livro.id_livro = livros.id_livro GROUP BY livros.id_livro ORDER BY biblioteca.livros.titulo_livro"
    cursor.execute(sql)
    result = cursor.fetchall()
    print("Lista de todos os livros cadastrados (em ordem alfabética): ")
    for id_livro, titulo_livro in result:
        print(f"- TÍTULO: {titulo_livro}")
        list_books_authors_only(id_livro)
        print(color.BOLD + f"- ID DO LIVRO: {id_livro}" + color.END)
        print(f"\n-----------------------------------------------------------------------------------------------------------\n")
    conn.close()

def list_book_publisher():
    conn = start_connection()
    cursor = conn.cursor()
    sql = "SELECT id_editora, nome_editora, local_editora FROM biblioteca.editoras ORDER BY nome_editora"
    cursor.execute(sql)
    result = cursor.fetchall()
    print("Lista de editoras cadastradas (em ordem alfabética): ")
    for id_editora, nome_editora, local_editora in result:
        if local_editora:
            print(f"- {nome_editora} ({local_editora}) | ID: {id_editora}")
        else:
            print(f"- {nome_editora} (local não cadastrado) - ID: {id_editora}")

def list_book_category():
    conn = start_connection()
    cursor = conn.cursor()
    sql = "SELECT id_categoria, nome_categoria FROM biblioteca.categorias ORDER BY nome_categoria"
    cursor.execute(sql)
    result = cursor.fetchall()
    print("Lista de categorias cadastradas (em ordem alfabética): ")
    for id_categoria, nome_categoria in result:
        print(f"- {nome_categoria} - ID: {id_categoria}")
    conn.close()

def list_students():
    conn = start_connection()
    cursor = conn.cursor()
    sql = "SELECT nome_aluno, matricula_aluno, curso_aluno, id_aluno FROM biblioteca.alunos ORDER BY nome_aluno"
    cursor.execute(sql)
    result = cursor.fetchall()
    print("Lista de alunos cadastrados (em ordem alfabética): ")
    for nome_aluno, matricula_aluno, curso_aluno, id_aluno in result:
        print(f"- NOME: {nome_aluno}")
        print(f"- MATRÍCULA: {matricula_aluno}")
        print(f"- CURSO: {curso_aluno}")
        print(color.BOLD + f"- ID: {id_aluno}" + color.END)
        print(f"\n-----------------------------------------------------------------------------------------------------------\n")
    conn.close()

def list_rented_books():
    conn = start_connection()
    cursor = conn.cursor()
    sql = "SELECT locacoes.id_locacao, livros.id_livro, livros.titulo_livro, alunos.id_aluno, alunos.nome_aluno FROM biblioteca.locacoes JOIN biblioteca.livros ON locacoes.id_livro = livros.id_livro JOIN biblioteca.alunos ON locacoes.id_aluno = alunos.id_aluno WHERE locacoes.status_devolucao = FALSE"
    cursor.execute(sql)
    result = cursor.fetchall()
    print("Lista de livros locados (em ordem de ID de locação): ")
    for id_locacao, id_livro, titulo_livro, id_aluno, nome_aluno in result:
        print(color.BOLD + f"- ID LOCAÇÃO: {id_locacao}" + color.END)
        print(f"- ID LIVRO: {id_livro}")
        print(f"- TÍTULO DO LIVRO: {titulo_livro}")
        print(f"- ID: {id_aluno}")
        print(f"- NOME: {nome_aluno}")
        print(f"\n-----------------------------------------------------------------------------------------------------------\n")
    conn.close()

def apply_fines():
    try:
        conn = start_connection()
        cursor = conn.cursor()
        today = date.today()
        sql = "SELECT id_locacao, multa_aplicada, valor_multa FROM biblioteca.locacoes WHERE data_devolucao IS NULL AND multa_aplicada = False AND prazo_emprestimo_devolucao < %s"
        cursor.execute(sql, (today,))
        result = cursor.fetchall()
        #print(result)
        for id_locacao, multa_aplicada, valor_multa in result:
            fine = valor_multa + 5
            multa_aplicada = True
            update_sql = "UPDATE biblioteca.locacoes SET valor_multa = %s WHERE locacoes.id_locacao = %s"
            cursor.execute(update_sql, (fine, id_locacao))
            conn.commit()
            update_sql2 = "UPDATE biblioteca.locacoes SET multa_aplicada = %s WHERE locacoes.id_locacao = %s"
            cursor.execute(update_sql2, (multa_aplicada, id_locacao))
            conn.commit()
        conn.close()
    except Exception as error:
        print(f"Erro ao aplicar a multa: {error}")

def check_if_exist_book_fine(return_id):
    conn = start_connection()
    cursor = conn.cursor()
    sql = "SELECT id_locacao, multa_aplicada, valor_multa FROM biblioteca.locacoes WHERE multa_aplicada = TRUE AND id_locacao = %s"
    cursor.execute(sql, (return_id,))
    result = cursor.fetchall()
    if result:
        return 5
    else:
        return 0

class color:
#    PURPLE = '\033[95m'
#    CYAN = '\033[96m'
#    DARKCYAN = '\033[36m'
#    BLUE = '\033[94m'
#    GREEN = '\033[92m'
#    YELLOW = '\033[93m'
#    RED = '\033[91m'
   BOLD = '\033[1m'
#    UNDERLINE = '\033[4m'
   END = '\033[0m'

# def get_limited_input(prompt, max_length=100):
#     while True:
#         user_input = input(prompt)
#         if len(user_input) <= max_length:
#             return user_input
#         else:
#             print(f"Há um limite de {max_length} caracteres.")