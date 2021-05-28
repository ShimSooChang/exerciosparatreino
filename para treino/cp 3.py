

serie_2 = []
serie_rm2 = []
serie_3 = []
serie_rm3 = []
serie_4 = []
serie_rm4 = []
serie_5 = []
serie_rm5 = []
#Matutino
segunda = []
terca = []
quarta= []
quinta= []
sext = []
#Vespertino
segundaV = []
tercaV = []
quartaV= []
quintaV= []
sextV = []


def cadastro_aln():
    num_a=int(input("Digite o número de alunos a serem cadastrados ->>>> "))
    for i in range(num_a):
        rm=int(input("Digite o rm do aluno somente em números: "))
        if  rm in serie_rm2 or rm in serie_rm3 or rm in serie_rm4 or rm in serie_rm5:
            print("RM já cadastrado voltando ao menu")
            break
        elif rm == 0:
            print("Cadstros concluidos")
            break
        serie=int(input("Digite a serie do aluno, somente o número: "))
        while serie > 5 or serie < 2 :
            serie=int(input("Serie não existente digite a serie novamente:  "))
        nome=str(input("Digite o nome do aluno: "))
        
            
        if serie == 2:
            serie_2.append(nome)
            serie_rm2.append(rm)
        elif serie == 3:
            serie_3.append(nome)
            serie_rm3.append(rm)
        elif serie == 4:
            serie_4.append(nome)
            serie_rm4.append(rm)
        elif serie == 5:
            serie_5.append(nome)
            serie_rm5.append(rm)
        


def fzr_inscr():

    
    rm=int(input("Digite o rm do aluno a ser inscrito: "))
    if rm in serie_rm2 or rm in serie_rm3 or rm in serie_rm4 or rm in serie_rm5:
        if rm in serie_rm2:
            print("1 - Criar e contar histórias - Segunda feira Matutino \n 2 - A língua de sinais - Quarta feira Matutino \n 3 - O mundo da imaginção - Quarta feira Vespertino \n 4 - Criando e recriando com emojis - Sexta feira Vespetino")
            print("Na primeira opção ja foram {} pessoas inscritas, na segunda são {} pessoas inscritas, na terceira {} pessoas inscritas e na quarta são {} pessoas inscritas".format(len(segunda),len(quarta),len(quartaV),len(sextV)))
            opc=int(input("Qual opção quer se inscrever?: "))
            if opc == 1 and rm not in segunda and len(segunda) < 10:
                segunda.append(rm)
                print("Inscrição realizada com sucesso")
            elif opc == 2 and rm not in quarta and len(quarta) < 10:
                quarta.append(rm)
                print("Inscrição realizada com sucesso")
            elif opc == 3 and rm not in quartaV and len(quartaV) < 10:
                quintaV.append(rm)
                print("Inscrição realizada com sucesso")
            elif opc == 4 and rm not in sextV and len(sextV) < 10:
                sextV.append(rm)
                print("Inscrição realizada com sucesso")
            else:
                print("ERRO - Opção invalida ou aluno já registrado na atividade")
        elif rm in serie_rm3:
            print("1 - Criar e contar histórias - Segunda feira Matutino \n 2 - Teatro - Terça feira Matutino \n 3 - A língua de sinais - Quarta feira Matutino \n 4 - O corpo fala - Terça feira Vespertino")
            print("Na primeira opção ja foram {} pessoas inscritas, na segunda são {} pessoas inscritas, na terceira {} pessoas inscritas e na quarta são {} pessoas inscritas".format(len(segunda),len(terca),len(quarta),len(tercaV)))
            opc=int(input("Qual opção quer se inscrever?: "))
            if opc == 1 and rm not in segunda and len(segunda) < 10:
                segunda.append(rm)
                print("Inscrição realizada com sucesso")
            elif opc == 2 and rm not in terca and len(terca) < 10:
                terca.append(rm)
                print("Inscrição realizada com sucesso")
            elif opc == 3 and rm not in quarta and len(quarta) < 10:
                quarta.append(rm)
                print("Inscrição realizada com sucesso")
            elif opc == 4 and rm not in tercaV and len(tercaV) < 10:
                tercaV.append(rm)
                print("Inscrição realizada com sucesso")
            else:
                print("ERRO - Opção invalida ou aluno já registrado na atividade")
        elif rm in serie_rm4:
            print("1 - Teatro - Terça feira Matutino \n 2 - Lingua de sinais - Quarta feira Matutino \n 3 - Expressão Artística - Quinta feira Matutino \n 4 - Leitura dramática - Segunda feira feira Vespertino")
            print("Na primeira opção ja foram {} pessoas inscritas, na segunda são {} pessoas inscritas, na terceira {} pessoas inscritas e na quarta são {} pessoas inscritas".format(len(terca),len(quarta),len(quinta),len(segundaV)))
            opc=int(input("Qual opção quer se inscrever?: "))
            if opc == 1 and rm not in terca and len(terca) < 10:
                terca.append(rm)
                print("Inscrição realizada com sucesso")
            elif opc == 2 and rm not in quarta and len(quarta) < 10:
                quarta.append(rm)
                print("Inscrição realizada com sucesso")
            elif opc == 3 and rm not in quinta and len(quinta) < 10:
                quinta.append(rm)
                print("Inscrição realizada com sucesso")
            elif opc == 4 and rm not in segundaV and len(segundaV) < 10:
                segundaV.append(rm)
                print("Inscrição realizada com sucesso")
            else:
                print("ERRO - Numero de inscricões para a atividade está no maximo ou aluno já registrado na atividade")
        elif rm in serie_rm5:
            print("1 - A língua de sinais - Quarta feira Matutino \n 2 - Expressão artistica - Quinta feira Matutino \n 3 - Soletrando - Sexta feira Matutino \n 4 - Leitura dinamica - Qunita feira feira Vespertino")
            print("Na primeira opção ja foram {} pessoas inscritas, na segunda são {} pessoas inscritas, na terceira {} pessoas inscritas e na quarta são {} pessoas inscritas".format(len(quarta),len(quinta),len(sext),len(quintaV)))
            opc=int(input("Qual opção quer se inscrever?: "))
            if opc == 1 and rm not in quarta and len(quarta) < 10:
                quarta.append(rm)
                print("Inscrição realizada com sucesso")
            elif opc == 2 and rm not in quinta and len(quinta) < 10:
                quinta.append(rm)
                print("Inscrição realizada com sucesso")
            elif opc == 3 and rm not in sext and len(sext) < 10:
                sext.append(rm)
                print("Inscrição realizada com sucesso")
            elif opc == 4 and rm not in quintaV and len(quintaV) < 10:
                quintaV.append(rm)
                print("Inscrição realizada com sucesso")
            else:
                print("ERRO - Numero de inscricões para a atividade está no maximo ou aluno já registrado na atividade")








while True:
    print("1 Cadastrar alunos \n 2 Fazer inscrições \n 3 Listar inscrições \n 4 - Sair ")
    opc=int(input("Digite o numero para operção ->>> "))
    while opc < 1 or opc > 4:
         opc=int(input("Digite o numero  entre 1 a 4 para operção ->>> "))
    if opc == 1:
        cadastro_aln()
    elif opc == 2:
        fzr_inscr()
    elif opc == 4:
        break