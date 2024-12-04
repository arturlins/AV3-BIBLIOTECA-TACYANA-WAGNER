from os import system
from utils.utils import list_books
from services.students_services import book_reservation, cancel_book_reservation, edit_student_name, edit_student_email, edit_student_password, list_user_reservations, list_user_rentings
from services.searching_services import book_search

def user_screen(user):
    while True:
        try:            
            print(f"TELA USUÁRIO\nBem-vindo {user[2]}")
            print("1 - Listar livros do catálogo")
            print("2 - Fazer uma busca no catálogo")
            print("3 - Reservar um livro")
            print("4 - Listar minhas reservas")
            print("5 - Cancelar uma reserva")
            print("6 - Listar meus empréstimos de livros")
            print("7 - Editar dados pessoais")
            print("8 - Sair do sistema")
            opc = int(input("Selecione a opção: "))
            match opc:
                case 1:
                    system('cls')
                    list_books()
                case 2:
                    system('cls')
                    book_search()
                case 3:
                    system('cls')
                    book_reservation(user)
                case 4:
                    system('cls')
                    list_user_reservations(user)
                case 5:
                    cancel_book_reservation(user)
                case 6:
                    list_user_rentings(user)
                case 7:
                    crud_student_personal_data(user)
                case 8:
                    system('cls')
                    print("Saindo...")
                    break
                case _:
                    system('cls')
                    print("Opção inválida")          
        except ValueError:
            system('cls')
            print("Opção inválida")

def crud_student_personal_data(user):
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
                    system('cls')
                    edit_student_name(user)
                case 2:
                    system('cls')
                    edit_student_email(user)
                case 3:
                    system('cls')
                    edit_student_password(user)
                case 4:
                    system('cls')
                    user_screen(user)
                case _:
                    system('cls')
                    print("Opção inválida")          
        except ValueError:
            system('cls')
            print("Opção inválida")