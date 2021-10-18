import turtle
import tkinter

turtle.title("Snakes & Ladders")
turtle.setup(550 * 1.25,550 * 1.25,0,0)
turtle.bgcolor("#000000")
bgp1 = turtle.Screen()
bgp1.bgpic("bgpic1.gif")

# This code is for drawing the 5 by 5 grid

# Below, i will define the main square for the grid
boxLabelLocation = [
    (-195 * 1.25, -140 * 1.2),
    (-115 * 1.25, -140 * 1.2),
    (-35 * 1.25, -140 * 1.2),
    (45 * 1.25, -140 * 1.25),
    (125 * 1.25, -140 * 1.25),
    (125 * 1.25, -60 * 1.25),
    (45 * 1.25, -60 * 1.25),
    (-35 * 1.25, -60 * 1.2),
    (-115 * 1.25, -60 * 1.2),
    (-195 * 1.25, -60 * 1.2),
    (-195 * 1.25, 20 * 1.2),
    (-115 * 1.25, 20 * 1.2),
    (-35 * 1.25, 20 * 1.2),
    (45 * 1.25, 20 * 1.25),
    (125 * 1.25, 20 * 1.25),
    (125 * 1.25, 100 * 1.25),
    (45 * 1.25, 100 * 1.25),
    (-35 * 1.25, 100 * 1.2),
    (-115 * 1.25, 100 * 1.2),
    (-195 * 1.25, 100 * 1.2),
    (-195 * 1.25, 180 * 1.2),
    (-115 * 1.25, 180 * 1.2),
    (-35 * 1.25, 180 * 1.2),
    (45 * 1.25, 180 * 1.25),
    (125 * 1.25, 180 * 1.25)]


def createSquare():
    turtle.hideturtle()
    MainBg = turtle.Turtle()
    MainBg.hideturtle()
    MainBg.pencolor("blue")
    MainBg.width(3)
    MainBg.speed(10)
    MainBg.penup()
    MainBg.goto(-200 * 1.25, -200 * 1.25)
    MainBg.pendown()
    for i in range(4):
        MainBg.forward(400 * 1.25)
        MainBg.left(90)


# Below, I will define 8 individual data blocks to draw each line of the grid
def BlockMake(coord, leftVal=0):
    turtle.hideturtle()
    box = turtle.Turtle()
    box.hideturtle()
    box.pencolor("blue")
    box.width(3)
    box.speed(10)
    box.pu()
    box.goto(coord)
    box.pd()
    box.lt(leftVal)
    box.forward(400 * 1.25)


def BlockPrint():
    BlockMake((-200 * 1.25, -120 * 1.25))
    BlockMake((-200 * 1.25, -40 * 1.25))
    BlockMake((-200 * 1.25, 40 * 1.25))
    BlockMake((-200 * 1.25, 120 * 1.25))

    BlockMake((-120 * 1.25, -200 * 1.25), 90)
    BlockMake((-40 * 1.25, -200 * 1.25), 90)
    BlockMake((40 * 1.25, -200 * 1.25), 90)
    BlockMake((120 * 1.25, -200 * 1.25), 90)


# this bit of code is used for labelling the squares
def numberMake(coord, num):
    turtle.speed(10)
    turtle.penup()
    turtle.setpos(coord)
    turtle.color("red")
    turtle.pendown()
    turtle.write(num, font=("Arial", 12, "bold italic"))


def LabelPrint():
    cnt = 0
    for box in boxLabelLocation:
        cnt += 1
        numberMake(box, cnt)



# this bit of code adds the ladders
def LadderMake(coord, ladderName):
    ladder = turtle.Turtle()
    ladder.penup()
    ladder.setpos(coord)
    turtle.addshape(ladderName)
    ladder.shape(ladderName)


def LadderPrint():
    l1 = LadderMake((-100, -50), "laddermodded1.gif")
    l2 = LadderMake((0, 150), "laddermodded2.gif")
    l3 = LadderMake((200, -100), "laddermodded3.gif")
    turtle.showturtle()


# this bit of code adds the snakes
def SnakeMake(coord, snakeName):
    snake = turtle.Turtle()
    snake.penup()
    snake.setpos(coord)
    turtle.addshape(snakeName)
    snake.shape(snakeName)


def SnakePrint():
    l1 = SnakeMake((100, 100), "snake.gif")
    l2 = SnakeMake((0, -150), "snake2.gif")
    l3 = SnakeMake((-200, -50), "snake3.gif")
    turtle.showturtle()


# this function resets and creates the background
def CreateBg():
    turtle.resetscreen()
    # This code is for setting up the dimensions of the turtle window
    turtle.setup(550 * 1.25, 550 * 1.25, 0, 0)
    # This code is for setting up the background 
    turtle.title("Snakes & Ladders")
    turtle.setup(550 * 1.25,550 * 1.25,0,0)
    turtle.bgcolor("#000000")
    bgp1 = turtle.Screen()
    bgp1.bgpic("bgpic1.gif")
    # This code is for hiding the turtle pens
    turtle.hideturtle()
    createSquare()
    BlockPrint()
    LabelPrint()
    LadderPrint()
    # turtle.hideturtle()
    SnakePrint()
    turtle.hideturtle()
