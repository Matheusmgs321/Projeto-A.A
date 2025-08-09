estoque = dict(Café=55, Leite=30, Açúcar=40, Torta=10, Coxinha= 12, Quibe=5, Pasteis= 23, empadas=5, água=16, refrigerante=25)


def mostrar_estoque():
    for produto in estoque:
        print(f"{produto}: {estoque[produto]} unidades")

def adicionar_produto():
    nome = input("Produto: ").title()
    if nome in estoque:
        print("Produto já existe.")
    else:
        qtd = int(input("Quantidade: "))
        estoque[nome] = qtd

def atualizar_produto():
    nome = input("Produto: ").title()
    if nome in estoque:
        qtd = int(input("Nova quantidade: "))
        estoque[nome] = qtd
    else:
        print("Produto não encontrado.")

def remover_produto():
    nome = input("Produto: ").title()
    if nome in estoque:
        del estoque[nome]
    else:
        print("Produto não encontrado.")

def menu():
    while True:
        print("\n1 - Ver estoque")
        print("2 - Adicionar produto")
        print("3 - Atualizar produto")
        print("4 - Remover produto")
        print("5 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            mostrar_estoque()
        elif opcao == "2":
            adicionar_produto()
        elif opcao == "3":
            atualizar_produto()
        elif opcao == "4":
            remover_produto()
        elif opcao == "5":
            break
        else:
            print("Opção inválida.")

menu()