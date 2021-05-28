num = int(input("Digite um número para saber se é primo: "))
cont = 0
x = 0

while x <= num or cont < 2:
    x += 1
    d = num % x
    if d == 0:
        cont += 1

if cont <= 2:
    print("é numero primo")
else:
    print("não é primo")
    