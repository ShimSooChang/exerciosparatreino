lista = []
listap = []
listai = []
listan = []
for i in range(8):
    num=int(input("Digite seu numero: "))
    while (num == 0) or (num in lista):
        num=int(input("Digite seu numero sem ser 0 e não seja repitido: "))
    lista.append(num)
    if (num%2== 0) and (num > 0):
        listap.append(num)
    elif (num > 0):
        listai.append(num)
    else:
        listan.append(num)
    
   
print("TODOS {} \n POSITIVOS {} \n INPARES {} \n NEGATIVOS {} \n MAIOR NUMERO {} E MENOR NUMERO {}".format(lista,listap,listai,listan,max(lista),min(lista)))
