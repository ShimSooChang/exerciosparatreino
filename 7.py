nome=str(input("digite o nome do aluno: "))
nota1=int(input("qual é a primeira nota: "))
nota2=int(input("qual é a segunda nota: "))
nota3=int(input("qual é a terceira nota: "))
freq=int(input("numero de faltas: "))

notafin=int((nota1 + nota2 + nota3) /3 )
if freq <= 20:
    if notafin >= 7:

        print("aluno ",nome, " aprovado")
    
    else:
        print("aluno",nome,"reprovado")
else:
    print("aluno",nome,"reprovado")