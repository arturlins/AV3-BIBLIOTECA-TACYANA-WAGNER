from os import system
from services.admin_services import list_books, add_new_book, remove_book, edit_books_titles, edit_books_quantities, add_book_author
from utils.utils import list_books, list_all_book_authors

def crud_admin_screen(user):
    system('cls')
    while True:
        try: 
            print("\nAÇÕES - LIVROS")
            print("1 - Listar livros cadastrados")
            print("2 - Adicionar um novo livro ao catálogo")
            print("3 - Remover um livro do catálogo")
            print("4 - Editar o título de um livro do catálogo")
            print("5 - Editar a quantidade de um livro disponível no acervo")
            print("\nAÇÕES - AUTORES")
            print("6 - Listar autores cadastrados")
            print("7 - Adicionar um autor ao cadastrado")
            print("8 - Remover um autor do cadastrado")
            print("9 - editar um autor do cadastrado")
            print("\nAÇÕES - EDITORAS")
            print("10 - Listar editoras cadastradas")
            print("11 - Adicionar uma editora ao cadastrado")
            print("12 - Remover uma editora do cadastrado")
            print("13 - Editar uma editora do cadastrado")
            print("\nAÇÕES - CATEGORIAS DE LIVROS")
            print("14 - Remover uma editora do cadastrado")
            opc = int(input("Selecione a opção: "))
            match opc:
                case 1:
                    list_books()
                case 2:
                    add_new_book(user)
                case 3:
                    remove_book()
                case 4:
                    edit_books_titles()
                case 5:
                    edit_books_quantities()
                case 6:
                    list_all_book_authors()
                case 7:
                    add_book_author()

                #     system('cls')
                #     print("Saindo...")
                #     break
                # case _:
                #     system('cls')
                #     print("Opção inválida")          
        except ValueError:
            system('cls')
            print("Opção inválida")