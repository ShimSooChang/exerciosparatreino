senha=int(input("Crie sua senha de 4 digitos: "))

senhaDig=int(input("Digite sua senha para validar:"))

if senha == senhaDig:
    print("sua senha esta correta e pronta")
else:
    print("sua senha está diferente da primeira")