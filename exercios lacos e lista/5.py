listpy = []
listddd = []
listboth = []
close = bool
while (close != True):
    rm=str(input("Type the ID of the sudent for python class "))
    listpy.append(rm)
    am=str(input("Do you want type another ID? use Y for yes and N for not "))
    while (am != "N") and (am != "Y"):
        am=str(input("USE ONLY Y OR N: "))
    
    if "N" in am:
        close = True
        

while (close != False):
    rm=str(input("Type the ID of the sudent for DDD class "))
    listddd.append(rm)
    am=(input("Do you want type another ID? use Y or N "))
    while (am != "N") and (am != "Y"):
        am=(input("USE ONLY Y OR N: "))
    if "N" in am:
        close = False




for i in range(len(listpy)):
    if listpy[i] in listddd:
        listboth.append(listpy[i])

for rm in listboth:
    print("the id in both classes are {}".format(rm))





