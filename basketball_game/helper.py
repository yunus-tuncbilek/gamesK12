'''THIS FILE WILL HELP YOU ADD A NEW FEATURE TO YOUR BASKETBALL GAME
    After following this document, there might be errors in your program.
    Please ask your teacher for help there are any errors.
'''

'''Add this code at the beginning of the file'''

# PHYSICAL CONSTRAINTS
STARTING_LOCATION = (-150, -200)
GRAVITY = -1
X_SPEED = 5 # default speed in the x direction which doesn't change
DEFAULT_SQUARE_SIDE = 20
BOUNDARY = 30 # how far does the ball have to be from the hoop to be considered in?

'''Add the rest of the code before the shoot function'''

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
        