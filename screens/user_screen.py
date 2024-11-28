from os import system
from services.admin_services import list_books
from services.students_services import rent_book, edit_student_data

def user_screen(user):
       while True:
        try:            
            print(f"TELA USUÁRIO\nBem-vindo {user[2]}")
            print("1 - Listar livros do catálogo")
            print("2 - Locar um livro")
            print("3 - Devolver um livro")
            print("4 - Editar dados pessoais")
            print("5 - Sair")
            opc = int(input("Selecione a opção: "))
            match opc:
                case 1:
                    list_books()
                case 2:
                    list_books()
                case 3:
                    system('cls')
                    print("Saindo...")
                    break
                case 4:
                    registration = input("Digite a matrícula do  aluno: ")
                    name = input("Digite o nome do  aluno: ")
                    email = input("Digite o email do  aluno:")
                    password = ("Digite a senha do aluno : ")
                    edit_student_data(registration, name, email, password)
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