janela = [0]*24
corredor = [0]*24
posi = 1
while True:
    opc=int(input("Digite a opção para escolher a funcionalidade \n 1 = Vender passagem \n 2 = Cancelar passage\n 3 = Mostrar Mapa de lugares \n 4 = SAIR\n:  "))
    while opc != 1 and opc != 2 and  opc != 3 and opc !=4:
        opc=int(input("Digite somente 1,2,3,4:\n"))

    if opc == 1:
        qual=int(input("DIGITE 1 PARA JANELA OU 2 para corredor?\n"))
        if qual == 1:
            if 0 not in janela:
                print("Todos lugares ocupados na janela")
            elif 0 in janela:      
                if qual == 1:
                    num=int(input("Digite o numero lugar no onibus para compra na janela : "))
                    lugar = janela[num-1]
                    if lugar == 1:
                        print("Lugar ocupado venda não realizada")
                    else:
                        print("Compra realizada com succeso")
                        janela.insert(num-1,1)
        elif qual == 2:
            if 0 not in corredor:
                print("Todos lugares ocupados na corredor")
            elif 0 in corredor:      
                if qual == 2:
                    num=int(input("Digite o numero lugar no onibus para compra no corredor : "))
                    lugar = corredor[num-1]
                    if lugar == 1:
                        print("Lugar ocupado venda nao realizada")
                    else:
                        print("Compra realizada com succeso")
                        corredor.insert(num-1,1)    
    elif opc == 2:
        qual=int(input("DIGITE 1 PARA JANELA ou 2 para o corredor? para cancelar a compra\n"))
        if qual == 1:
            if 1 not in janela:
                print("Todos lugares Descoupados na janela")
            elif 1 in janela:      
                if qual == 1:
                    num=int(input("Digite o numero lugar no onibus para cancelamento da compra: "))
                    lugar = janela[num-1]
                    if lugar == 0:
                        print("Poltrona livre. Compra não cancelada!")
                    else:
                        print("Compra canelada")
                        janela.insert(num-1,0)
        elif qual == 2:
            if 1 not in corredor:
                print("Todos lugares Descoupados no corredor")
            elif 1 in corredor:      
                if qual == 2:
                    num=int(input("Digite o numero lugar no onibus para cancelamento da compra: "))
                    lugar = corredor[num-1]
                    if lugar == 0:
                        print("Poltrona livre. Compra não cancelada! -")
                    else:
                        print("Compra canelada")
                        corredor.insert(num-1,0)    
    elif opc == 3:
        print("---------Janela------------")
        for lugar in janela:
            if lugar == 0:
                str=(place)="Desocupado"
            elif lugar == 1:
                str=(place)="Ocupado"
            posi == (janela.index(lugar))
            
            print("{} - {}".format(posi,place))
            posi+=1
        print("-----------Corredor----------")
        posi = 1
        for lugar in corredor:
            if lugar == 0:
                str=(place)="Desocupado"
            elif lugar == 1:
                str=(place)="Ocupado"
            posi == (corredor.index(lugar))
           
            print("{} - {}".format(posi,place))
            posi+=1
    elif opc == 4:
        print("Finalizando o programa")
        break

                