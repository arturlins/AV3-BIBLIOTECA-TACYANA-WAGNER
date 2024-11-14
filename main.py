from os import system
from services import *

while True:
    try:            
        print("Bem-vindo à Biblioteca de Jogos!\nEscolha uma opção abaixo: ")
        print("1 - Fazer busca no catálogo")
        print("2 - Listar apenas os títulos dos jogos em ordem crescente")
        print("3 - Listar os jogos que contêm 'k' no título ou subtítulo")
        print("4 - Sair")
        opc = int(input("Selecione a opção: "))
        match opc:
            case 1:
                search_games()
            case 2:
                list_games()
            case 3:
                search_k_games()
            case 4:
                print("Saindo...")
                break
            case _:
                system('cls')
                print("Opção inválida")          
    except ValueError:
        system('cls')
        print("Opção inválida")