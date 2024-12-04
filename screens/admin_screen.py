from os import system
from services.admin_services import add_admin, list_books, add_new_book, remove_book, edit_books_titles, edit_books_quantities, add_book_author, remove_author, edit_books_authors, edit_worker_name, edit_worker_email, edit_worker_password, add_publisher, edit_publishers, remove_publisher, add_new_category, remove_category, edit_category
from utils.utils import list_books, list_all_book_authors, list_book_publisher, list_book_category
from services.searching_services import book_search
import pwinput

def admin_screen(user):
    system('cls')
    while True:
        try:            
            print(f"TELA ADMIN\nBem-vindo {user[2]}\nEscolha uma opção: ")
            print("1 - Cadastrar um novo administrador")
            print("2 - Menu de opções: LIVROS")
            print("3 - Menu de opções: RESERVAS E LOCAÇÕES")
            print("4 - Editar dados pessoais")
            print("5 - Sair do sistema")
            opc = int(input("Selecione a opção: "))
            match opc:
                case 1:
                    system('cls')
                    registration = input("Digite a matrícula do administrador: ")
                    system('cls')
                    name = input("Digite o nome do administrador: ")
                    system('cls')
                    email = input("Digite o email do administrador: ")
                    system('cls')
                    password = pwinput.pwinput("Digite a senha do administrador: ")
                    add_admin(registration, name, email, password)
                case 2:
                    crud_admin_books(user)
                case 3:
                    crud_admin_locations(user)
                case 4:
                    crud_admin_personal_data(user)
                case 5:
                    system('cls')
                    print("Saindo...")
                    break
                case _:
                    system('cls')
                    print("Opção inválida")          
        except ValueError:
            system('cls')
            print("Opção inválida")

def crud_admin_books(user):
    system('cls')
    while True:
        try: 
            print("\nAÇÕES - LIVROS")
            print("1 - Fazer busca no sistema")
            print("2 - Listar livros cadastrados")
            print("3 - Adicionar um novo livro ao catálogo")
            print("4 - Remover um livro do catálogo")
            print("5 - Editar o título de um livro do catálogo")
            print("6 - Editar a quantidade de um livro disponível no acervo")
            print("\nAÇÕES - AUTORES")
            print("7 - Listar autores cadastrados")
            print("8 - Adicionar um autor ao cadastro")
            print("9 - Remover um autor do cadastro")
            print("10 - Editar um autor do cadastro")
            print("\nAÇÕES - EDITORAS")
            print("11 - Listar editoras cadastradas")
            print("12 - Adicionar uma editora ao cadastro")
            print("13 - Remover uma editora do cadastro")
            print("14 - Editar uma editora do cadastro")
            print("\nAÇÕES - CATEGORIAS DE LIVROS")
            print("15 - Listar as categorias de livros cadastradas")
            print("16 - Adicionar uma categoria de livros ao cadastro")
            print("17 - Remover uma categoria de livros do cadastro")
            print("18 - Editar uma categoria de livros do cadastro")
            print("\nVOLTAR")
            print("19 - Voltar ao menu anterior")
            opc = int(input("Selecione a opção: "))
            match opc:
                case 1:
                    system('cls')
                    book_search()
                case 2:
                    system('cls')
                    list_books()
                case 3:
                    system('cls')
                    add_new_book(user)
                case 4:
                    system('cls')
                    remove_book()
                case 5:
                    system('cls')
                    edit_books_titles()
                case 6:
                    system('cls')
                    edit_books_quantities()
                case 7:
                    system('cls')
                    list_all_book_authors()
                case 8:
                    system('cls')
                    add_book_author()
                case 9:
                    system('cls')
                    remove_author()
                case 10:
                    system('cls')
                    edit_books_authors()
                case 11:
                    system('cls')
                    list_book_publisher()
                case 12:
                    system('cls')
                    add_publisher()
                case 13:
                    system('cls')
                    remove_publisher()
                case 14:
                    system('cls')
                    edit_publishers()
                case 15:
                    system('cls')
                    list_book_category()
                case 16:
                    system('cls')
                    add_new_category()
                case 17:
                    system('cls')
                    remove_category()
                case 18:
                    system('cls')
                    edit_category()
                case 19:
                    system('cls')
                    admin_screen(user)
                case _:
                    system('cls')
                    print("Opção inválida")          
        except ValueError:
            system('cls')
            print("Opção inválida")

def crud_admin_personal_data(user):
    system('cls')
    while True:
        try: 
            print("EDITAR DADOS PESSOAIS\n")
            print("1 - Atualizar o nome")
            print("2 - Atualizar o e-mail")
            print("3 - Atualizar a senha")
            print("4 - Voltar ao menu anterior")
            opc = int(input("Selecione a opção: "))
            match opc:
                case 1:
                    system('cls')
                    edit_worker_name(user)
                case 2:
                    system('cls')
                    edit_worker_email(user)
                case 3:
                    system('cls')
                    edit_worker_password(user)
                case 4:
                    system('cls')
                    admin_screen(user)
                case _:
                    system('cls')
                    print("Opção inválida")          
        except ValueError:
            system('cls')
            print("Opção inválida")

def crud_admin_locations(user):
    print("")