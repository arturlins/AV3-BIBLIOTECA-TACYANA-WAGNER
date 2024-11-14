from services.users_services import add_student
import pwinput

registration = input("Digite a matrícula do aluno: ")
name = input("Digite o nome do aluno: ")
email = input("Digite o e-mail do aluno: ")
course = input("Digite o curso do aluno: ")
password = pwinput.pwinput("Digite a senha do aluno: ")
add_student(registration, name, email, course, password)