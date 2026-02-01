print("Hello from lesson 4")

import time 
#a = 10
#while True:
#    print(a)
 #   time.sleep(1)
##    a = a - 1
#    if a == 0:
#        print ("happy new year")
#        break

#planets = [
#    "Mercury",
#     "Earth", 
#     "Mars", 
#     "Jupiter",
#     "Saturn", 
#     "Uranus", 
#     "Neptune"
#]

#planets[3] = "hello"
#print(planets)
#planets.append("pluto") 
#planets.insert(3,"lalaland")
#print(planets)
#
##    print(i)
#    if i == "Earth":
#        print ("this is my home")
#    elif i == "hello":
#        print ("i conqered this")
#    elif i == "lalaland":
#        print ("i created this")

#con = []
#while True:
 #   add = input("what country do u wanna go? ")
 #   if add == "end":
#        break
#    else:
#        con.append(add)
#
#for i in con:
#    print(" i want to go " , i)

menu = []
while True:
    food = input("add wut in menu ")
    if food == "end":
        print(menu)
        break
    else:
        menu.append(food)

while True:
    cusin = input (" what do u wanna eat? ")
    for menu in cusin:
        if menu == cusin:
            print ("yes we have that")
        else :
            print ("no we dont sell that bye")