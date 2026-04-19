num = 0
orlist = [

]

while True:
    order = str(input("what would you like to order  "))
    str(order)
    if order != "end" :
        
        orlist.append(order)
    else:
        break



for a in orlist:
    for i in range(len(orlist)):
        print(i , ".", a)

# num = num + 1
# hi = num, ". " ,order