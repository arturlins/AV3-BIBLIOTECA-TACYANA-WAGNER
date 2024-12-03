from os import system
from utils.utils import list_books
from services.students_services import book_reservation, cancel_book_reservation, edit_student_name, edit_student_email, edit_student_password

def user_screen(user):
    while True:
        try:            
            system('cls')
            print(f"TELA USUÁRIO\nBem-vindo {user[2]}")
            print("1 - Listar livros do catálogo")
            print("2 - Reservar um livro")
            print("3 - Cancelar uma reserva")
            print("4 - Editar dados pessoais")
            print("5 - Sair")
            opc = int(input("Selecione a opção: "))
            match opc:
                case 1:
                    list_books(user)
                case 2:
                    book_reservation(user)
                case 3:
                    cancel_book_reservation(user)
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