import turtle
# import random
import time

# Screen setup
screen = turtle.Screen()
screen.setup(width=600, height=500)
screen.bgcolor("lightskyblue")
screen.tracer(0)  # Turn off screen updates to reduce drag

# PHYSICAL CONSTRAINTS
STARTING_LOCATION = (-150, -200)
GRAVITY = -1
X_SPEED = 5 # default speed in the x direction which doesn't change
DEFAULT_SQUARE_SIDE = 20
BOUNDARY = 30 # how far does the ball have to be from the hoop to be considered in?

# Basketball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("orange")
ball.penup()
ball.goto(STARTING_LOCATION)
ball.speed(0)

# Hoop
hoop = turtle.Turtle()
hoop.shape("square")
hoop.color("red")
hoop.shapesize(stretch_wid=3, stretch_len=1)
hoop.penup()
hoop.goto(200, -150)
hoop.speed(0)

# Floor
floor = turtle.Turtle()
floor.hideturtle()
floor.penup()
floor.goto(-300, -220)
floor.pendown()
floor.pensize(3)
floor.color("gray")
floor.forward(600)

# Score
score = 0
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("black")
score_display.penup()
score_display.hideturtle()
score_display.goto(-280, 190)

# Power bar
power_bar = turtle.Turtle()
power_bar.shape("square")
power_bar.color("gray")
power_bar.shapesize(stretch_wid=10, stretch_len=1)
power_bar.penup()
power_bar.goto(-250, 0)
power_bar.speed(0)

green_bar = turtle.Turtle()
green_bar.shape("square")
green_bar.color("green")
green_bar.shapesize(stretch_wid=1, stretch_len=1)
green_bar.penup()
green_bar.goto(-250, 0)
green_bar.speed(0)

# get the distance of the ball from the hoop
def get_distance():
    return int(abs(ball.xcor() - hoop.xcor()))

# the optimal speed that would ensure the ball will go in
def get_optimal_speed():
    global green_bar

    # Here we use the projectile motion formula to find
    #   the optimal speed range
    d = get_distance()
    gravity = abs(GRAVITY)
    x_speed = X_SPEED
    res = (d * gravity) / (2 * x_speed)

    return res

# speed and inverse speed formulas define the speed in the y direction
def speed_formula(line_location):
    return 20 + line_location ** (1/2)
def inverse_speed_formula(speed):
    # if speed is under 20, line location cannot exist, 
    # so we return -25 to signal that it's impossible to make the shot from there
    if speed < 20:
        return -25
    return (speed - 20) ** 2

# updates the location of the green bar which signals the optimal speed
def update_green_bar():
    global green_bar

    optimal_speed = get_optimal_speed()

    desired_location = -power_bar.shapesize()[0] * DEFAULT_SQUARE_SIDE / 2
    desired_location += inverse_speed_formula(optimal_speed)

    print(optimal_speed, desired_location)

    green_bar.goto(green_bar.xcor(), desired_location)

    return True

update_green_bar()

# this is a moving line on the power_bar object
# the user chooses his shooting speed using this moving line
line = turtle.Turtle()
line.shape("square")
line.color('blue')
line.shapesize(stretch_wid=0.25, stretch_len=1)
line.penup()
line.goto(-250, 0)
line.speed(10)

# get the line's location on the power_bar object 
# the possible locations are from 0 to the height of power bar
def get_line_location():
    center = power_bar.ycor()
    half_height = power_bar.shapesize()[0] * DEFAULT_SQUARE_SIDE / 2

    return int(line.ycor()- (center - half_height))    

speed = get_line_location()
line_moving_direction = "up"

def move_line():
    global line_moving_direction

    # move the line
    if line_moving_direction == "up":
        line.goto(line.xcor(), line.ycor()+1)
    else:
        line.goto(line.xcor(), line.ycor()-1)

    # sleep to slow down the movement of the line
    time.sleep(0.001)

    # change direction by comparing the current line location against 
    # max and min locations
    if get_line_location() <= 0:
        line_moving_direction = "up"

    highest_speed = power_bar.shapesize()[0] * DEFAULT_SQUARE_SIDE
    if get_line_location() >= highest_speed:
        line_moving_direction = "down"

high_score = 0
winner = ""

# Lives
DEFAULT_LIVES = 5
lives = DEFAULT_LIVES

# updates the score board after the user shoots
def update_board():
    score_display.clear()
    score_display.write(f"Score: {score}; Lives: {lives}\nHighscore: {high_score}; Name: {winner}", align="left", font=("Arial", 16, "normal"))

update_board()

# Function to move the ball up (shooting)
def shoot():
    global score, lives, high_score, winner

    if ball.ycor() < -190:  # Only allow shooting from the starting position
        # user's y speed is chosen using the line object
        y_speed = speed_formula(get_line_location())

        # local gravity variable
        gravity = GRAVITY

        # made is True if the user makes the shot, otherwise False
        made = False

        # while the ball is in the air, move it up
        while ball.ycor() >= -200:
            ball.goto(ball.xcor() + X_SPEED, ball.ycor() + y_speed)
            y_speed += gravity
            screen.update()
            time.sleep(0.02)
            
            boundary = BOUNDARY
            # Check for collision with the hoop
            if (abs(ball.xcor() - hoop.xcor()) < boundary and
                    abs(ball.ycor() - hoop.ycor()) < boundary):
                made = True
                # give the user a three or two pointer depending on his distance
                score += 1
                
                # TODO: score increase should be proportional to the initial distance to the hoop (3 pointers, 2 pointers...)
                update_board()
                ball.goto(STARTING_LOCATION) # Reset ball position

        ball.goto(STARTING_LOCATION) # Reset ball position even if miss
        update_green_bar()

        if not made:
            lives -= 1
            update_board()
            
        if lives <= 0:
            turtle.TK.messagebox.showinfo(title="The Turtle says:", message=f"Your score is {score}.")
            
            if score > high_score:
                name = turtle.TK.simpledialog.askstring("Congrats!", "You're the highest scorer. Enter your name:")
                high_score = score
                winner = name

            score = 0
            lives = DEFAULT_LIVES
            update_board()

def move_left():
    ball.goto(ball.xcor() - 5, ball.ycor())
    update_green_bar()

def move_right():
    ball.goto(ball.xcor() + 5, ball.ycor())
    update_green_bar()

# Keyboard binding
screen.listen()
screen.onkeypress(shoot, "space")
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# Main game loop
while True:
    screen.update()
    move_line()

# TODO: improved graphics; include stickman, basket, 3 point line... 