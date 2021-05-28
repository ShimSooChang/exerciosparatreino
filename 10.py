print("1.Somar dois números\n2.Raiz quadrada de um número")
opcao=int(input("Digite a opcao desejada ->>> "))

if opcao == 1:
    numero1=int(input("digite o primeiro numero: "))
    numero2=int(input("digite o segundo numero: "))
    print("a soma dos numeros é: ",(numero1 +numero2))
elif opcao == 2:
    num=input("Digite um número ->>> ")
    raiz=float(num) ** 0.5
    print("A raiz quadrada de",num, " é ",raiz)
else:
    print("Opcao incorreta")