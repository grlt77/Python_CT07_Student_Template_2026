import random
hp = 100
rf = 0

print("hero starts adventure at health " ,hp)
while hp > 0:
    lhp = random.randint(1,15)
    hp = hp - lhp
    rf = rf + 1
    print ("after fighting monsters hero health is at " ,hp)
else:
    print("hero has fought " ,rf ,"battles and died")