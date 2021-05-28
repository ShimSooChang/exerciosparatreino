quantPrato=int(input("Digite o total de pratos da mesa ---->: "))
while quantPrato <= 0:
     quantPrato=int(input("Número de pratos principais inválido. Digite novamente --->: "))

valorT=float(input("Digite o valor em reais da nota da mesa ---->: "))
while valorT <= 0:
     valorT=float(input("Valor inválido. Digite novamente --->: "))

valorSemDis=float(valorT)


cupomValido=str(input("Digite S para sim e N para não. \nPossue um cumpom valido ----->:"))

while cupomValido != "S" and cupomValido != "N":
    cupomValido=str(input("Digite somente S para sim e N para não --->: "))

nomeCupom=str

while cupomValido == "S" and nomeCupom != "BORALA10" and nomeCupom != "BORALA05":
    nomeCupom=str(input("Digite o nome do cupom ---->: "))
    if nomeCupom != "BORALA10" and nomeCupom != "BORALA05" and cupomValido == "S":
        print("Cupom inválido")
        cupomValido=str(input("Digite S para sim e N para não. \nPossue um cupom VALIDO? ----->:"))
        while cupomValido != "S" and cupomValido != "N":
            cupomValido=str(input("Digite somente S para sim e N para não --->: "))
    else:
        print("Cupom aplicado")




visitaRest=str(input("Digite S para sim e N para não. \nÉ a primeria vez no restaurante? ----->:"))

while visitaRest != "S" and visitaRest != "N":
    visitaRest=str(input("Digite somente S para sim e N para não --->: "))



if quantPrato > 3:
   diconto1=float(valorT * 4/100) 
   valorT -= diconto1

if valorT > 500:
    discontov=float(valorT * 6/100)
    valorT -= discontov

if nomeCupom == "BORALA10":
    diconto2=float(valorT * 10/100)
    valorT -= diconto2

if nomeCupom == "BORALA05":
    diconto2=float(valorT * 5/100)
    valorT -= diconto2

if visitaRest == "S":
    disconto4=float(valorT * 5/100)
    valorT -= disconto4




cquantPessoa=str(input("Há mais de uma pessoa a pagar a conta? \n Digite S para sim ou N para não ->>>>>: "))
    
while cquantPessoa != "S" and cquantPessoa != "N":
    print("Valor invalido")
    cquantPessoa=str(input("Há mais de uma pessoa a pagar a conta? \n Digite S para sim ou N para não ->>>>>: "))
if cquantPessoa == "S":
    quantPep=int(input("A conta será divida em quantas pessoas?: "))
    while quantPep <= 0:
        print("Numero invalido")
        quantPep=int(input("A conta será divida em quantas pessoas?: "))
    print("-------------------------------")
    print("Valor total da nota fiscal: ", valorSemDis)
    print("Valor total da nota com desconto: {0:.2f}".format(valorT))
    print("\nNúmero de pessoas: " , quantPep)
    print("Total por pessoa: {0:.2f}".format(valorT/quantPep))
    print("-------------------------------")
else:
    print("-------------------------------")
    print("Valor total da nota fiscal: ", valorSemDis)
    print("Valor total da nota com desconto: {0:.2f}".format(valorT))
    print("-------------------------------")




