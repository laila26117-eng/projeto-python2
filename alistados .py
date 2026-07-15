alistados = []

quantidade = int(input("Quantas pessoas deseja cadastrar? "))

for i in range(quantidade):
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    if idade >= 18:
        print(nome, "pode se alistar.")
        alistados.append(nome)
    else:
        print(nome, "ainda não pode se alistar.")

print("Pessoas que podem se alistar:")

for nome in alistados:
    print(nome)