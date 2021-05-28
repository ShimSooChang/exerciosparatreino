
listap = []
negative = 0
for i in range(10):
    numb=int(input("Type your number: "))
    if numb < 0:
        negative +=1
    else:
        listap.append(numb)

print("theres {} negative numbers and the sum of all positive is {}".format(negative,sum(listap)))










