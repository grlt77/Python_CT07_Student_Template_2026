#print("Hello from lesson 7")
#list1 = ["apple","banana","cherry"]
#list2 = ["durian","blueberry","figs"]
#list3 = list1 + list2
#print(list3)


#list1 = [3.20, 2.65, 1.75]
#list2 = [6.15, 5.45, 4.20]
#list3 = list1 + list2
#print(list3)
#sortedlist3 = sorted(list3)
#print(sortedlist3)


#fruits = ["Apple", "Banana", "Cherry", "Durian", "Elderberry", "Figs"]
#print(fruits)
#slice = fruits[0:3]
#print(slice)


#fruits = ["Apple", "Banana", "Cherry", "Durian", "Elderberry", "Figs"]
#hi = len(fruits)
#hii = hi//2
#split1 = fruits[:hii]
#split2 = fruits[hii:]
#print(split1)
#print(split2)


list1 = ["Apple", "Banana", "Cherry", "Durian"]
list2 = ["Cherry", "Durian", "Elderberry", "Figs"]
common = []
for item in list1:
    if item in list2:
        common.append(item)
print(common)