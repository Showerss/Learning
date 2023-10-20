import turtle
import time
import random

phil = turtle.Turtle()

# def project():
#     phil.forward(20)
#     phil.left(90)
#     phil.forward(20)
#     phil.right(90)
#     phil.forward(20)

#     turtle.exitonclick()

# project()


# def newthing():
#     phil.shape('circle')

#     phil.setx(phil.xcor() + 20)
#     time.sleep(0.5)

#     phil.sety(phil.ycor() + 20)
#     time.sleep(0.5)

#     phil.setx(phil.xcor() + 20)
#     time.sleep(0.5)

#     phil.sety(phil.ycor() + 20)

#     turtle.exitonclick()

# newthing()

def spawnFood():
    screen = turtle.Screen()
    ww = (screen.window_width() // 2) // 20 
    wh = (screen.window_height() // 2) // 20 
    food_x = random.randrange(-ww, ww) *20 
    food_y = random.randrange(-ww, ww) *20 
    food = turtle.Turtle('triangle')
    food.color('yellow')
    food.penup()
    food.goto(food_x, food_y)

def thirdthing():
    philbody = [turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle()] #create 4 turtles
    turtlecolors = ['black', 'red', 'blue', 'green']

    for i in range(len(philbody)): #will get the length of the list and return 4 to count 0,1,2,3
        philbody[i].speed('slowest')
        philbody[i].penup()
        philbody[i].shape('circle') #for each part of philbody make each new one the circle
        philbody[i].color(turtlecolors[i]) #for each one in philbody, phil and etc etc
        philbody[i].setx(i * (20)) #move the x coordinates to 1*-20, 2*-20, etc

    def moveRight():
        move('right')

    def moveLeft():
        move('left')

    def moveDown():
        move('down')

    def moveup():
        move('up')

    spawnFood()

    def move(direction):
        coords = 0,0
        if direction == 'left':
            coords = philbody[0].xcor() - 20, philbody[0].ycor()
        elif direction == 'right':
            coords = philbody[0].xcor() + 20, philbody[0].ycor()
        elif direction == 'up':
            coords = philbody[0].xcor(), philbody[0].ycor() +20
        elif direction == 'down':
            coords = philbody[0].xcor(), philbody[0].ycor() -20

        philtail = philbody.pop() #pop the end off and store it to the variable philtail
        philbody.insert(0,philtail) #insert philtail to position 0 of philbody
        philtail.goto(*coords) #reset the end to the beginning of the bodys position * 20 in x value
        # the *coords recognizes the comma above and uses them as two seperate values to pass throgh coords
        
    move('right')
    move('down')
    move('right')
    move('up')
    move('up')
    move('left')




    turtle.exitonclick()
thirdthing()



''' 
in order: 

before game starts: (globals)
spawn food

while in game:
    move
    if snake head collides into food
        spawn more food

    ========

how do we check for colisions? 
what does that look like in code

    ========

module... import random

'''


