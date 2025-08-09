menu = {
    "café": ["Café, Água quente", 3.00],
    "leite": ["Leite", 1.50],
    "açúcar": ["Açúcar", 0.50],
    "torta": ["Farinha, Queijo, Ovo, Leite, Óleo", 8.00],
    "coxinha": ["Farinha, Leite, Ovo, Frango", 8.50],
    "quibe": ["Trigo, Carne moída", 3.50],
    "pastel": ["Trigo, Água, Frango", 5.50],
    "empada": ["Trigo, Ovo, Manteiga", 7.50],
    "chá gelado": ["Água, Mate, Gelo", 3.00],
    "suco": ["Água, Polpa", 5.50]
}

total = 0
pedido = []

print("Bem vindo!")

while True:
    print("Menu:")
    for i in menu:
        print(i, "-", menu[i][1])

    escolha = input("Produto ou sair: ")
    escolha = escolha.lower()

    if escolha == "sair":
        break

    if escolha in menu:
        print("Escolheu:", escolha)
        print("Ingredientes:", menu[escolha][0])
        total = total + menu[escolha][1]
        pedido.append(escolha)
        print("Total parcial:", total)
    else:
        print("Produto não achado.")

print("Pedido final:")
for i in pedido:
    print(i, "-", menu[i][1])

print("Total a pagar:", total)
