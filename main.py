from os import system
from services.users_services import add_student, login_student, login_worker
from screens.admin_screen import admin_screen
from screens.user_screen import user_screen
import pwinput

while True:
    try:            
        print("Bem-vindo à Biblioteca do Cesmac!\nEscolha uma opção abaixo: ")
        print("1) Criar cadastro")
        print("2) Fazer Login - Alunos")
        print("3) Fazer Login - Funcionários")
        print("4) Sair")
        opc = int(input("Selecione a opção: "))
        match opc:
            case 1:
                system('cls')
                add_student()
            case 2:
                email = input("Digite o email: ")
                password = pwinput.pwinput("Digite a senha: ")
                login_student(email, password)
                authenticated_user = login_student(email, password)
                if authenticated_user:
                    user_screen(authenticated_user)
                else:
                    system('cls')
                    print("Usuario ou senha inválidos!")
            case 3:
                email = input("Digite o email: ")
                password = pwinput.pwinput("Digite a senha: ")
                login_worker(email, password)
                authenticated_user = login_worker(email, password)
                if authenticated_user:
                    admin_screen(authenticated_user)
                else:
                    system('cls')
                    print("Usuario ou senha inválidos!")
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