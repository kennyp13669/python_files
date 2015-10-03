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
      print"There are no solutions.\nThe vertex is at (%r, %r)" % (x_coord, y_coord)
    elif d == 0:
      print"There is exactly one solution. x = %r\nThe vertex is at (%r, %r)" % (x_pos, x_coord, y_coord)
    else:
      print"The solutions are: x = %r, %r\nThe vertex is at (%r, %r)" % (x_pos, x_neg, x_coord, y_coord)
      
def open_up_or_down(a):
    if a > 0:
      print"The parabola opens upward"
    else:
      print"The parabola opens downward"

print"enter the constants:"

a = float(raw_input("a = "))
b = float(raw_input("b = "))
c = float(raw_input("c = "))

d = (b * b) - (4 * a * c )

x_pos = quadratic_pos(a, b, c)
x_neg = quadratic_neg(a, b, c)

x_coord = vertex_x(a, b)
y_coord = vertex_y(a, b, c)




print_stuff(d)
open_up_or_down(a)
