print("Hello from lesson 6")
import random
n = []
for i in range (100):
    num = random.randint(1,1000)
    if num not in n:
       n.append(num)
    else:
        while num in n:
            num = random.randint(1,1000)
        n.append(num)

print (n)

print(max(n))
print(min(n))




contacts = []
contact1 = ["John", 98453126, "john@gmail.com"]
contact2 = ["Adam", 93029102, "adam@gmail.com"]
contact3 = ["Sylvia", 87894032, "sylvia@gmail.com"]

contacts.append(contact1)
contacts.append(contact2)
contacts.append(contact3)
print(contacts)












students = [
    ["Olivia", "F"], ["Noah", "M"], ["Emma", "F"],
    ["Liam", "M"], ["Ava", "F"], ["Ethan", "M"],
    ["Sophia", "F"], ["Lucas", "M"], ["Mia", "F"],
    ["Aiden", "M"], ["Isabella", "F"], ["Jackson", "M"],
    ["Amelia", "F"], ["Logan", "M"], ["Lily", "F"]
]
b = []
g = []
for students in students:
    name.gender
