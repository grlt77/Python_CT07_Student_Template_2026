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


for i in orlist:
    print((int(i) + 1) , ".", order)

# num = num + 1
# hi = num, ". " ,order