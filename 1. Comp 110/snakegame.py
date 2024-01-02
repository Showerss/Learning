import time
import random
import turtle

###########################################################
################## Classes and prep work ##################
class GameCharacters(turtle.Turtle):
    def __init__(self, x,y, shape="square", color="white", speed=0):
        super().__init__()
        self.speed(0)
        self.shape(shape)
        self.color(color)
        self.penup()
        self.goto(x,y)

#snake food subclass, start it off at the same XY value every start of the game
class Food(GameCharacters):
    def __init__(self):
        super().__init__(0, 100, "circle", "orange")

#game over turtle subclass, hiding it by default cause its only meant to write game over
class GameOver(GameCharacters):
    def __init__(self):
        super().__init__(0,0, "square", "red")
        self.hideturtle()

#title screen turtle subclass, hiding it by default cause its only meant to write the title
class Title(GameCharacters):
    def __init__(self):
        super().__init__(0,0, "square", "white")
        self.hideturtle()

class SnakeBody(GameCharacters):
    def __init__(self):
        super().__init__(0,0, "square", "grey")
        self.direction = None
        
    ### movements
    def go_up(self):
        print("up")
        self.direction = "up"

    def go_down(self):
        print("down")
        self.direction = "down"

    def go_left(self):
        print("left")
        self.direction = "left"

    def go_right(self):
        print("right")
        self.direction = "right"
        
    def move(self):
        print("Current direction:", self.direction)

        if self.direction == "up":
            y = self.ycor()
            self.sety(y + 20)

        if self.direction == "down":
            y = self.ycor()
            self.sety(y - 20)

        if self.direction == "left":
            x = self.xcor()
            self.setx(x - 20)

        if self.direction == "right":
            x = self.xcor()
            self.setx(x + 20)

class Score(GameCharacters):
    def __init__(self):
        super().__init__(0,0, "square", "white")
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write("Score: {}".format(score), align="top", font=("Courier", 12, "normal"))

#initialize classes
food = Food()
game_over_turtle = GameOver()
title = Title()
score = Score()
head = SnakeBody()

#initialize additional variables alongside my class initialization
score = 0 
segments = []
delay = 0

###########################################################
############### GAME STARTS HERE  #########################
    
#make our window that we'll be using for the game
win = turtle.Screen()
win.listen()

win.title("Snake? SNAKE? SNAAAAAAAAAKE!")
win.bgcolor("black")
win.setup(width=600, height=600)

# or use WASD if needed
win.onkeypress(head.go_up, "w")
win.onkeypress(head.go_down, "s")
win.onkeypress(head.go_left, "a")
win.onkeypress(head.go_right, "d")

## write the title screen options
title.goto(0,0)
title.write("Snake? SNAKE? SNAAAAAAAAAKE!", align="center", font=("Courier", 32, "normal"))

title.goto(0,-50)
title.write("1. Slow", align="center", font=("Courier", 24, "normal"))

title.goto(0,-100)
title.write("2. Normal", align="center", font=("Courier", 24, "normal"))

title.goto(0,-150)
title.write("3. Lightning", align="center", font=("Courier", 24, "normal"))

## difficulty selection
difficulty = win.textinput("Difficulty", "Select difficulty: ")
if difficulty == "1":
    title.clear()
    delay = 0.5

elif difficulty == "2":
    title.clear()
    delay = 0.1

elif difficulty == "3":
    title.clear()
    delay = 0.01




##################################################
############## MAIN GAME LOOP ####################
while True:
    win.update()
    head.move()

    #check for collision with border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290: 
        game_over_turtle.write("Game Over", align="center", font=("Courier", 38, "normal"))
        time.sleep(1)
        win.clear()

        #hide the segments if the border it hit
        for segment in segments:
            segment.goto(1000,1000)
        segments.clear()

        #reset the score
        score = 0
    
    #check for collision with food
    if head.distance(food) < 30:
        #move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)
        #increase the score within the if food distance check
        score += 20
        score.update_score()

        #add a segment to the snake, make them different than the head so we can track it though
        segments.append(head) 

    #move the end segments first in reverse order
    for index in range(len(segments)-1 ,0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x,y)
        # basically whats going on here is that we are moving the segments to the position of the segment in front of it, 
        # so the last segment will move to the position of the second to last segment, the second to last segment 
        # will move to the position of the third to last segment, etc.

    for segment in segments:
        if head.distance(segment) < 20:
            game_over_turtle.write("Game Over", align="center", font=("Courier", 38, "normal"))
            time.sleep(1)
            win.clear()

    #move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y) # this is the first segment, so it will move to the position of the head
        # it needs to be seperate because the head is not a segment, so it needs to be moved seperately

    time.sleep(delay)
