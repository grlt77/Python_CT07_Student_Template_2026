print("Hello from lesson 1")
#check if item is paper, plastic, glass
#if item is paper put it in the paper bin
#if item is plastic, put it in the plastic bin
#if item is glass put it in the glass bin
red = 1
blue = 2
green = 3
tred = red * 3
tblue = blue * 5
tgreen = green * 4
total = tred + tblue + tgreen
print(total)

score_one = 80
score_two = 90
score_three = 75

total = score_one + score_two + score_three

average_score = total / 3

student_name = "Alex"

print("Average score for " , student_name + " is: " , average_score)


ans = int(input("enter score: "))

if ans > 74 :
    print("Grade A")
elif ans > 59 and ans < 75 :
    print("Grade B")
elif ans > 49 and ans < 60 :
    print("Grade C")
else :
    print("Fail")