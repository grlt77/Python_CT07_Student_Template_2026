daily_sales = [1205, 986, 1354, 10535, 15741, 11200, 800, 13056, 952, 1100,
                1025, 8574, 14014, 9987, 1238, 1458, 7803, 900, 13674, 14539,
                13241, 10886, 7541, 8743, 1482, 11523, 977, 12181, 8903, 1008, 1530]

a = min(daily_sales)
b = max(daily_sales)

date_of_sales = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]

print(date_of_sales.pop(date_of_sales.index(daily_sales.index(b) + 1)),"august has the highest sales of $",b)
print(date_of_sales.pop(date_of_sales.index(daily_sales.index(a) + 1)),"august has the lowest sales of $",a)


c = sum(daily_sales)
d = c / len(daily_sales)
print("average sales for august is $",round(d,2))