from os import system
from services.admin_services import add_admin
from screens.crud_admin import crud_admin_screen, crud_admin_edit
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
                    registration = input("Digite a matrícula do administrador: ")
                    name = input("Digite o nome do administrador: ")
                    email = input("Digite o email do administrador: ")
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

