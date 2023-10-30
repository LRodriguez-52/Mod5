#Lorraine Rodriguez
#10/29/2023

#Problem 1 – Consider a program that prints “Hello World” to the screen 100 times.
#Use draw.io to draw the flow of execution.
#Then write the program. Submit both the flowchart and the code.

for i in range (0,100):
    print("Hello World")

#Problem 2 – Assume you have a list of numbers 12, 10, 32, 3, 66, 17, 42, 99, 20.
#a. Write a loop that prints each of the numbers on a new line.
#b. Write a loop that prints each number and its square on a new line.


num=[12, 10, 32, 3, 66, 17, 42, 99, 20]
for number in num:
    print(number)

num=[12, 10, 32, 3, 66, 17, 42, 99, 20]
for number in num:
    print(number ** 2)

#Problem 3 - Write a program that asks the user for the number of sides,
#the length of the side, he color of the line, and the fill color of a
#regular polygon. The program should draw the polygon and then fill it in.

import turtle
wn = turtle.Screen()
user = turtle.Turtle()

sides = [int(input("How many sides does a polygon have?"))]
length = int(input("What is the length of each side?"))
line_color = input ("What is the color of the line?")
fill_color = input ("What is the fill color of the polygon?")

user.colorline = (line_color)
user.colorfill = (fill_color)

user.begin_fill()

for i in range(sides[0]):
    user.color(line_color)
    user.forward(length)
    user.left(90)
    user.color(fill_color)

user.end_fill()

#Problem 4:Problem 4 – Consider a program that iterates the integers from 1 to 50.
#For multiples of three print “Divisible by three” instead of the number and for the
#multiples of five print “Divisible by five”. For numbers which are multiples of both
#three and five print “Divisible by both”. Use draw.io to draw the flow of execution.
#Then write the program. Submit both the flowchart and the code.



n = 40
if n%3 == 0: 
    print('Divisible by3!')
else:
    print('Not divisible by 3!')


for n in range(0,51):
    if n%3 == 0:
        print('Divisible by 3!')
    if n%5 == 0:
        print('Divisible by 5!')
    if n%3 == 0 and n%5 ==0:
        print('Divisible by both!')
    else:
        print("Not Divided by 3 or 5!")


#Problem5:

import turtle
wn = turtle.Screen()
lr = turtle.Turtle()
lr.color("black")
lr.pensize(1)


lr2 = turtle.Turtle()
lr2.color("black")

dr = turtle.Turtle()
dr.color("black")

wdw = turtle.Turtle()
wdw.color("black")

fen = turtle.Turtle()
fen.color("black")


lr.forward(50)
lr.left(90)
lr.forward(50)
lr.left(45)
lr.forward(35)
lr.left(45)
lr.left(45)
lr.forward(35)
lr.left(45)
lr.forward(50)

dr.forward(10)
dr.left(90)
dr.forward(25)
dr.right(90)
dr.forward(10)
dr.right(90)
dr.forward(25)


lr2.backward(50)
lr2.left(90)
lr2.forward(50)
lr2.right(90)
lr2.forward(50)

fen.backward(50)
fen.left(90)
fen.forward(25)
fen.left(45)
fen.forward(10)
fen.left(45)
fen.left(45)
fen.forward(10)
fen.left(45)
fen.forward(25)
fen.right(90)
fen.right(1)
fen.right(90)
fen.forward(25)
fen.left(45)
fen.forward(10)
fen.left(45)
fen.left(45)
fen.forward(10)
fen.left(45)
fen.forward(25)
fen.right(90)
fen.right(1)
fen.right(90)
fen.forward(25)
fen.left(45)
fen.forward(10)
fen.left(45)
fen.left(45)
fen.forward(10)
fen.left(45)
fen.forward(25)
fen.right(90)
fen.right(1)
fen.right(90)
fen.forward(25)








    
