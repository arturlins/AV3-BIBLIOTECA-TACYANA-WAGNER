from os import system
from services.admin_services import add_admin, list_books, add_new_book
import pwinput

def admin_screen(user):
    system('cls')
    while True:
        try:            
            print(f"TELA ADMIN\nBem-vindo {user[2]}")
            print("1 - Cadastrar um novo administrador")
            print("2 - Listar livros cadastrados")
            print("3 - Adicionar um novo livro ao catálogo")
            print("4 - Sair")
            opc = int(input("Selecione a opção: "))
            match opc:
                case 1:
                    registration = input("Digite a matrícula do administrador: ")
                    name = input("Digite o nome do administrador: ")
                    email = input("Digite o email do administrador: ")
                    password = pwinput.pwinput("Digite a senha do administrador: ")
                    add_admin(registration, name, email, password)
                case 2:
                    list_books()
                case 3:
                    add_new_book(user)
                case 4:
                    system('cls')
                    print("Saindo...")
                    break
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

