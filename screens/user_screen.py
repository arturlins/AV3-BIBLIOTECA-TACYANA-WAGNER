def user_screen(user):
    while(True):
        print(f"Bem-vindo {user[2]}")
        print("""
        TELA USUÁRIO
        1 - Cadastrar Task
        2 - Listar Tasks
        3 - Deletar Task
        4 - Atualizar Task
        5 - Sair
        """)

        opc = input("Digite a opcao desejada: ")

        if opc == "1":
            title = input("Digite o titulo da task: ")
            create_task(usuario[0], title)
            print("Tarefa Criada!")
        elif opc == "2":
            tasks = list_tasks(usuario[0])
            print(tasks)
        elif opc == "3":
            taks_id = input("Digite o id da task: ")
            delete_task(usuario[0], taks_id)
        elif opc == "4":
            title = input("Digite o novo titulo da task: ")
            tasks_id = input("Digite o id da task: ")
            update_task(usuario[0], tasks_id, title)
        elif opc == "5":
            break