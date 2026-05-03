# print("Hello from lesson 11_12_13")

# import random 

# def diceGuess(guess):
#     num = random.randint(1,6)
#     if num == guess:
#         return True
#     else:
#         return False 
    
# inputNum = input ("guess a num: ")
# if diceGuess (inputNum):
#     print("correct")
# else:
#     print ("incorrect")


import turtle

screenwidth = 300
screenheight = 300



window = turtle.Screen()
window.setup(screenwidth,screenheight)




t = turtle.Turtle()
t.shape("turtle")
t.color("green")
t.penup()

t.goto(100,300)
t.seth(270)
t.pendown()
t.forward(1000)
t.penup()
t.goto(200,300)
t.seth(270)
t.pendown()
t.forward(1000)
t.penup()
t.goto(300,100)
t.seth(360)
t.pendown()
t.forward(1000)
t.penup()
t.goto(300,200)
t.seth(360)
t.pendown()
t.forward(1000)

window.mainloop()



