import turtle
import random
import backgroundMod
import time
turtle.title("Snakes & Ladders")
turtle.setup(550 * 1.25,550 * 1.25,0,0)
turtle.bgcolor("#000000")
bgp1 = turtle.Screen()
bgp1.bgpic("bgpic1.gif")

boxLocation = [
    (-200, -200),  # 1
    (-100, -200),  # 2
    (0, -200),  # 3
    (100, -200),  # 4
    (200, -200),  # 5
    (200, -100),  # 6
    (100, -100),  # 7
    (0, -100),  # 8
    (-100, -100),  # 9
    (-200, -100),  # 10
    (-200, 0),  # 11
    (-100, 0),  # 12
    (0, 0),  # 13
    (100, 0),  # 14
    (200, 0),  # 15
    (200, 100),  # 16
    (100, 100),  # 17
    (0, 100),  # 18
    (-100, 100),  # 19
    (-200, 100),  # 20
    (-200, 200),  # 21
    (-100, 200),  # 22
    (0, 200),  # 23
    (100, 200),  # 24
    (200, 200)  # 25
]


def roll():
    # Rolls dice
    rolledNum = random.randint(1, 6)
    rolledNumImage = ("Dice" + str(rolledNum) + ".gif")
    diceIcon = turtle.Turtle()
    diceIcon.penup()
    diceIcon.setpos(-295, 0)
    turtle.addshape(rolledNumImage)
    diceIcon.shape(rolledNumImage)
    return rolledNum


def player_mover(player, num):
    # Moves the player icon to the coord given
    if num == 0:
        location = num
    elif num > 0 and num < 24:
        location = num-1
    else:
        location = 24
    print("You move to", num)
    player.penup()
    player.goto(boxLocation[location])


def turtleWin(score, winner):
    # displays win image
    winnerIMG = turtle.Turtle()
    winnerIMG.penup()
    winnerIMG.setpos(0, 0)
    if winner == "p1":
        score[0] += 1
        turtle.addshape("win1.gif")
        winnerIMG.shape("win1.gif")
    elif winner == "p2":
        score[1] += 1
        turtle.addshape("win2.gif")
        winnerIMG.shape("win2.gif")
    time.sleep(3)
    turtle.clearscreen()
    return score


def enterInput():
    # accepts input from user
    enter = input("\nPress Enter to carry on : ")
    if enter == "":
        return "Y"
    else:
        print("You have failed to make the correct inputs, progam will now end")
        print("Next time, hit the Enter key to make a correct input")
        print("bye")
        exit()


def snakeAndLadderGame():
    # Game function
    player = [1, 1]
    i = 0

    # setup player 1 turtle
    turtle.addshape("bull.gif")
    p1Turtle = turtle.Turtle()
    p1Turtle.shape("bull.gif")
    player_mover(p1Turtle, 0)

    # setup player 2 turtle
    turtle.addshape("cow.gif")
    p2Turtle = turtle.Turtle()
    p2Turtle.shape("cow.gif")
    player_mover(p2Turtle, 0)

    nextInput = enterInput()
    while (nextInput == 'Y'):
        title = ("PLAYER " + str(i+1) + " TURN")
        turtle.title(title)
        print("---------------------\n", title)

        diceRoll = roll()
        print("You rolled ", diceRoll)
        player[i] += diceRoll
        player_mover(p1Turtle if i == 0 else p2Turtle, player[i])

        # Ladder
        if(player[i] == 5 or player[i] == 9 or player[i] == 18):
            print("\nLUCKY!!")
            print("You landed on a ladder!!")
            print("You go up!!")
            if player[i] == 5:
                player[i] = 6
            if player[i] == 9:
                player[i] = 12
            if player[i] == 18:
                player[i] = 23
            player_mover(p1Turtle if i == 0 else p2Turtle, player[i])

        # Snakes
        if(player[i] == 8 or player[i] == 20 or player[i] == 24):
            print("\nUNLUCKY!!")
            print("You landed on a Snake!!")
            print("SSS SSS SSS SORRY!!")
            print("You go down!!")
            print("You're down bad :(")
            if player[i] == 8:
                player[i] = 3
            if player[i] == 20:
                player[i] = 1
            if player[i] == 24:
                player[i] = 14
            player_mover(p1Turtle if i == 0 else p2Turtle, player[i])

        # Win Statements
        if(player[0] > 24):
            print("\nCONGRATULATIONS!!!!!!!!")
            print("Player 1...")
            print("YOU WON!!!!!!!!!!!!!!!!")
            print("So, sorry player 2, maybe next time ;)")
            return("p1")
        if(player[1] > 24):
            print("\nCONGRATULATIONS!!!!!!!!")
            print("Player 2...")
            print("YOU WON!!!!!!!!!!!!!!!!")
            print("So, sorry player 1, maybe next time ;)")
            return("p2")

        i = (i+1) % 2
        nextInput = enterInput()


scores = [0, 0]
# gamesPlayed = 0
while True:
    backgroundMod.CreateBg()
    # gamesPlayed += 1
    print("New Game Start")
    print("Game Count : ", (scores[0] + scores[1]))
    # foo = snakeAndLadderGame()
    scores = turtleWin(scores, snakeAndLadderGame())
    print("---------------------End Game---------------------")
    print("PLAYER 1 WIN COUNT : ", scores[0])
    print("PLAYER 2 WIN COUNT : ", scores[1])
    print("Play Again?")
    playAgain = enterInput()
    if playAgain != "Y":
        break
exit()
