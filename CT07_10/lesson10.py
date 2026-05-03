# num = input("put in a number ")

# def is_even(num):
#     if num % 2 == 0:
#         print("its even")
#     else:
#         print("not even")

# is_even()

# age = input("what is your age? ")

# def age_group(age):
#     if age <= 13:
#         print("ur a child")
#         break
#     elif age >= 14 and age <= 20:
#         print("ur a teen")
#         break
#     elif age >= 21 and age <= 64 :
#         print("ur a adult")
#         break 
#     else:
#         print("ur a senior")
#         break

# num1 = int(input("choose a number "))

# def quad(num1):
#     num2 = num1 * 4
#     print(num2)

# quad(num1)

# def squared(num):
#     return num * num

# print(squared(5))

# def add_Square(num1,num2):
#     return squared(num1) + squared(num2)

# print(add_Square(5,7))

import turtle

screenwidth = 300
screenheight = 500
dx = 2
dy = 2

def setup_screen(screenwidth,screenheight):
    window = turtle.Screen()
    window.setup(screenwidth,screenheight)
    return window

def create_greenturtle():
    t = turtle.Turtle()
    t.shape("turtle")
    t.color("green")
    # t.penup()
    return t

def move_turtle(t,dx,dy):
    t.setx(t.xcor() + dx)
    t.sety(t.ycor() + dy)

def check_x(t,screenwidth):
    if t.xcor() > (screenwidth/2) or t.xcor() < (-screenwidth/2):
        return True

def check_y(t,screenheight):
    if t.ycor() > (screenheight/2) or t.ycor() < (-screenheight/2):
        return True
    
window = setup_screen(screenwidth,screenheight)
t = create_greenturtle()

while True:
    move_turtle(t,dx,dy)
    if check_x(t,screenwidth):
        dx *= -1
    if check_y(t,screenheight):
        dy *= -1

window.mainloop()

