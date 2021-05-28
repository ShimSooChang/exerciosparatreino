lista_nomes = []
lista_idades = []

for i in range(5):
    nome = input("Digite seu nome: ")
    lista_nomes.append(nome)
    idade = int(input("Digite sua idade: "))
    lista_idades.append(idade)

print("Pessoas com mais de 18 anos: ")

for i in range(5):
    if(lista_idades[i]>18):
        print(lista_nomes[i])