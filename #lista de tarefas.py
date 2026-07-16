#lista de tarefas
tarefas = ["Estudar", "Treinar", "Lavar louça"]


while True:
    # Exibe a lista atual de forma simples
    print(f"\nLista atual: {tarefas}")
    # Exibe o menu de opções
    print("--- MENU DE OPÇÕES ---")
    print("1. Adicionar no final ")
    print("2. Inserir no início")
    print("3. Remover pelo nome ")
    print("4. Remover o último da lista ")
    print("5. Remover a lista")
    print("6. Sair")
    #Escolher o opção
    opcao = input("Escolha uma opção (1 a 5): ")
    # Se o usuario escolher a opção 1: adicionar uma nova tarefa
    if opcao == '1':
        item = input("Digite a nova tarefa: ")
        tarefas.append(item)
        print(f"'{item}' adicionado!")
    #Se o usuario escolher a opção 2: Inserir tarefa no inicio da lista
    elif opcao == '2':
        item = input("Digite a tarefa prioritária para o início: ")
        tarefas.insert(0, item)
        print(f"'{item}' inserido no início!")
    #Se o usuario escolher a opção 3: Remover tarefa
    elif opcao == '3':
        item = input("Digite o nome exato da tarefa que quer remover: ")
        if item in tarefas:
            tarefas.remove(item)
            print(f"'{item}' removido com sucesso!")
        else:
            print("Tarefa não encontrada na lista.")
    # Se o usuario escolher a opção 4: Remover o ultimo item da lista
    elif opcao == '4':
        if len(tarefas) > 0:
            removido = tarefas.pop()
            print(f"'{removido}' foi retirado da lista!")
        else:
            print("A lista já está vazia.")
    # Se o usuario escolher a opção 5: Remover a lista
    elif opcao == '5':
        tarefas.clear()
        print("A lista foi removida")
    #Se o usuario escolher a opção: Encerrar programa
    elif opcao == '6':
        print("Programa encerrado!")
        break
    #Se não opção invalida
    else:
        print("Opção inválida! Digite um número de 1 a 6.")
