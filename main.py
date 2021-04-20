def test_1():
    global FOOT_LOW, FOOT_HIGH
    foot = LEFT_BACK_FOOT
    FOOT_LOW = 20
    FOOT_HIGH = 150
    Servo.servo(foot, FOOT_HIGH)
    basic.pause(1000)
    Servo.servo(foot, FOOT_LOW)
def stand_up():
    Servo.servo(LEFT_BACK_FOOT, 0)
    Servo.servo(RIGHT_BACK_FOOT, 0)
    Servo.servo(LEFT_FRONT_FOOT, 0)
    Servo.servo(RIGHT_FRONT_FOOT, 0)
def default_position():
    # Set the robot to the default position
    Servo.servo(LEFT_FRONT_FOOT, 90)
    Servo.servo(LEFT_FRONT_LEG, 90)
    Servo.servo(LEFT_BACK_FOOT, 90)
    Servo.servo(LEFT_BACK_LEG, 90)
    Servo.servo(RIGHT_FRONT_FOOT, 90)
    Servo.servo(RIGHT_FRONT_LEG, 90)
    Servo.servo(RIGHT_BACK_FOOT, 90)
    Servo.servo(RIGHT_BACK_LEG, 90)
    basic.show_icon(IconNames.SMALL_DIAMOND)
LEFT_FRONT_FOOT = 0
FOOT_HIGH = 0
FOOT_LOW = 0
RIGHT_BACK_LEG = 0
RIGHT_BACK_FOOT = 0
RIGHT_FRONT_LEG = 0
RIGHT_FRONT_FOOT = 0
LEFT_BACK_LEG = 0
LEFT_FRONT_LEG = 0
LEFT_BACK_FOOT = 0
LEFT_BACK_FOOT = 0
LEFT_FRONT_LEG = 1
LEFT_BACK_FOOT = 3
LEFT_BACK_LEG = 2
RIGHT_FRONT_FOOT = 4
RIGHT_FRONT_LEG = 5
RIGHT_BACK_FOOT = 6
RIGHT_BACK_LEG = 7
soundExpression.hello.play()

def on_forever():
    if input.button_is_pressed(Button.A):
        test_1()
        basic.pause(1000)
    if input.logo_is_pressed():
        default_position()
    if input.button_is_pressed(Button.B):
        stand_up()
    default_position()
basic.forever(on_forever)
