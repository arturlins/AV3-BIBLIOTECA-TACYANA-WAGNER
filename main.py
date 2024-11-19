from os import system
from services.users_services import add_student, login, privilege_check
from screens.admin_screen import admin_screen
from screens.user_screen import  user_screen
import pwinput

while True:
    try:            
        print("Bem-vindo à Biblioteca do Cesmac!\nEscolha uma opção abaixo: ")
        print("1 - Criar cadastro")
        print("2 - Fazer Login")
        print("3 - Sair")
        opc = int(input("Selecione a opção: "))
        match opc:
            case 1:
                add_student()
            case 2:
                email = input("Digite o email: ")
                password = pwinput.pwinput("Digite a senha: ")
                login(email, password)
                authenticated_user = login(email, password)
                privilege_check(email)
                privilege = privilege_check(email)
                if authenticated_user and privilege == True:
                        admin_screen(authenticated_user)
                elif authenticated_user and privilege == False:
                        user_screen(authenticated_user)
                else:
                    system('cls')
                    print("Usuario ou senha invalidos!")
            case 3:
                system('cls')
                print("Saindo...")
                break
            case _:
                system('cls')
                print("Opção inválida")          
    except ValueError:
        system('cls')
        print("Opção inválida")