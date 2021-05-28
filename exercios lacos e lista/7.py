lista = []
vezes = []
for i in range(10):
    numba=int(input("Type your number: "))
    lista.append(numba)
print(lista)

for i in range(10):
    counter = lista.count(lista[i]) 
    if counter > 1 and lista[i] not in vezes:
        vezes.append(lista[i])

for i in range(len(vezes)):
    print("{} - {} vezes".format(vezes[i],lista.count(vezes[i])))

    



