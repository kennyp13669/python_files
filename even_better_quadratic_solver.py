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
      print("There is exactly one solution. x = %r\nThe vertex is at (%r, %r)" % (x_pos,
                                                                        x_coord, y_coord))
    else:
      print("The solutions are: x = %r, %r\nThe vertex is at (%r, %r)" % (x_pos, x_neg,
                                                                          x_coord, y_coord))
      
def open_up_or_down(a):
    if a > 0:
      print("The first parabola graphed opens upward")
    else:
      print("The parabola opens downward")

print(
    '''enter the constants of two quadratic equations\n
    (ax^2+bx+c and hx^2+ix+j)\n
    enter the constants of the lower function first:'''
    )

a = float(input("a = "));     b = float(input("b = "));    c = float(input("c = "))
h = float(input("h = "));     i = float(input("i = "));    j = float(input("j = "))

d = (b * b) - (4 * a * c )
k = (i * i) - (4 * h * j )

x_pos = quadratic_pos(a, b, c)
x_neg = quadratic_neg(a, b, c)


x_coord = vertex_x(a, b)
y_coord = vertex_y(a, b, c)

print_stuff(d)
open_up_or_down(a)

# puts the constants into equation 1
def plug_in_abc(a, b, c, new_number):
    return a * new_number ** 2 + b * new_number + c    

# puts the constants into equation 2
def plug_in_hij(h, i, j, new_number):
    return h * new_number ** 2 + i * new_number + j

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

#fillcolor(30, 60, 90)
#begin_fill()


for x in range(1, 2):   # performs the while loop once
    new_number = -20   # starts at -200
    while new_number < 20:   #goes to 200
        y_position = plug_in_abc(a, b, c, new_number)
        setposition(new_number * 10, y_position * 10)
        pendown()
        new_number += 0.2
    penup()

pencolor(200, 80, 20)   #changes the pen color

# plots the second function
for x in range(1, 2):   # performs the while loop once
    new_number = -20   # starts at -200
    while new_number < 20:   #goes to 200
        y_position = plug_in_hij(h, i, j, new_number)
        setposition(new_number * 10, y_position * 10)
        pendown()
        new_number += 0.2
    penup()

#end_fill()


pencolor(30, 220, 20)    # puts a dot at the vertex and writes the coordinates
penup()
setposition(x_coord * 10, y_coord * 10);       dot();                   penup()
setposition(x_coord * 10, y_coord * 10 - 20);   write("(%2.2f, %2.2f)" % (x_coord, y_coord)); penup()


if d > 0:
    pencolor(180, 230, 20)    # puts dots on the x-intercepts and writes the coordinates
    setposition(x_pos * 10, 0); dot()
    setposition(x_pos * 10 + 2, -20); write("(%2.2f, %2.2f)" % (x_pos, 0)); penup()
    pencolor(30, 230, 150)
    setposition(x_neg * 10, 0); dot()
    setposition(x_neg * 10 - 15, -20); write("(%2.2f, %2.2f)" % (x_neg, 0)); penup()


l = a - h; m = b - i; n = c - j  # sets both equations equal to each other
                                 # and gets everything on one side

descriminant_m = m ** 2 - 4 * l * n  # the descriminant of the intersection function

x_intersection_pos = (-m + (m ** 2 - 4 * l * n) ** 0.5) / (2 * l)
x_intersection_neg = (-m - (m ** 2 - 4 * l * n) ** 0.5) / (2 * l)

# puts dots at the intersections if the parabolas intersect
y_intersection_pos = h * x_intersection_pos ** 2 + i * x_intersection_pos + j
if descriminant_m > 0:
    setposition(x_intersection_pos * 10, y_intersection_pos * 10);        dot();    penup()

y_intersection_neg = h * x_intersection_neg ** 2 + i * x_intersection_neg + j
if descriminant_m > 0:
    setposition(x_intersection_neg * 10, y_intersection_neg * 10);        dot();    penup()

print("The points of intersection are: (%f, %f), (%f, %f)" % (
    x_intersection_neg, y_intersection_neg, x_intersection_pos, y_intersection_pos))

# puts vertical lines inside the region where the graphs intersect

pencolor(200, 200, 50)


for x in range(1, 2):          # performs this loop once
    new_number = x_intersection_neg    # starts the loop at the left intersection
    while new_number < x_intersection_pos:    # stops the loop at the right intersection
        y_position_lower = plug_in_abc(a, b, c, new_number) #of course, lower may be the 
        y_position_upper = plug_in_hij(h, i, j, new_number) # upper, and upper may be lower
        setposition(new_number * 10, y_position_lower * 10)
        pendown()
        setposition(new_number * 10, y_position_upper * 10)
        penup()
        new_number += .8

# subtracts one function from the other and integrates
def area_between_curves(l, m, n, x_intersection_pos, x_intersection_neg):
    return abs(
(l/3)*x_intersection_pos**3 + (m/2)*x_intersection_pos**2 + n*x_intersection_pos -
(
    (l/3) * x_intersection_neg**3 + (m/2) * x_intersection_neg**2 + n * x_intersection_neg
     )
        )

print("the area between the curves is %f" % area_between_curves(l, m, n,
                                                                x_intersection_pos,
                                                                x_intersection_neg))

penup()
setposition(0, 0)
exitonclick()
