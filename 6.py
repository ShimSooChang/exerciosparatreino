print("\nVerificador de triangulo")
lado1=int(input("Digite o primeiro lado do triangulo:\n"))
lado2=int(input("Digite o segundo lado do triangulo:\n"))
lado3=int(input("Digite o terceiro lado do triangulo:\n"))

if lado1 == lado2 == lado3:
    print("equilatero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("isósceles")
else:
    print("escaleno.")
