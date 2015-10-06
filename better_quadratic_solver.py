import math

def quadratic_pos(a, b, c):
    if d < 0:
      return 0
    else:
      return (-b + (d ** (.5))) / (2 * a)

def quadratic_neg(a, b, c):
    if d < 0:
      return 0
    else:
      return (-b - (d ** (.5))) / (2 * a)

def vertex_x(a, b):
    return -b/(2 * a)

def vertex_y(a, b, c):
    return ((4 * a * c) - (b ** 2)) / (4 * a)
 
def print_stuff(d):
    if d < 0:
      print("There are no solutions.\nThe vertex is at (%r, %r)" % (x_coord, y_coord))
    elif d == 0:
      print("There is exactly one solution. x = %r\nThe vertex is at (%r, %r)" % (x_pos, x_coord, y_coord))
    else:
      print("The solutions are: x = %r, %r\nThe vertex is at (%r, %r)" % (x_pos, x_neg, x_coord, y_coord))
      
def open_up_or_down(a):
    if a > 0:
      print("The parabola opens upward")
    else:
      print("The parabola opens downward")

print("enter the constants:")

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

d = (b * b) - (4 * a * c )

x_pos = quadratic_pos(a, b, c)
x_neg = quadratic_neg(a, b, c)

x_coord = vertex_x(a, b)
y_coord = vertex_y(a, b, c)

print_stuff(d)
open_up_or_down(a)

def plug_in_abc(a, b, c, new_number):
    return a * new_number ** 2 + b * new_number + c    

from turtle import *
import time

bgcolor('black')   # makes the background color black
pencolor('blue')   # makes the pen blue
penup()            # lifts the pen up
setposition(-200, 0)  

pendown()     # sets the pen down
fd(400) # moves foreward 400 units
penup()

setposition(0, -200) # goes to (0, -200)
lt(90) # turn left 90 degrees
pendown() # sets the pen down
fd(400) # moves foreward 400 units
penup() # lifts the pen up

setposition(-221, -5);  write("x   <")          # writes intervals in the grid
setposition(-200, -20); write("-20");  penup()
setposition(-150, -20); write("-15");  penup()
setposition(-100, -20); write("-10");  penup()
setposition(-50, -20);  write("-5");   penup()
setposition(50, -20);   write("5");    penup()
setposition(100, -20);  write("10");   penup()
setposition(150, -20);  write("15");   penup()
setposition(200, -20);  write("20");   penup()
setposition(200, -7);   write(">");    penup()


setposition(-1, -206);   write("v");     penup()
setposition(-20, -200);  write("-20");   penup()
setposition(-20, -150);  write("-15");   penup()
setposition(-20, -100);  write("-10");   penup()
setposition(-20, -50);   write("-5");    penup()
setposition(-20, 50);    write("5");     penup()
setposition(-20, 100);   write("10");    penup()
setposition(-20, 150);   write("15");    penup()
setposition(-20, 200);   write("20");    penup()
setposition(-1, 191);    write("^  y")

colormode(255)
pencolor((200, 30, 75))
setposition(0, 0)

for x in range(1, 2):   # performs the while loop once
    new_number = -20   # starts at -200
    while new_number < 20:   #goes to 200
        y_position = plug_in_abc(a, b, c, new_number)
        setposition(new_number * 10, y_position * 10)
        dot()
        penup()
        new_number += 0.2
       

pencolor(30, 220, 20)    # puts a dot at the vertex and writes the coordinates
penup()
setposition(x_coord * 10, y_coord * 10);       dot();                   penup()
setposition(x_coord * 10, y_coord * 10 - 20);   write("(%2.2f, %2.2f)" % (x_coord, y_coord)); penup()

pencolor(180, 230, 20)    # puts dots on the x-intercepts and writes the coordinates
setposition(x_pos * 10, 0); dot()
#x_pos *= 10
setposition(x_pos * 10 + 2, -20); write("(%2.2f, %2.2f)" % (x_pos, 0)); penup()
pencolor(30, 230, 150)
setposition(x_neg * 10, 0); dot()
#x_neg *= 10
setposition(x_neg * 10 - 15, -20); write("(%2.2f, %2.2f)" % (x_neg, 0)); penup()

penup()
setposition(0, 0)
exitonclick()
