#print("Hello from lesson 5")

#favfood = [
#    "pasta",
#    "chicken",
 #   "cucumber",
#    "potato",
#    "pizza",
#]

#favfood.pop(2)
#print(favfood)
#favfood.append("water")
#for i in favfood:
#    print(i)

import random

#n = []
#hi = True

#for i in range (100):
#    num = random.randint(1,1000)
#    if num not in n:
#       n.append(num)
#    else:
#        while num in n:
#            num = random.randint(1,1000)
#        n.append(num)

#print (n)

#print(max(n))
#print(min(n))

namelist = ["Olivia", "Liam", "Emma", "Noah", "Ava", "Ethan",
            "Sophia", "Lucas", "Mia", "Aiden"
            ]
heightlist = [160, 165, 158, 170, 162, 168, 159, 172, 164, 166]
tallh = max(heightlist)
tallhin = heightlist.index(tallh)
print(tallh)
print()



pokemons = [
    "Pikachu", "Charizard", "Bulbasaur", "Squirtle",
    "Jigglypuff", "Meowth", "Psyduck", "Eevee", "Snorlax",
    "Mewtwo", "Lapras", "Gengar", "Dragonite", "Machamp",
    "Arcanine", "Alakazam", "Gyarados", "Vaporeon", "Scyther",
    "Electabuzz"
]

powers = [
    55, 84, 49, 48, 45,
    45, 52, 55, 110, 110,
    85, 65, 134, 130, 110,
    50, 125, 65, 110, 83
]

poke1 = random.choice(pokemons)
poke2 = random.choice(pokemons)

print (poke1)
while poke2 == poke1:
    poke2 = random.choice
print(poke2)

poke1in = pokemons.index(poke1)
print(poke1in)
poke2in = pokemons.index(poke2)
print(poke2in)

poke1pow = powers[poke1in]
poke2pow = powers[poke2in]

if poke1pow < poke2pow:
    print(poke2 , "won!! With " , poke2pow)
elif poke1pow > poke2pow:
    print(poke1 , "won!! With " , poke1pow)
else:
    print(poke1 , " and " , poke2 , " are tied")