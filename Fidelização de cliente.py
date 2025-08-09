clientes = {}

while True:
    print("1 - Cadastrar cliente")
    print("2 - Adicionar pontos")
    print("3 - Ver pontos")
    print("4 - Resgatar pontos")
    print("5 - Sair")

    escolha = input("Escolha: ")

    if escolha == "1":
        nome = input("Nome: ")
        nome = nome.lower()
        if nome in clientes:
            print("Já existe")
        else:
            clientes[nome] = 0
            print("Cadastrado")

    elif escolha == "2":
        nome = input("Nome: ")
        nome = nome.lower()
        if nome in clientes:
            valor = input("Valor: ")
            pontos = int(float(valor))
            clientes[nome] = clientes[nome] + pontos
            print("Pontos adicionados")
        else:
            print("Cliente não achado")

    elif escolha == "3":
        nome = input("Nome: ")
        nome = nome.lower()
        if nome in clientes:
            print("Pontos:", clientes[nome])
        else:
            print("Cliente não achado")

    elif escolha == "4":
        nome = input("Nome: ")
        nome = nome.lower()
        if nome in clientes:
            pontos = input("Pontos: ")
            pontos = int(pontos)
            if pontos <= clientes[nome]:
                clientes[nome] = clientes[nome] - pontos
                print("Pontos tirados")
            else:
                print("Não tem pontos")
        else:
            print("Cliente não achado")

    elif escolha == "5":
        break

    else:
        print("Opção errada")
