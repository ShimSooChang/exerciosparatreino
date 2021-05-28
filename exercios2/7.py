
num = int(input("Digite o numero para ser descoberto: "))
num_dig = int
cont = 0
while  num != num_dig:
       cont += 1
       num_dig = int(input("Descubra o numer: "))
       if num_dig > num:
              print("***CHUTOU ALTO***")
       elif num_dig < num:
              print("***CHUTOU BAXIO***")
       elif num_dig == num:
              print("*** ACERTOU! PARABÉNS! VOCÊ PRECISOU DE ",cont," CHANCES **")
            


    
    
    