import turtle
import time
import random

phil = turtle.Turtle()

def moveRight():
    global direction
    direction = 'right'

def moveLeft():
    global direction
    direction = 'left'

def moveDown():
    global direction
    direction = 'down'

def moveUp():
    global direction
    direction = 'up'

turtle.listen()
turtle.onkeypress(moveUp, 'Up')
turtle.onkeypress(moveDown, 'Down')
turtle.onkeypress(moveRight, 'Right')
turtle.onkeypress(moveLeft, 'Left')

def spawnFood():
    screen = turtle.Screen()
    ww = (screen.window_width() // 2) // 20 
    wh = (screen.window_height() // 2) // 20 
    food_x = random.randrange(-ww, ww) * 20 
    food_y = random.randrange(-ww, ww) * 20 
    food = turtle.Turtle('triangle')
    food.color('yellow')
    food.penup()
    food.goto(food_x, food_y)

# def thirdthing():
philbody = [turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle()] #create 4 turtles
turtlecolors = ['black', 'red', 'blue', 'green']

for i in range(len(philbody)): #will get the length of the list and return 4 to count 0,1,2,3
    philbody[i].speed('fastest')
    philbody[i].penup()
    philbody[i].shape('circle') #for each part of philbody make each new one the circle
    philbody[i].color(turtlecolors[i]) #for each one in philbody, phil and etc etc
    philbody[i].setx(i * (20)) #move the x coordinates to 1*-20, 2*-20, etc

direction = ''
spawnFood()

def move(direction):
    coords = 0,0
    if direction == 'left':
        coords = philbody[0].xcor() - 20, philbody[0].ycor()
    elif direction == 'right':
        coords = philbody[0].xcor() + 20, philbody[0].ycor()
    elif direction == 'up':
        coords = philbody[0].xcor(), philbody[0].ycor() + 20
    elif direction == 'down':
        coords = philbody[0].xcor(), philbody[0].ycor() - 20

    philtail = philbody.pop() #pop the end off and store it to the variable philtail
    philbody.insert(0,philtail) #insert philtail to position 0 of philbody
    philtail.goto(*coords) #reset the end to the beginning of the bodys position * 20 in x value ...the *coords recognizes the comma above and uses them as two seperate values to pass throgh coords
    
while True:
    move(direction)

    #dictionary
    snake_body = {snake_body[0]:philbody[0], 
            snake_body[1]:philbody[1], 
            snake_body[2]:philbody[2], 
            snake_body[3]:philbody[3]}

    turtle.exitonclick()


