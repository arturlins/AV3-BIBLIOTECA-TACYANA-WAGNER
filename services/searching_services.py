from os import system
from config.db import start_connection

def book_search():
    system('cls')
    conn = start_connection()
    cursor = conn.cursor()
    search = input("Digite a palavra/frase que você quer pesquisar: ")
    sql = f"SELECT titulo_livro, nome_autor, nome_editora FROM biblioteca.livros JOIN biblioteca.autores_do_livro ON livros.id_livro = autores_do_livro.id_livro JOIN biblioteca.autores ON autores_do_livro.id_autor = autores.id_autor JOIN biblioteca.editoras ON livros.id_editora = editoras.id_editora WHERE titulo_livro ILIKE '%{search}%' OR nome_autor ILIKE '%{search}%' OR nome_editora ILIKE '%{search}%' ORDER BY livros.titulo_livro"
    cursor.execute(sql)
    result = cursor.fetchall()
    if result:    
        print(f"Resultados encontrados em '{search}': ")
        for titulo_livro, nome_autor, nome_editora in result:
            print(f"- TÍTULO DO LIVRO: {titulo_livro}")
            print(f"- AUTOR: {nome_autor}")
            print(f"- EDITORA: {nome_editora}")
            print(f"-------------------------------------------------------------------------------------\n")
    else:
        system('cls')
        print(f"Nenhum livro, autor ou editora encontrado em '{search}'")
        print("\n")
        
def student_search():
    system('cls')
    conn = start_connection()
    cursor = conn.cursor()
    search = input("Digite a palavra que você quer pesquisar: ")
    sql = f"SELECT nome_aluno, matricula_aluno, curso_aluno FROM biblioteca.alunos WHERE nome_aluno ILIKE '%{search}%' ORDER BY alunos.nome_aluno"
    cursor.execute(sql)
    result = cursor.fetchall()
    if result:    
        print(f"Resultados encontrados em '{search}': ")
        for nome_aluno, matricula_aluno, curso_aluno in result:
            print(f"- NOME DO ALUNO: {nome_aluno}")
            print(f"- MATRÍCULA: {matricula_aluno}")
            print(f"- CURSO: {curso_aluno}")
            print(f"-------------------------------------------------------------------------------------\n")
        print("\n")
    else:
        system('cls')
        print(f"Nenhum aluno encontrado em '{search}'")
        print("\n")