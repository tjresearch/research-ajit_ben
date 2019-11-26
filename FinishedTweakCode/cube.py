import numpy as np
import copy
from tkinter import *
root = Tk()
root.geometry("330x300")
canvas = Canvas(root, width=330, height=300)
canvas.pack()
# import pygame module in this program

# activate the pygame library .
# initiate pygame and give permission
# to use pygame's functionality.

# define the RGB value
# for white, green,
# blue, black, red
# colour respectively.
grey = (200, 200, 200)
white = (255, 255, 255)
green = (102, 255, 0)
blue = (0, 0, 128)
orange = (255, 165, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)

arraycolors=['green2', 'red', 'deep sky blue', 'orange', 'white', 'yellow' ]

# assigning values to X and Y variable
X = 400
Y = 400

centerorder = ['green2', 'red', 'deep sky blue', 'orange', 'white', 'yellow']

# create the display surface object
# of specific dimension..e(X,Y).

# completely fill the surface object
# with white colour

# draw a polygon using draw.polygon()
# method of pygame.
# pygame.draw.polygon(surface, color, pointlist, thickness)
# thickness of line parameter is optional.
canvas.create_rectangle(110, 50, 130, 70, fill = 'white')
canvas.create_rectangle(50, 110, 70, 130, fill = 'orange')
canvas.create_rectangle(110, 110, 130, 130, fill = 'green2')
canvas.create_rectangle(170, 110, 190, 130, fill = 'red')
canvas.create_rectangle(230, 110, 250, 130, fill = 'deep sky blue')
canvas.create_rectangle(110, 170, 130, 190, fill = 'yellow')

canvas.create_rectangle(90, 30, 110, 50, fill = arraycolors[4])
canvas.create_rectangle(110, 30, 130, 50, fill = arraycolors[4])
canvas.create_rectangle(130, 30, 150, 50, fill = arraycolors[4])
canvas.create_rectangle(130, 50, 150, 70, fill = arraycolors[4])
canvas.create_rectangle(130, 70, 150, 90, fill = arraycolors[4])
canvas.create_rectangle(110, 70, 130, 90, fill = arraycolors[4])
canvas.create_rectangle(90, 70, 110, 90, fill = arraycolors[4])
canvas.create_rectangle(90, 50, 110, 70, fill = arraycolors[4])

canvas.create_rectangle(90, 90, 110, 110, fill = arraycolors[0])
canvas.create_rectangle(110, 90, 130, 110, fill = arraycolors[0])
canvas.create_rectangle(130, 90, 150, 110, fill = arraycolors[0])
canvas.create_rectangle(130, 110, 150, 130, fill = arraycolors[0])
canvas.create_rectangle(130, 130, 150, 150, fill = arraycolors[0])
canvas.create_rectangle(110, 130, 130, 150, fill = arraycolors[0])
canvas.create_rectangle(90, 130, 110, 150, fill = arraycolors[0])
canvas.create_rectangle(90, 110, 110, 130, fill = arraycolors[0])

canvas.create_rectangle(150, 90, 170, 110, fill = arraycolors[1])
canvas.create_rectangle(170, 90, 190, 110, fill = arraycolors[1])
canvas.create_rectangle(190, 90, 210, 110, fill = arraycolors[1])
canvas.create_rectangle(190, 110, 210, 130, fill = arraycolors[1])
canvas.create_rectangle(190, 130, 210, 150, fill = arraycolors[1])
canvas.create_rectangle(170, 130, 190, 150, fill = arraycolors[1])
canvas.create_rectangle(150, 130, 170, 150, fill = arraycolors[1])
canvas.create_rectangle(150, 110, 170, 130, fill = arraycolors[1])

canvas.create_rectangle(210, 90, 230, 110, fill = arraycolors[2])
canvas.create_rectangle(230, 90, 250, 110, fill = arraycolors[2])
canvas.create_rectangle(250, 90, 270, 110, fill = arraycolors[2])
canvas.create_rectangle(250, 110, 270, 130, fill = arraycolors[2])
canvas.create_rectangle(250, 130, 270, 150, fill = arraycolors[2])
canvas.create_rectangle(230, 130, 250, 150, fill = arraycolors[2])
canvas.create_rectangle(210, 130, 230, 150, fill = arraycolors[2])
canvas.create_rectangle(210, 110, 230, 130, fill = arraycolors[2])

canvas.create_rectangle(30, 90, 50, 110, fill = arraycolors[3])
canvas.create_rectangle(50, 90, 70, 110, fill = arraycolors[3])
canvas.create_rectangle(70, 90, 90, 110, fill = arraycolors[3])
canvas.create_rectangle(70, 110, 90, 130, fill = arraycolors[3])
canvas.create_rectangle(70, 130, 90, 150, fill = arraycolors[3])
canvas.create_rectangle(50, 130, 70, 150, fill = arraycolors[3])
canvas.create_rectangle(30, 130, 50, 150, fill = arraycolors[3])
canvas.create_rectangle(30, 110, 50, 130, fill = arraycolors[3])

canvas.create_rectangle(90, 150, 110, 170, fill = arraycolors[5])
canvas.create_rectangle(110, 150, 130, 170, fill = arraycolors[5])
canvas.create_rectangle(130, 150, 150, 170, fill = arraycolors[5])
canvas.create_rectangle(130, 170, 150, 190, fill = arraycolors[5])
canvas.create_rectangle(130, 190, 150, 210, fill = arraycolors[5])
canvas.create_rectangle(110, 190, 130, 210, fill = arraycolors[5])
canvas.create_rectangle(90, 190, 110, 210, fill = arraycolors[5])
canvas.create_rectangle(90, 170, 110, 190, fill = arraycolors[5])




# draw a line using draw.line()
# method of pygame.
# pygame.draw.line(surface, color,
# start point, end point, thickness)


# infinite loop

"""

Goal: Input original state of cube, type in sequence of moves into the command line and it makes those moves and outputs the new T-representation of the cube
Eventually

Standard: white on top, green in front

      0 1 2
      7 w 3
      6 5 4
0 1 2 0 1 2 0 1 2 0 1 2            w
7 o 3 7 g 3 7 r 3 7 b 3    =     o g r b
6 5 4 6 5 4 6 5 4 6 5 4            y
      0 1 2
      7 y 3
      6 5 4

g = 0
r = 1
b = 2
o = 3
w = 4
y = 5

cubeState is 6x8 array full of numbers 0-5 each representing the color of that square

0th element is green side
1st element is red side
2nd element is blue side
3rd element is orange side
4th element is white side
5th element is yellow side

"""
def R(cubeStateM):
    newCubeState = []
    newRight = []
    for i in range(8):
        newRight.append(cubeStateM[1][(i-2)%8])
    newCubeState.append(copy.deepcopy(cubeStateM[0]))
    newCubeState[0][2] = cubeStateM[5][2]
    newCubeState[0][3] = cubeStateM[5][3]
    newCubeState[0][4] = cubeStateM[5][4]
    newCubeState.append(copy.deepcopy(newRight))
    newCubeState.append(copy.deepcopy(cubeStateM[2]))
    newCubeState[2][0] = cubeStateM[4][4]
    newCubeState[2][7] = cubeStateM[4][3]
    newCubeState[2][6] = cubeStateM[4][2]
    newCubeState.append(copy.deepcopy(cubeStateM[3]))
    newCubeState.append(copy.deepcopy(cubeStateM[4]))
    newCubeState[4][2] = cubeStateM[0][2]
    newCubeState[4][3] = cubeStateM[0][3]
    newCubeState[4][4] = cubeStateM[0][4]
    newCubeState.append(copy.deepcopy(cubeStateM[5]))
    newCubeState[5][2] = cubeStateM[2][6]
    newCubeState[5][3] = cubeStateM[2][7]
    newCubeState[5][4] = cubeStateM[2][0]
    return newCubeState
def Rprime(cubeStateM):
    newCubeState = []
    newRight = []
    for i in range(8):
        newRight.append(cubeStateM[1][(i+2)%8])
    newCubeState.append(copy.deepcopy(cubeStateM[0]))
    newCubeState[0][2] = cubeStateM[4][2]
    newCubeState[0][3] = cubeStateM[4][3]
    newCubeState[0][4] = cubeStateM[4][4]
    newCubeState.append(copy.deepcopy(newRight))
    newCubeState.append(copy.deepcopy(cubeStateM[2]))
    newCubeState[2][0] = cubeStateM[5][4]
    newCubeState[2][7] = cubeStateM[5][3]
    newCubeState[2][6] = cubeStateM[5][2]
    newCubeState.append(copy.deepcopy(cubeStateM[3]))
    newCubeState.append(copy.deepcopy(cubeStateM[4]))
    newCubeState[4][2] = cubeStateM[2][6]
    newCubeState[4][3] = cubeStateM[2][7]
    newCubeState[4][4] = cubeStateM[2][0]
    newCubeState.append(copy.deepcopy(cubeStateM[5]))
    newCubeState[5][2] = cubeStateM[0][2]
    newCubeState[5][3] = cubeStateM[0][3]
    newCubeState[5][4] = cubeStateM[0][4]
    return newCubeState
def L(cubeStateM):
    newCubeState = []
    newLeft = []
    for i in range(8):
        newLeft.append(cubeStateM[3][(i-2)%8])
    newCubeState.append(copy.deepcopy(cubeStateM[0]))
    newCubeState[0][6] = cubeStateM[4][6]
    newCubeState[0][7] = cubeStateM[4][7]
    newCubeState[0][0] = cubeStateM[4][0]
    newCubeState.append(copy.deepcopy(cubeStateM[1]))
    newCubeState.append(copy.deepcopy(cubeStateM[2]))
    newCubeState[2][2] = cubeStateM[5][6]
    newCubeState[2][3] = cubeStateM[5][7]
    newCubeState[2][4] = cubeStateM[5][0]
    newCubeState.append(copy.deepcopy(newLeft))
    newCubeState.append(copy.deepcopy(cubeStateM[4]))
    newCubeState[4][0] = cubeStateM[2][4]
    newCubeState[4][7] = cubeStateM[2][3]
    newCubeState[4][6] = cubeStateM[2][2]
    newCubeState.append(copy.deepcopy(cubeStateM[5]))
    newCubeState[5][0] = cubeStateM[0][0]
    newCubeState[5][7] = cubeStateM[0][7]
    newCubeState[5][6] = cubeStateM[0][6]
    return newCubeState
def Lprime(cubeStateM):
    newCubeState = []
    newLeft = []
    for i in range(8):
        newLeft.append(cubeStateM[3][(i+2)%8])
    newCubeState.append(copy.deepcopy(cubeStateM[0]))
    newCubeState[0][0] = cubeStateM[5][0]
    newCubeState[0][7] = cubeStateM[5][7]
    newCubeState[0][6] = cubeStateM[5][6]
    newCubeState.append(copy.deepcopy(cubeStateM[1]))
    newCubeState.append(copy.deepcopy(cubeStateM[2]))
    newCubeState[2][4] = cubeStateM[4][0]
    newCubeState[2][3] = cubeStateM[4][7]
    newCubeState[2][2] = cubeStateM[4][6]
    newCubeState.append(copy.deepcopy(newLeft))
    newCubeState.append(copy.deepcopy(cubeStateM[4]))
    newCubeState[4][6] = cubeStateM[0][6]
    newCubeState[4][7] = cubeStateM[0][7]
    newCubeState[4][0] = cubeStateM[0][0]
    newCubeState.append(copy.deepcopy(cubeStateM[5]))
    newCubeState[5][6] = cubeStateM[2][2]
    newCubeState[5][7] = cubeStateM[2][3]
    newCubeState[5][0] = cubeStateM[2][4]
    return newCubeState
def U(cubeStateM):
    newCubeState = []
    newUp = []
    for i in range(8):
        newUp.append(cubeStateM[4][(i-2)%8])
    newCubeState.append(copy.deepcopy(cubeStateM[0]))
    newCubeState[0][0] = cubeStateM[1][0]
    newCubeState[0][1] = cubeStateM[1][1]
    newCubeState[0][2] = cubeStateM[1][2]
    newCubeState.append(copy.deepcopy(cubeStateM[1]))
    newCubeState[1][0] = cubeStateM[2][0]
    newCubeState[1][1] = cubeStateM[2][1]
    newCubeState[1][2] = cubeStateM[2][2]
    newCubeState.append(copy.deepcopy(cubeStateM[2]))
    newCubeState[2][0] = cubeStateM[3][0]
    newCubeState[2][1] = cubeStateM[3][1]
    newCubeState[2][2] = cubeStateM[3][2]
    newCubeState.append(copy.deepcopy(cubeStateM[3]))
    newCubeState[3][0] = cubeStateM[0][0]
    newCubeState[3][1] = cubeStateM[0][1]
    newCubeState[3][2] = cubeStateM[0][2]
    newCubeState.append(copy.deepcopy(newUp))
    newCubeState.append(copy.deepcopy(cubeStateM[5]))
    return newCubeState
def Uprime(cubeStateM):
    newCubeState = []
    newUp = []
    for i in range(8):
        newUp.append(cubeStateM[4][(i+2)%8])
    newCubeState.append(copy.deepcopy(cubeStateM[0]))
    newCubeState[0][0] = cubeStateM[3][0]
    newCubeState[0][1] = cubeStateM[3][1]
    newCubeState[0][2] = cubeStateM[3][2]
    newCubeState.append(copy.deepcopy(cubeStateM[1]))
    newCubeState[1][0] = cubeStateM[0][0]
    newCubeState[1][1] = cubeStateM[0][1]
    newCubeState[1][2] = cubeStateM[0][2]
    newCubeState.append(copy.deepcopy(cubeStateM[2]))
    newCubeState[2][0] = cubeStateM[1][0]
    newCubeState[2][1] = cubeStateM[1][1]
    newCubeState[2][2] = cubeStateM[1][2]
    newCubeState.append(copy.deepcopy(cubeStateM[3]))
    newCubeState[3][0] = cubeStateM[2][0]
    newCubeState[3][1] = cubeStateM[2][1]
    newCubeState[3][2] = cubeStateM[2][2]
    newCubeState.append(copy.deepcopy(newUp))
    newCubeState.append(copy.deepcopy(cubeStateM[5]))
    return newCubeState
def D(cubeStateM):
    newCubeState = []
    newDown = []
    for i in range(8):
        newDown.append(cubeStateM[5][(i-2)%8])
    newCubeState.append(copy.deepcopy(cubeStateM[0]))
    newCubeState[0][6] = cubeStateM[3][6]
    newCubeState[0][5] = cubeStateM[3][5]
    newCubeState[0][4] = cubeStateM[3][4]
    newCubeState.append(copy.deepcopy(cubeStateM[1]))
    newCubeState[1][6] = cubeStateM[0][6]
    newCubeState[1][5] = cubeStateM[0][5]
    newCubeState[1][4] = cubeStateM[0][4]
    newCubeState.append(copy.deepcopy(cubeStateM[2]))
    newCubeState[2][6] = cubeStateM[1][6]
    newCubeState[2][5] = cubeStateM[1][5]
    newCubeState[2][4] = cubeStateM[1][4]
    newCubeState.append(copy.deepcopy(cubeStateM[3]))
    newCubeState[3][6] = cubeStateM[2][6]
    newCubeState[3][5] = cubeStateM[2][5]
    newCubeState[3][4] = cubeStateM[2][4]
    newCubeState.append(copy.deepcopy(cubeStateM[4]))
    newCubeState.append(copy.deepcopy(newDown))
    return newCubeState
def Dprime(cubeStateM):
    newCubeState = []
    newDown = []
    for i in range(8):
        newDown.append(cubeStateM[5][(i+2)%8])
    newCubeState.append(copy.deepcopy(cubeStateM[0]))
    newCubeState[0][6] = cubeStateM[1][6]
    newCubeState[0][5] = cubeStateM[1][5]
    newCubeState[0][4] = cubeStateM[1][4]
    newCubeState.append(copy.deepcopy(cubeStateM[1]))
    newCubeState[1][6] = cubeStateM[2][6]
    newCubeState[1][5] = cubeStateM[2][5]
    newCubeState[1][4] = cubeStateM[2][4]
    newCubeState.append(copy.deepcopy(cubeStateM[2]))
    newCubeState[2][6] = cubeStateM[3][6]
    newCubeState[2][5] = cubeStateM[3][5]
    newCubeState[2][4] = cubeStateM[3][4]
    newCubeState.append(copy.deepcopy(cubeStateM[3]))
    newCubeState[3][6] = cubeStateM[0][6]
    newCubeState[3][5] = cubeStateM[0][5]
    newCubeState[3][4] = cubeStateM[0][4]
    newCubeState.append(copy.deepcopy(cubeStateM[4]))
    newCubeState.append(copy.deepcopy(newDown))
    return newCubeState
def F(cubeStateM):
    newCubeState = []
    newFront = []
    for i in range(8):
        newFront.append(cubeStateM[0][(i-2)%8])
    newCubeState.append(copy.deepcopy(newFront))
    newCubeState.append(copy.deepcopy(cubeStateM[1]))
    newCubeState[1][0] = cubeStateM[4][6]
    newCubeState[1][7] = cubeStateM[4][5]
    newCubeState[1][6] = cubeStateM[4][4]
    newCubeState.append(copy.deepcopy(cubeStateM[2]))
    newCubeState.append(copy.deepcopy(cubeStateM[3]))
    newCubeState[3][2] = cubeStateM[5][0]
    newCubeState[3][3] = cubeStateM[5][1]
    newCubeState[3][4] = cubeStateM[5][2]
    newCubeState.append(copy.deepcopy(cubeStateM[4]))
    newCubeState[4][4] = cubeStateM[3][2]
    newCubeState[4][5] = cubeStateM[3][3]
    newCubeState[4][6] = cubeStateM[3][4]
    newCubeState.append(copy.deepcopy(cubeStateM[5]))
    newCubeState[5][0] = cubeStateM[1][6]
    newCubeState[5][1] = cubeStateM[1][7]
    newCubeState[5][2] = cubeStateM[1][0]
    return newCubeState
def Fprime(cubeStateM):
    newCubeState = []
    newFront = []
    for i in range(8):
        newFront.append(cubeStateM[0][(i+2)%8])
    newCubeState.append(copy.deepcopy(newFront))
    newCubeState.append(copy.deepcopy(cubeStateM[1]))
    newCubeState[1][0] = cubeStateM[5][2]
    newCubeState[1][7] = cubeStateM[5][1]
    newCubeState[1][6] = cubeStateM[5][0]
    newCubeState.append(copy.deepcopy(cubeStateM[2]))
    newCubeState.append(copy.deepcopy(cubeStateM[3]))
    newCubeState[3][2] = cubeStateM[4][4]
    newCubeState[3][3] = cubeStateM[4][5]
    newCubeState[3][4] = cubeStateM[4][6]
    newCubeState.append(copy.deepcopy(cubeStateM[4]))
    newCubeState[4][4] = cubeStateM[1][6]
    newCubeState[4][5] = cubeStateM[1][7]
    newCubeState[4][6] = cubeStateM[1][0]
    newCubeState.append(copy.deepcopy(cubeStateM[5]))
    newCubeState[5][0] = cubeStateM[3][2]
    newCubeState[5][1] = cubeStateM[3][3]
    newCubeState[5][2] = cubeStateM[3][4]
    return newCubeState
def B(cubeStateM):
    newCubeState = []
    newBack = []
    for i in range(8):
        newBack.append(cubeStateM[2][(i-2)%8])
    newCubeState.append(copy.deepcopy(cubeStateM[0]))
    newCubeState.append(copy.deepcopy(cubeStateM[1]))
    newCubeState[1][2] = cubeStateM[5][4]
    newCubeState[1][3] = cubeStateM[5][5]
    newCubeState[1][4] = cubeStateM[5][6]
    newCubeState.append(copy.deepcopy(newBack))
    newCubeState.append(copy.deepcopy(cubeStateM[3]))
    newCubeState[3][0] = cubeStateM[4][2]
    newCubeState[3][7] = cubeStateM[4][1]
    newCubeState[3][6] = cubeStateM[4][0]
    newCubeState.append(copy.deepcopy(cubeStateM[4]))
    newCubeState[4][0] = cubeStateM[1][2]
    newCubeState[4][1] = cubeStateM[1][3]
    newCubeState[4][2] = cubeStateM[1][4]
    newCubeState.append(copy.deepcopy(cubeStateM[5]))
    newCubeState[5][4] = cubeStateM[3][6]
    newCubeState[5][5] = cubeStateM[3][7]
    newCubeState[5][6] = cubeStateM[3][0]
    return newCubeState
def Bprime(cubeStateM):
    newCubeState = []
    newBack = []
    for i in range(8):
        newBack.append(cubeStateM[2][(i+2)%8])
    newCubeState.append(copy.deepcopy(cubeStateM[0]))
    newCubeState.append(copy.deepcopy(cubeStateM[1]))
    newCubeState[1][2] = cubeStateM[4][0]
    newCubeState[1][3] = cubeStateM[4][1]
    newCubeState[1][4] = cubeStateM[4][2]
    newCubeState.append(copy.deepcopy(newBack))
    newCubeState.append(copy.deepcopy(cubeStateM[3]))
    newCubeState[3][0] = cubeStateM[5][6]
    newCubeState[3][7] = cubeStateM[5][5]
    newCubeState[3][6] = cubeStateM[5][4]
    newCubeState.append(copy.deepcopy(cubeStateM[4]))
    newCubeState[4][0] = cubeStateM[3][6]
    newCubeState[4][1] = cubeStateM[3][7]
    newCubeState[4][2] = cubeStateM[3][0]
    newCubeState.append(copy.deepcopy(cubeStateM[5]))
    newCubeState[5][4] = cubeStateM[1][2]
    newCubeState[5][5] = cubeStateM[1][3]
    newCubeState[5][6] = cubeStateM[1][4]
    return newCubeState
def r(cubeStateM):
    return x(L(cubeStateM))
def rprime(cubeStateM):
    return xprime(Lprime(cubeStateM))
def r2(cubeStateM):
    return r(r(cubeStateM))
def l(cubeStateM):
    return xprime(R(cubeStateM))
def lprime(cubeStateM):
    return x(Rprime(cubeStateM))
def l2(cubeStateM):
    return l(l(cubeStateM))
def u(cubeStateM):
    return y(D(cubeStateM))
def uprime(cubeStateM):
    return yprime(Dprime(cubeStateM))
def u2(cubeStateM):
    return u(u(cubeStateM))
def f(cubeStateM):
    return z(B(cubeStateM))
def fprime(cubeStateM):
    return zprime(Bprime(cubeStateM))
def f2(cubeStateM):
    return f(f(cubeStateM))
def d(cubeStateM):
    return yprime(U(cubeStateM))
def dprime(cubeStateM):
    return y(Uprime(cubeStateM))
def d2(cubeStateM):
    return d(d(cubeStateM))
def b(cubeStateM):
    return zprime(F(cubeStateM))
def bprime(cubeStateM):
    return z(Fprime(cubeStateM))
def b2(cubeStateM):
    return b(b(cubeStateM))
def M(cubeStateM):
    return R(Lprime(xprime(cubeStateM)))
def Mprime(cubeStateM):
    return Rprime(L(x(cubeStateM)))
def M2(cubeStateM):
    return M(M(cubeStateM))
def E(cubeStateM):
    return U(Dprime(yprime(cubeStateM)))
def Eprime(cubeStateM):
    return Uprime(D(y(cubeStateM)))
def E2(cubeStateM):
    return E(E(cubeStateM))
def Sprime(cubeStateM):
    return F(Bprime(zprime(cubeStateM)))
def S(cubeStateM):
    return Fprime(B(z(cubeStateM)))
def S2(cubeStateM):
    return S(S(cubeStateM))
"""
4 5 6
3   7
2 1 0
0 1 2
7   3
6 5 4


"""

"""
FIXED IT FOR x, JUST FIX FOR THE REST OF THE ROTATIONS

      0 1 2
      7 w 3
      6 5 4
0 1 2 0 1 2 0 1 2 0 1 2            w
7 o 3 7 g 3 7 r 3 7 b 3    =     o g r b
6 5 4 6 5 4 6 5 4 6 5 4            y
      0 1 2
      7 y 3
      6 5 4
"""
def x(cubeStateM):
    NewCubeState = copy.deepcopy(cubeStateM)
    NewCubeState[0] = cubeStateM[5]
    NewCubeState[1] = cubeStateM[1][-2:] + cubeStateM[1][:-2]
    NewCubeState[2] = cubeStateM[4][4:] + cubeStateM[4][:4]
    NewCubeState[3] = cubeStateM[3][2:] + cubeStateM[3][:2]
    NewCubeState[4] = cubeStateM[0]
    NewCubeState[5] = cubeStateM[2][4:] + cubeStateM[2][:4]
    return NewCubeState
def xprime(cubeStateM):
    NewCubeState = copy.deepcopy(cubeStateM)
    NewCubeState[0] = cubeStateM[4]
    NewCubeState[1] = cubeStateM[1][2:] + cubeStateM[1][:2]
    NewCubeState[2] = cubeStateM[5][4:] + cubeStateM[5][:4]
    NewCubeState[3] = cubeStateM[3][-2:] + cubeStateM[3][:-2]
    NewCubeState[4] = cubeStateM[2][4:] + cubeStateM[2][:4]
    NewCubeState[5] = cubeStateM[0]
    return NewCubeState
def y(cubeStateM):
    NewCubeState = copy.deepcopy(cubeStateM)
    NewCubeState[0] = cubeStateM[1]
    NewCubeState[1] = cubeStateM[2]
    NewCubeState[2] = cubeStateM[3]
    NewCubeState[3] = cubeStateM[0]
    NewCubeState[4] = cubeStateM[4][-2:] + cubeStateM[4][:-2]
    NewCubeState[5] = cubeStateM[5][2:] + cubeStateM[5][:2]
    return NewCubeState
def yprime(cubeStateM):
    NewCubeState = copy.deepcopy(cubeStateM)
    NewCubeState[0] = cubeStateM[3]
    NewCubeState[1] = cubeStateM[0]
    NewCubeState[2] = cubeStateM[1]
    NewCubeState[3] = cubeStateM[2]
    NewCubeState[4] = cubeStateM[4][2:] + cubeStateM[4][:2]
    NewCubeState[5] = cubeStateM[5][-2:] + cubeStateM[5][:-2]
    return NewCubeState
def z(cubeStateM):
    NewCubeState = copy.deepcopy(cubeStateM)
    NewCubeState[0] = cubeStateM[0][-2:] + cubeStateM[0][:-2]
    NewCubeState[1] = cubeStateM[4][-2:] + cubeStateM[4][:-2]
    NewCubeState[2] = cubeStateM[2][2:] + cubeStateM[2][:2]
    NewCubeState[3] = cubeStateM[5][-2:] + cubeStateM[5][:-2]
    NewCubeState[4] = cubeStateM[3][-2:] + cubeStateM[3][:-2]
    NewCubeState[5] = cubeStateM[1][-2:] + cubeStateM[1][:-2]
    return NewCubeState
def zprime(cubeStateM):
    NewCubeState = copy.deepcopy(cubeStateM)
    NewCubeState[0] = cubeStateM[0][2:] + cubeStateM[0][:2]
    NewCubeState[1] = cubeStateM[5][2:] + cubeStateM[5][:2]
    NewCubeState[2] = cubeStateM[2][-2:] + cubeStateM[2][:-2]
    NewCubeState[3] = cubeStateM[4][2:] + cubeStateM[4][:2]
    NewCubeState[4] = cubeStateM[1][2:] + cubeStateM[1][:2]
    NewCubeState[5] = cubeStateM[3][2:] + cubeStateM[3][:2]
    return NewCubeState

cubeState = []
for i in range(6):
    cubeState.append([i]*8)
print(cubeState)
while True:
    str = input()
    moves = str.split(" ") #list of moves
    for i in moves:
        if i == 'R':
            cubeState = R(cubeState)
        if i == "R'":
            cubeState = Rprime(cubeState)
        if i == 'L':
            cubeState = L(cubeState)
        if i == "L'":
            cubeState = Lprime(cubeState)
        if i == 'U':
            cubeState = U(cubeState)
        if i == "U'":
            cubeState = Uprime(cubeState)
        if i == 'D':
            cubeState = D(cubeState)
        if i == "D'":
            cubeState = Dprime(cubeState)
        if i == 'F':
            cubeState = F(cubeState)
        if i == "F'":
            cubeState = Fprime(cubeState)
        if i == 'B':
            cubeState = B(cubeState)
        if i == "B'":
            cubeState = Bprime(cubeState)
        if i == "R2":
            cubeState = R(R(cubeState))
        if i == "D2":
            cubeState = D(D(cubeState))
        if i == "L2":
            cubeState = L(L(cubeState))
        if i == "B2":
            cubeState = B(B(cubeState))
        if i == "F2":
            cubeState = F(F(cubeState))
        if i == "U2":
            cubeState = U(U(cubeState))
        if i == "x":
            cubeState = x(cubeState)
            newcenterorder = copy.deepcopy(centerorder)
            newcenterorder[0] = centerorder[5]
            newcenterorder[1] = centerorder[1]
            newcenterorder[2] = centerorder[4]
            newcenterorder[3] = centerorder[3]
            newcenterorder[4] = centerorder[0]
            newcenterorder[5] = centerorder[2]
            centerorder = copy.deepcopy(newcenterorder)
        if i == "x'":
            cubeState = xprime(cubeState)
            newcenterorder = copy.deepcopy(centerorder)
            newcenterorder[0] = centerorder[4]
            newcenterorder[1] = centerorder[1]
            newcenterorder[2] = centerorder[5]
            newcenterorder[3] = centerorder[3]
            newcenterorder[4] = centerorder[2]
            newcenterorder[5] = centerorder[0]
            centerorder = copy.deepcopy(newcenterorder)
        if i == "y":
            cubeState = y(cubeState)
            newcenterorder = copy.deepcopy(centerorder)
            newcenterorder[0] = centerorder[1]
            newcenterorder[1] = centerorder[2]
            newcenterorder[2] = centerorder[3]
            newcenterorder[3] = centerorder[0]
            newcenterorder[4] = centerorder[4]
            newcenterorder[5] = centerorder[5]
            centerorder = copy.deepcopy(newcenterorder)
        if i == "y'":
            cubeState = yprime(cubeState)
            newcenterorder = copy.deepcopy(centerorder)
            newcenterorder[0] = centerorder[3]
            newcenterorder[1] = centerorder[0]
            newcenterorder[2] = centerorder[1]
            newcenterorder[3] = centerorder[2]
            newcenterorder[4] = centerorder[4]
            newcenterorder[5] = centerorder[5]
            centerorder = copy.deepcopy(newcenterorder)
        if i == "z":
            cubeState = z(cubeState)
            newcenterorder = copy.deepcopy(centerorder)
            newcenterorder[0] = centerorder[0]
            newcenterorder[1] = centerorder[4]
            newcenterorder[2] = centerorder[2]
            newcenterorder[3] = centerorder[5]
            newcenterorder[4] = centerorder[3]
            newcenterorder[5] = centerorder[1]
            centerorder = copy.deepcopy(newcenterorder)
        if i == "z'":
            cubeState = zprime(cubeState)
            newcenterorder = copy.deepcopy(centerorder)
            newcenterorder[0] = centerorder[0]
            newcenterorder[1] = centerorder[5]
            newcenterorder[2] = centerorder[2]
            newcenterorder[3] = centerorder[4]
            newcenterorder[4] = centerorder[1]
            newcenterorder[5] = centerorder[3]
            centerorder = copy.deepcopy(newcenterorder)
        if i == "r":
            cubeState = r(cubeState)
            newcenterorder = copy.deepcopy(centerorder)
            newcenterorder[0] = centerorder[5]
            newcenterorder[1] = centerorder[1]
            newcenterorder[2] = centerorder[4]
            newcenterorder[3] = centerorder[3]
            newcenterorder[4] = centerorder[0]
            newcenterorder[5] = centerorder[2]
            centerorder = copy.deepcopy(newcenterorder)
        if i == "r'":
            cubeState = rprime(cubeState)
            newcenterorder = copy.deepcopy(centerorder)
            newcenterorder[0] = centerorder[4]
            newcenterorder[1] = centerorder[1]
            newcenterorder[2] = centerorder[5]
            newcenterorder[3] = centerorder[3]
            newcenterorder[4] = centerorder[2]
            newcenterorder[5] = centerorder[0]
            centerorder = copy.deepcopy(newcenterorder)
        if i == "r2":
            cubeState = r(r(cubeState))
            newcenterorder = copy.deepcopy(centerorder)
            newcenterorder[0] = centerorder[5]
            newcenterorder[1] = centerorder[1]
            newcenterorder[2] = centerorder[4]
            newcenterorder[3] = centerorder[3]
            newcenterorder[4] = centerorder[0]
            newcenterorder[5] = centerorder[2]
            centerorder = copy.deepcopy(newcenterorder)
            newcenterorder = copy.deepcopy(centerorder)
            newcenterorder[0] = centerorder[5]
            newcenterorder[1] = centerorder[1]
            newcenterorder[2] = centerorder[4]
            newcenterorder[3] = centerorder[3]
            newcenterorder[4] = centerorder[0]
            newcenterorder[5] = centerorder[2]
            centerorder = copy.deepcopy(newcenterorder)
        if i == "l":
            cubeState = l(cubeState)
            newcenterorder = copy.deepcopy(centerorder)
            newcenterorder[0] = centerorder[4]
            newcenterorder[1] = centerorder[1]
            newcenterorder[2] = centerorder[5]
            newcenterorder[3] = centerorder[3]
            newcenterorder[4] = centerorder[2]
            newcenterorder[5] = centerorder[0]
            centerorder = copy.deepcopy(newcenterorder)
        if i == "l'":
            cubeState = lprime(cubeState)
            newcenterorder = copy.deepcopy(centerorder)
            newcenterorder[0] = centerorder[5]
            newcenterorder[1] = centerorder[1]
            newcenterorder[2] = centerorder[4]
            newcenterorder[3] = centerorder[3]
            newcenterorder[4] = centerorder[0]
            newcenterorder[5] = centerorder[2]
            centerorder = copy.deepcopy(newcenterorder)
        if i == "l2":
            cubeState = l(l(cubeState))
            newcenterorder = copy.deepcopy(centerorder)
            newcenterorder[0] = centerorder[4]
            newcenterorder[1] = centerorder[1]
            newcenterorder[2] = centerorder[5]
            newcenterorder[3] = centerorder[3]
            newcenterorder[4] = centerorder[2]
            newcenterorder[5] = centerorder[0]
            centerorder = copy.deepcopy(newcenterorder)
            newcenterorder = copy.deepcopy(centerorder)
            newcenterorder[0] = centerorder[4]
            newcenterorder[1] = centerorder[1]
            newcenterorder[2] = centerorder[5]
            newcenterorder[3] = centerorder[3]
            newcenterorder[4] = centerorder[2]
            newcenterorder[5] = centerorder[0]
            centerorder = copy.deepcopy(newcenterorder)
        if i == "b":
            cubeState = b(cubeState)
            newcenterorder = copy.deepcopy(centerorder)
            newcenterorder[0] = centerorder[0]
            newcenterorder[1] = centerorder[5]
            newcenterorder[2] = centerorder[2]
            newcenterorder[3] = centerorder[4]
            newcenterorder[4] = centerorder[1]
            newcenterorder[5] = centerorder[3]
            centerorder = copy.deepcopy(newcenterorder)
        if i == "b'":
            cubeState = bprime(cubeState)
            newcenterorder = copy.deepcopy(centerorder)
            newcenterorder[0] = centerorder[0]
            newcenterorder[1] = centerorder[4]
            newcenterorder[2] = centerorder[2]
            newcenterorder[3] = centerorder[5]
            newcenterorder[4] = centerorder[3]
            newcenterorder[5] = centerorder[1]
            centerorder = copy.deepcopy(newcenterorder)
        if i == "b2":
            cubeState = b(b(cubeState))
            newcenterorder = copy.deepcopy(centerorder)
            newcenterorder[0] = centerorder[0]
            newcenterorder[1] = centerorder[5]
            newcenterorder[2] = centerorder[2]
            newcenterorder[3] = centerorder[4]
            newcenterorder[4] = centerorder[1]
            newcenterorder[5] = centerorder[3]
            centerorder = copy.deepcopy(newcenterorder)
            newcenterorder = copy.deepcopy(centerorder)
            newcenterorder[0] = centerorder[0]
            newcenterorder[1] = centerorder[5]
            newcenterorder[2] = centerorder[2]
            newcenterorder[3] = centerorder[4]
            newcenterorder[4] = centerorder[1]
            newcenterorder[5] = centerorder[3]
            centerorder = copy.deepcopy(newcenterorder)
        if i == "f":
            cubeState = f(cubeState)
            newcenterorder = copy.deepcopy(centerorder)
            newcenterorder[0] = centerorder[0]
            newcenterorder[1] = centerorder[4]
            newcenterorder[2] = centerorder[2]
            newcenterorder[3] = centerorder[5]
            newcenterorder[4] = centerorder[3]
            newcenterorder[5] = centerorder[1]
            centerorder = copy.deepcopy(newcenterorder)
        if i == "f'":
            cubeState = fprime(cubeState)
            newcenterorder = copy.deepcopy(centerorder)
            newcenterorder[0] = centerorder[0]
            newcenterorder[1] = centerorder[5]
            newcenterorder[2] = centerorder[2]
            newcenterorder[3] = centerorder[4]
            newcenterorder[4] = centerorder[1]
            newcenterorder[5] = centerorder[3]
            centerorder = copy.deepcopy(newcenterorder)
        if i == "f2":
            cubeState = f(f(cubeState))
            newcenterorder = copy.deepcopy(centerorder)
            newcenterorder[0] = centerorder[0]
            newcenterorder[1] = centerorder[4]
            newcenterorder[2] = centerorder[2]
            newcenterorder[3] = centerorder[5]
            newcenterorder[4] = centerorder[3]
            newcenterorder[5] = centerorder[1]
            centerorder = copy.deepcopy(newcenterorder)
            newcenterorder = copy.deepcopy(centerorder)
            newcenterorder[0] = centerorder[0]
            newcenterorder[1] = centerorder[4]
            newcenterorder[2] = centerorder[2]
            newcenterorder[3] = centerorder[5]
            newcenterorder[4] = centerorder[3]
            newcenterorder[5] = centerorder[1]
            centerorder = copy.deepcopy(newcenterorder)
        if i == "d":
            cubeState = d(cubeState)
            newcenterorder = copy.deepcopy(centerorder)
            newcenterorder[0] = centerorder[3]
            newcenterorder[1] = centerorder[0]
            newcenterorder[2] = centerorder[1]
            newcenterorder[3] = centerorder[2]
            newcenterorder[4] = centerorder[4]
            newcenterorder[5] = centerorder[5]
            centerorder = copy.deepcopy(newcenterorder)
        if i == "d'":
            cubeState = dprime(cubeState)
            newcenterorder = copy.deepcopy(centerorder)
            newcenterorder[0] = centerorder[1]
            newcenterorder[1] = centerorder[2]
            newcenterorder[2] = centerorder[3]
            newcenterorder[3] = centerorder[0]
            newcenterorder[4] = centerorder[4]
            newcenterorder[5] = centerorder[5]
            centerorder = copy.deepcopy(newcenterorder)
        if i == "d2":
            cubeState = d(d(cubeState))
            newcenterorder = copy.deepcopy(centerorder)
            newcenterorder[0] = centerorder[3]
            newcenterorder[1] = centerorder[0]
            newcenterorder[2] = centerorder[1]
            newcenterorder[3] = centerorder[2]
            newcenterorder[4] = centerorder[4]
            newcenterorder[5] = centerorder[5]
            centerorder = copy.deepcopy(newcenterorder)
            newcenterorder = copy.deepcopy(centerorder)
            newcenterorder[0] = centerorder[3]
            newcenterorder[1] = centerorder[0]
            newcenterorder[2] = centerorder[1]
            newcenterorder[3] = centerorder[2]
            newcenterorder[4] = centerorder[4]
            newcenterorder[5] = centerorder[5]
            centerorder = copy.deepcopy(newcenterorder)
        if i == "u":
            cubeState = u(cubeState)
            newcenterorder = copy.deepcopy(centerorder)
            newcenterorder[0] = centerorder[1]
            newcenterorder[1] = centerorder[2]
            newcenterorder[2] = centerorder[3]
            newcenterorder[3] = centerorder[0]
            newcenterorder[4] = centerorder[4]
            newcenterorder[5] = centerorder[5]
            centerorder = copy.deepcopy(newcenterorder)
        if i == "u'":
            cubeState = uprime(cubeState)
            newcenterorder = copy.deepcopy(centerorder)
            newcenterorder[0] = centerorder[3]
            newcenterorder[1] = centerorder[0]
            newcenterorder[2] = centerorder[1]
            newcenterorder[3] = centerorder[2]
            newcenterorder[4] = centerorder[4]
            newcenterorder[5] = centerorder[5]
            centerorder = copy.deepcopy(newcenterorder)
        if i == "u2":
            cubeState = u(u(cubeState))
            newcenterorder = copy.deepcopy(centerorder)
            newcenterorder[0] = centerorder[1]
            newcenterorder[1] = centerorder[2]
            newcenterorder[2] = centerorder[3]
            newcenterorder[3] = centerorder[0]
            newcenterorder[4] = centerorder[4]
            newcenterorder[5] = centerorder[5]
            centerorder = copy.deepcopy(newcenterorder)
            newcenterorder = copy.deepcopy(centerorder)
            newcenterorder[0] = centerorder[1]
            newcenterorder[1] = centerorder[2]
            newcenterorder[2] = centerorder[3]
            newcenterorder[3] = centerorder[0]
            newcenterorder[4] = centerorder[4]
            newcenterorder[5] = centerorder[5]
            centerorder = copy.deepcopy(newcenterorder)
        if i == "M":
            cubeState = M(cubeState)
            newcenterorder = copy.deepcopy(centerorder)
            newcenterorder[0] = centerorder[4]
            newcenterorder[1] = centerorder[1]
            newcenterorder[2] = centerorder[5]
            newcenterorder[3] = centerorder[3]
            newcenterorder[4] = centerorder[2]
            newcenterorder[5] = centerorder[0]
            centerorder = copy.deepcopy(newcenterorder)
        if i == "M'":
            cubeState = Mprime(cubeState)
            newcenterorder = copy.deepcopy(centerorder)
            newcenterorder[0] = centerorder[5]
            newcenterorder[1] = centerorder[1]
            newcenterorder[2] = centerorder[4]
            newcenterorder[3] = centerorder[3]
            newcenterorder[4] = centerorder[0]
            newcenterorder[5] = centerorder[2]
            centerorder = copy.deepcopy(newcenterorder)
        if i == "M2":
            cubeState = M2(cubeState)
            newcenterorder = copy.deepcopy(centerorder)
            newcenterorder[0] = centerorder[5]
            newcenterorder[1] = centerorder[1]
            newcenterorder[2] = centerorder[4]
            newcenterorder[3] = centerorder[3]
            newcenterorder[4] = centerorder[0]
            newcenterorder[5] = centerorder[2]
            centerorder = copy.deepcopy(newcenterorder)
            newcenterorder = copy.deepcopy(centerorder)
            newcenterorder[0] = centerorder[5]
            newcenterorder[1] = centerorder[1]
            newcenterorder[2] = centerorder[4]
            newcenterorder[3] = centerorder[3]
            newcenterorder[4] = centerorder[0]
            newcenterorder[5] = centerorder[2]
            centerorder = copy.deepcopy(newcenterorder)
        if i == "E":
            cubeState = E(cubeState)
            newcenterorder = copy.deepcopy(centerorder)
            newcenterorder[0] = centerorder[3]
            newcenterorder[1] = centerorder[0]
            newcenterorder[2] = centerorder[1]
            newcenterorder[3] = centerorder[2]
            newcenterorder[4] = centerorder[4]
            newcenterorder[5] = centerorder[5]
            centerorder = copy.deepcopy(newcenterorder)
        if i == "E'":
            cubeState = Eprime(cubeState)
            newcenterorder = copy.deepcopy(centerorder)
            newcenterorder[0] = centerorder[1]
            newcenterorder[1] = centerorder[2]
            newcenterorder[2] = centerorder[3]
            newcenterorder[3] = centerorder[0]
            newcenterorder[4] = centerorder[4]
            newcenterorder[5] = centerorder[5]
            centerorder = copy.deepcopy(newcenterorder)
        if i == "E2":
            cubeState = E2(cubeState)
            newcenterorder = copy.deepcopy(centerorder)
            newcenterorder[0] = centerorder[3]
            newcenterorder[1] = centerorder[0]
            newcenterorder[2] = centerorder[1]
            newcenterorder[3] = centerorder[2]
            newcenterorder[4] = centerorder[4]
            newcenterorder[5] = centerorder[5]
            centerorder = copy.deepcopy(newcenterorder)
            newcenterorder = copy.deepcopy(centerorder)
            newcenterorder[0] = centerorder[3]
            newcenterorder[1] = centerorder[0]
            newcenterorder[2] = centerorder[1]
            newcenterorder[3] = centerorder[2]
            newcenterorder[4] = centerorder[4]
            newcenterorder[5] = centerorder[5]
            centerorder = copy.deepcopy(newcenterorder)
        if i == "S":
            cubeState = S(cubeState)
            newcenterorder = copy.deepcopy(centerorder)
            newcenterorder[0] = centerorder[0]
            newcenterorder[1] = centerorder[4]
            newcenterorder[2] = centerorder[2]
            newcenterorder[3] = centerorder[5]
            newcenterorder[4] = centerorder[3]
            newcenterorder[5] = centerorder[1]
            centerorder = copy.deepcopy(newcenterorder)
        if i == "S'":
            cubeState = Sprime(cubeState)
            newcenterorder = copy.deepcopy(centerorder)
            newcenterorder[0] = centerorder[0]
            newcenterorder[1] = centerorder[5]
            newcenterorder[2] = centerorder[2]
            newcenterorder[3] = centerorder[4]
            newcenterorder[4] = centerorder[1]
            newcenterorder[5] = centerorder[3]
            centerorder = copy.deepcopy(newcenterorder)
        if i == "S2":
            cubeState = S2(cubeState)
            newcenterorder = copy.deepcopy(centerorder)
            newcenterorder[0] = centerorder[0]
            newcenterorder[1] = centerorder[4]
            newcenterorder[2] = centerorder[2]
            newcenterorder[3] = centerorder[5]
            newcenterorder[4] = centerorder[3]
            newcenterorder[5] = centerorder[1]
            centerorder = copy.deepcopy(newcenterorder)
            newcenterorder = copy.deepcopy(centerorder)
            newcenterorder[0] = centerorder[0]
            newcenterorder[1] = centerorder[4]
            newcenterorder[2] = centerorder[2]
            newcenterorder[3] = centerorder[5]
            newcenterorder[4] = centerorder[3]
            newcenterorder[5] = centerorder[1]
            centerorder = copy.deepcopy(newcenterorder)



    canvas.create_rectangle(110, 50, 130, 70, fill = centerorder[4])
    canvas.create_rectangle(50, 110, 70, 130, fill = centerorder[3])
    canvas.create_rectangle(110, 110, 130, 130, fill = centerorder[0])
    canvas.create_rectangle(170, 110, 190, 130, fill = centerorder[1])
    canvas.create_rectangle(230, 110, 250, 130, fill = centerorder[2])
    canvas.create_rectangle(110, 170, 130, 190, fill = centerorder[5])


    canvas.create_rectangle(90, 30, 110, 50, fill = arraycolors[cubeState[4][0]])
    canvas.create_rectangle(110, 30, 130, 50, fill = arraycolors[cubeState[4][1]])
    canvas.create_rectangle(130, 30, 150, 50, fill = arraycolors[cubeState[4][2]])
    canvas.create_rectangle(130, 50, 150, 70, fill = arraycolors[cubeState[4][3]])
    canvas.create_rectangle(130, 70, 150, 90, fill = arraycolors[cubeState[4][4]])
    canvas.create_rectangle(110, 70, 130, 90, fill = arraycolors[cubeState[4][5]])
    canvas.create_rectangle(90, 70, 110, 90, fill = arraycolors[cubeState[4][6]])
    canvas.create_rectangle(90, 50, 110, 70, fill = arraycolors[cubeState[4][7]])

    canvas.create_rectangle(90, 90, 110, 110, fill = arraycolors[cubeState[0][0]])
    canvas.create_rectangle(110, 90, 130, 110, fill = arraycolors[cubeState[0][1]])
    canvas.create_rectangle(130, 90, 150, 110, fill = arraycolors[cubeState[0][2]])
    canvas.create_rectangle(130, 110, 150, 130, fill = arraycolors[cubeState[0][3]])
    canvas.create_rectangle(130, 130, 150, 150, fill = arraycolors[cubeState[0][4]])
    canvas.create_rectangle(110, 130, 130, 150, fill = arraycolors[cubeState[0][5]])
    canvas.create_rectangle(90, 130, 110, 150, fill = arraycolors[cubeState[0][6]])
    canvas.create_rectangle(90, 110, 110, 130, fill = arraycolors[cubeState[0][7]])

    canvas.create_rectangle(150, 90, 170, 110, fill = arraycolors[cubeState[1][0]])
    canvas.create_rectangle(170, 90, 190, 110, fill = arraycolors[cubeState[1][1]])
    canvas.create_rectangle(190, 90, 210, 110, fill = arraycolors[cubeState[1][2]])
    canvas.create_rectangle(190, 110, 210, 130, fill = arraycolors[cubeState[1][3]])
    canvas.create_rectangle(190, 130, 210, 150, fill = arraycolors[cubeState[1][4]])
    canvas.create_rectangle(170, 130, 190, 150, fill = arraycolors[cubeState[1][5]])
    canvas.create_rectangle(150, 130, 170, 150, fill = arraycolors[cubeState[1][6]])
    canvas.create_rectangle(150, 110, 170, 130, fill = arraycolors[cubeState[1][7]])

    canvas.create_rectangle(210, 90, 230, 110, fill = arraycolors[cubeState[2][0]])
    canvas.create_rectangle(230, 90, 250, 110, fill = arraycolors[cubeState[2][1]])
    canvas.create_rectangle(250, 90, 270, 110, fill = arraycolors[cubeState[2][2]])
    canvas.create_rectangle(250, 110, 270, 130, fill = arraycolors[cubeState[2][3]])
    canvas.create_rectangle(250, 130, 270, 150, fill = arraycolors[cubeState[2][4]])
    canvas.create_rectangle(230, 130, 250, 150, fill = arraycolors[cubeState[2][5]])
    canvas.create_rectangle(210, 130, 230, 150, fill = arraycolors[cubeState[2][6]])
    canvas.create_rectangle(210, 110, 230, 130, fill = arraycolors[cubeState[2][7]])

    canvas.create_rectangle(30, 90, 50, 110, fill = arraycolors[cubeState[3][0]])
    canvas.create_rectangle(50, 90, 70, 110, fill = arraycolors[cubeState[3][1]])
    canvas.create_rectangle(70, 90, 90, 110, fill = arraycolors[cubeState[3][2]])
    canvas.create_rectangle(70, 110, 90, 130, fill = arraycolors[cubeState[3][3]])
    canvas.create_rectangle(70, 130, 90, 150, fill = arraycolors[cubeState[3][4]])
    canvas.create_rectangle(50, 130, 70, 150, fill = arraycolors[cubeState[3][5]])
    canvas.create_rectangle(30, 130, 50, 150, fill = arraycolors[cubeState[3][6]])
    canvas.create_rectangle(30, 110, 50, 130, fill = arraycolors[cubeState[3][7]])

    canvas.create_rectangle(90, 150, 110, 170, fill = arraycolors[cubeState[5][0]])
    canvas.create_rectangle(110, 150, 130, 170, fill = arraycolors[cubeState[5][1]])
    canvas.create_rectangle(130, 150, 150, 170, fill = arraycolors[cubeState[5][2]])
    canvas.create_rectangle(130, 170, 150, 190, fill = arraycolors[cubeState[5][3]])
    canvas.create_rectangle(130, 190, 150, 210, fill = arraycolors[cubeState[5][4]])
    canvas.create_rectangle(110, 190, 130, 210, fill = arraycolors[cubeState[5][5]])
    canvas.create_rectangle(90, 190, 110, 210, fill = arraycolors[cubeState[5][6]])
    canvas.create_rectangle(90, 170, 110, 190, fill = arraycolors[cubeState[5][7]])

    print(cubeState)
mainloop()
