lista = []

for n in range(20):
    num = input("Digite um numero inteiro: ")
    lista.append(num)

print('Maior numeor:{}, Menor numero:{}'.format(max(lista),min(lista)))