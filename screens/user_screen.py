from os import system
from utils.utils import list_books
from services.students_services import book_reservation, cancel_book_reservation, edit_student_name, edit_student_email, edit_student_password

def user_screen(user):
    while True:
        try:            
            print(f"TELA USUÁRIO\nBem-vindo {user[2]}")
            print("1 - Listar livros do catálogo")
            print("2 - Reservar um livro")
            print("3 - Cancelar uma reserva")
            print("4 - Editar dados pessoais")
            print("5 - Sair")
            opc = int(input("Selecione a opção: "))
            match opc:
                case 1:
                    list_books()
                case 2:
                    book_reservation()
                case 3:
                    cancel_book_reservation()
                case 4:
                    edit_student_data_screen(user)
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

def edit_student_data_screen(user):
    while True:
        try:            
            print(f"EDITAR DADOS PESSOAIS")
            print("1 - Alterar nome")
            print("2 - Alterar e-mail")
            print("3 - Alterar a senha")
            print("4 - Voltar ao menu anterior")
            opc = int(input("Selecione a opção: "))
            match opc:
                case 1:
                    edit_student_name(user)
                case 2:
                    edit_student_email(user)
                case 3:
                    edit_student_password(user)
                case 4:
                    user_screen(user)
                case _:
                    system('cls')
                    print("Opção inválida")          
        except ValueError:
            system('cls')
            print("Opção inválida")

    # while(True):
    #     print(f"Bem-vindo {user[2]}")
    #     print("""
    #     TELA USUÁRIO
    #     1 - Listar livros disponíveis no catálogo
    #     5 - Sair
 

        # opc = input("Digite a opcao desejada: ")

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