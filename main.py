from os import system
from services.users_services import add_student, login
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
            case 3:
                print("Saindo...")
                break
            case _:
                system('cls')
                print("Opção inválida")          
    except ValueError:
        system('cls')
        print("Opção inválida")