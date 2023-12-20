import time
import random
import turtle

## To do list ##
# 1. import snake head
# 2. import MGS music 
# 5. import snake food pictures
# 6. make some type of recursion for the snake body
# 8. make a score counter




###########################################################
################## PREP WORK ##############################
class GameCharacters(turtle.Turtle):
    def __init__(self, x,y, shape="square", color="white"):
        self.speed(0)
        self.shape(shape)
        self.color(color)
        self.penup()
        self.goto(x,y)

#create my main snake but as a subclass since they're all going to be very similar 
class Snake(GameCharacters):
    def __init__(self):
        super().__init__(0,0, "square", "teal")
        self.direction = "stop"

    ### movements
    def go_up(self):
        self.direction = "up"
    def go_down(self):
        self.direction = "down"
    def go_left(self):
        self.direction = "left"
    def go_right(self):
        self.direction = "right"
    def move(self):
        if self.direction == 'up':
            y = self.ycor()
            self.sety(y + 20)
        if self.direction == 'down':
            y = self.ycor()
            self.sety(y - 20)
        if self.direction == 'left':
            x = self.xcor()
            self.setx(x - 20)
        if self.direction == 'right':
            x = self.xcor()
            self.setx(x + 20)

#snake food subclass
class Food(GameCharacters):
    def __init__(self):
        super().__init__(0, 100, "circle", "orange")
        self.speed(0)
    
    def show(self):
        self.showturtle()

#game over turtle subclass
class GameOver(GameCharacters):
    def __init__(self):
        super().__init__(0,0, "square", "red")

#initialize classes
food = Food()
game_over_turtle = GameOver()
head = Snake()

#initialize additional variables alongside my class initialization
score = 0 
segments = []
delay = 0









###########################################################
############### GAME STARTS HERE  #########################

#title screen creation 
win = turtle.Screen()
win.title("Snake? SNAKE? SNAAAAAAAAAKE!")
win.bgcolor("black")
win.setup(width=600, height=600)

title_turtle = turtle.Turtle()
title_turtle.speed(0)
title_turtle.color("white")
title_turtle.penup()
title_turtle.hideturtle()

title_turtle.goto(0,0)
title_turtle.write("Snake? SNAKE? SNAAAAAAAAAKE!", align="center", font=("Courier", 38, "normal"))

title_turtle.goto(0,-50)
title_turtle.write("1. Slow", align="center", font=("Courier", 24, "normal"))

title_turtle.goto(0,-100)
title_turtle.write("2. Normal", align="center", font=("Courier", 24, "normal"))

title_turtle.goto(0,-150)
title_turtle.write("3. Lightning", align="center", font=("Courier", 24, "normal"))



## difficulty selection
difficulty = win.textinput("Difficulty", "Select difficulty: ")
if difficulty == "1":
    title_turtle.clear()
    delay = 0.5

elif difficulty == "2":
    title_turtle.clear()
    delay = 0.1

elif difficulty == "3":
    title_turtle.clear()
    delay = 0.01







##################################################
############## MAIN GAME LOOP ####################
while True:
    win.update()

    #check for collision with border
    if Snake.xcor() > 290 or Snake.xcor() < -290 or Snake.ycor() > 290 or Snake.ycor() < -290: 
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
    if head.distance(Snake.food) < 30:
        #move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        #increase the score within the if food distance check
        score += 20

        #add a segment to the snake, make them different than the head so we can track it though
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment) 

    #move the end segments first in reverse order
    for index in range(len(segments)-1 ,0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x,y)
        # basically whats going on here is that we are moving the segments to the position of the segment in front of it, 
        # so the last segment will move to the position of the second to last segment, the second to last segment 
        # will move to the position of the third to last segment, etc.

    for segment in segments:
        if Snake.head.distance(segment) < 20:
            game_over_turtle.write("Game Over", align="center", font=("Courier", 38, "normal"))
            time.sleep(1)
            win.clear()

    #move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y) # this is the first segment, so it will move to the position of the head
        # it needs to be seperate because the head is not a segment, so it needs to be moved seperately

    Snake.move()
    time.sleep(delay)