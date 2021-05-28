vendedor = []
total = []
perc = []

for i in range(3):
    nome=str(input("Digite o nome do vendedor: "))
    vendedor.append(nome)
    tot=float(input("Digite o o valor vendido pelo vendedor: "))
    total.append(tot)
    porc=float(input("Digite o percentual de comissão do vendedor: "))
    perc.append(total[i]*porc/100)


for i in range(len(vendedor)):
    print("O vendedor {} possui {} $ de comissão e o total de {} vendas".format(vendedor[i],perc[i],total[i]))


print("O total de vendas é {} ".format(sum(total)))

print("O maior valor de vendas é {} para o vendedor {}" .format(max(perc),vendedor[perc.index(max(perc))]))
print("O maior valor de vendas é {} para o vendedor {}" .format(min(perc),vendedor[perc.index(min(perc))]))






