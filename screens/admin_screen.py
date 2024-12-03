from os import system
from services.admin_services import add_admin, list_books, add_new_book, remove_book, edit_books_titles, edit_books_quantities, add_book_author, remove_author, edit_books_authors, edit_worker_name, edit_worker_email, edit_worker_password, add_publisher, edit_publishers, remove_publisher
from utils.utils import list_books, list_all_book_authors, list_book_publisher
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
            print("5 - Sair")
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
                    crud_admin_screen(user)
                # case 3:
                #     add_new_book(user)
                case 4:
                    crud_admin_edit(user)
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
            print("11 - Adicionar uma editora ao cadastro")
            print("12 - Remover uma editora do cadastrado")
            print("13 - Editar uma editora do cadastrado")
            # print("\nAÇÕES - CATEGORIAS DE LIVROS")
            # print("14 - Remover uma editora do cadastrado")
            print("20 - Voltar ao menu anterior")
            opc = int(input("Selecione a opção: "))
            match opc:
                case 1:
                    system('cls')
                    list_books()
                case 2:
                    system('cls')
                    add_new_book(user)
                case 3:
                    system('cls')
                    remove_book()
                case 4:
                    system('cls')
                    edit_books_titles()
                case 5:
                    system('cls')
                    edit_books_quantities()
                case 6:
                    system('cls')
                    list_all_book_authors()
                case 7:
                    system('cls')
                    add_book_author()
                case 8:
                    system('cls')
                    remove_author()
                case 9:
                    system('cls')
                    edit_books_authors()
                case 10:
                    system('cls')
                    list_book_publisher()
                case 12:
                    remove_publisher()
                case 11:
                    add_publisher()
                case 13:
                    edit_publishers()
                case 20:
                    system('cls')
                    admin_screen(user)
                case _:
                    system('cls')
                    print("Opção inválida")          
        except ValueError:
            system('cls')
            print("Opção inválida")

def crud_admin_edit(user):
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
                    edit_worker_name(user)
                case 2:
                    edit_worker_email(user)
                case 3:
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

        # if opc == "1":
        #     title = input("Digite o titulo da task: ")
        #     create_task(usuario[0], title)
        #     print("Tarefa Criada!")
        # elif opc == "2":
        #     tasks = list_tasks(usuario[0])
        #     print(tasks)
        # elif opc == "3":
        #     taks_id = input("Digite o id da task: ")
        #     delete_task(usuario[0], taks_id)
        # elif opc == "4":
        #     title = input("Digite o novo titulo da task: ")
        #     tasks_id = input("Digite o id da task: ")
        #     update_task(usuario[0], tasks_id, title)
        # elif opc == "5":
        #     break

