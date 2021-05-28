tabuada = int(0)
num = int(0)

for c in range(10):
    tabuada += 1
    for i in range(10):
        num += 1
        print( tabuada,"X",num,"=",num * tabuada )
    print("------------------")
    num = 0
    