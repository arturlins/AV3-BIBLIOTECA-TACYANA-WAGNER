from services.admin_services import add_admin
import pwinput

registration = input("Digite a matrícula do administrador: ")
name = input("Digite o nome do administrador: ")
email = input("Digite o email do administrador: ")
password = pwinput.pwinput("Digite a senha do administrador: ")
add_admin(registration, name, email, password)