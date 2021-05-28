valorp=float(input("valor do produto "))
if valorp < 20:
    novo_valor = valorp + (25/100 * valorp)
    print("o valor de venda é de ",novo_valor)
else:
    novo_valor = valorp + (30/100 * valorp)
    print("o valor de venda é de ",novo_valor)
    