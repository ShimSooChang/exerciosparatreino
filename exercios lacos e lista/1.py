div3 = []
div2 = []
arg = []
for lista in range(7):
    num=int(input("Digite seu um numero:\n"))
    arg.append(num)

for iten in arg:
    if iten%2 == 0:
        div2.append(iten)
        
    elif iten%3 == 0:
        div3.append(iten)
        

print("Divisiveis por 2 {} e divisiveis por 3 {}".format(div2,div3))

