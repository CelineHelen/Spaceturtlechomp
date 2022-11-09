# Turtle Graphics Game - Space Turtle Chomp
import turtle
import math
import random
import winsound
import time
# Set up screen
turtle.setup(650,650)
wn = turtle.Screen()
wn.bgcolor('black')
wn.bgpic('kbgame-bg.gif')
wn.tracer(3)
# Draw border
mypen=turtle.Turtle()
mypen.penup()
mypen.setposition(-300,-300)
mypen.pendown()
mypen.pensize(3)
mypen.color('white')
mypen.speed(0)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()
# Create player turtle
player = turtle.Turtle()
player.color('salmon')
player.shape('turtle')
player.penup()
player.speed(0)
# Create opponent turtle
comp = turtle.Turtle()
comp.color('blue')
comp.shape('turtle')
comp.penup()
comp.setposition(random.randint(-290, 290), random.randint(-290, 290))
# Create competition score
mypen2=turtle.Turtle()
mypen2.color('red')
mypen2.hideturtle()
# Create variable score 
score=0
comp_score=0
# Create food
maxFoods=10
foods=[]
for count in range(maxFoods):
    new_food = turtle.Turtle()
    new_food.shapesize(.5)
    new_food.color("light green")
    new_food.shape("circle")
    new_food.penup()
    new_food.speed(0)
    new_food.setposition(random.randint(-290,290), random.randint(-290,290))
    foods.append(new_food)
# Set speed variable
speed=1
# Set game time limit for 1 minute (60 seconds)
timeout=time.time() + (10*6)
# Define functions
def isCollision(t1, t2):
    d = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2) + math.pow(t1.ycor()-t2.ycor(), 2))
    if d<20:
        return True
    else:
        return False
def turn_left():
    player.left(30)
def turn_right():
    player.right(30)
def increase_speed():
    global speed
    speed += 1
def RecordCollision(food, pen, score, iscomp):
    food.setposition(random.randint(-290,290), random.randint(-290,290))
    food.right(random.randint(0, 360))
    winsound.PlaySound('chomp.wav', winsound.SND_ASYNC)
    #record scores
    scorestring ="Score: %s " % score
    #draw scores
    pen.undo()
    pen.penup()
    pen.hideturtle()
    xpos=200 if iscomp else -290
    pen.setposition(xpos, 310)
    pen.write(scorestring, False, align='left', font=('Arial', 14, 'normal'))


# Set keyboard binding
turtle.listen()
turtle.onkey(turn_left, 'Left')
turtle.onkey(turn_right, 'Right')
turtle.onkey(increase_speed, 'Up')
while True:
    gametime=0
    if gametime==6 or time.time() > timeout:
        break
    gametime = gametime - 1
    player.forward(speed)
    comp.forward(12)

    #Boundary Player Checking x coordinate
    if player.xcor() > 290 or player.xcor() <-290:
        player.right(180)
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
    #Boundary Player Checking y coordinate
    if player.ycor() > 290 or player.ycor() <-290:
        player.right(180)
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
    # Boundary Comp Checking x coordinate
    if comp.xcor() > 290 or comp.xcor() < -290:
        #comp.right(random.randint(30, 155))
        comp.right(180)
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    # Boundary Comp Checking y coordinate
    if comp.ycor() > 290 or comp.ycor() < -290:
        #comp.right(random.randint(30, 155))
        comp.right(180)
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    # Move food around
    for food in foods:
        food.forward(1)
    
     # Boundary Food Checking x coordinate
        if food.xcor() > 290 or food.xcor() < -290:
            food.right(180)
            winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    # Boundary Food Checking y coordinate
        if food.ycor() > 290 or food.ycor() < -290:
            food.right(180)
            winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
        if isCollision(player, food):
            score+=1
            RecordCollision(food, mypen, score, False)
        if isCollision(comp, food):
            comp_score+=1
            RecordCollision(food, mypen2, comp_score, True)

if (int(score) > int(comp_score)):
    mypen.setposition(0, 0)
    mypen.color("yellow")
    mypen.write("Game Over: You WIN", False, align="center", font=("Arial", 28, "normal"))
else:
    mypen.setposition(0, 0)
    mypen.color("yellow")
    mypen.write("Game Over: You LOSE", False, align="center", font=("Arial", 28, "normal"))
delay = input("Press Enter to finish")



    



