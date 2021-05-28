abc = []
for numero in range(15):
    num=int(input("Digite um número "))
    abc.append(num)

 
if abc.count(30):
    print("Numero 30 aparece {} vezes".format(abc.count(30)))

index_pos = [ i for i in range(len(abc)) if abc[i] == 30 ]
print("o index de 30 na lista é: ", index_pos)

    
    
 
 
    





    
    

