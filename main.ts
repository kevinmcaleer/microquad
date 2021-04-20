function test_1 () {
    foot = LEFT_FRONT_FOOT
    FOOT_LOW = 20
    FOOT_HIGH = 150
    Servo.Servo(foot, FOOT_HIGH)
    basic.pause(1000)
    Servo.Servo(foot, FOOT_LOW)
}
function stand_up () {
    Servo.Servo(LEFT_BACK_FOOT, 0)
    Servo.Servo(RIGHT_BACK_FOOT, 0)
    Servo.Servo(LEFT_FRONT_FOOT, 0)
    Servo.Servo(RIGHT_FRONT_FOOT, 0)
}
function default_position () {
    // Set the robot to the default position
    Servo.Servo(LEFT_FRONT_FOOT, 90)
    Servo.Servo(LEFT_FRONT_LEG, 90)
    Servo.Servo(LEFT_BACK_FOOT, 90)
    Servo.Servo(LEFT_BACK_LEG, 90)
    Servo.Servo(RIGHT_FRONT_FOOT, 90)
    Servo.Servo(RIGHT_FRONT_LEG, 90)
    Servo.Servo(RIGHT_BACK_FOOT, 90)
    Servo.Servo(RIGHT_BACK_LEG, 90)
    basic.showIcon(IconNames.SmallDiamond)
}
let FOOT_HIGH = 0
let FOOT_LOW = 0
let LEFT_FRONT_FOOT = 0
let foot = 0
let RIGHT_BACK_LEG = 0
let RIGHT_BACK_FOOT = 0
let RIGHT_FRONT_LEG = 0
let RIGHT_FRONT_FOOT = 0
let LEFT_BACK_LEG = 0
let LEFT_FRONT_LEG = 0
let LEFT_BACK_FOOT = 0
LEFT_BACK_FOOT = 0
LEFT_FRONT_LEG = 1
LEFT_BACK_FOOT = 3
LEFT_BACK_LEG = 2
RIGHT_FRONT_FOOT = 4
RIGHT_FRONT_LEG = 5
RIGHT_BACK_FOOT = 6
RIGHT_BACK_LEG = 7
soundExpression.hello.play()
basic.forever(function () {
    if (input.buttonIsPressed(Button.A)) {
        test_1()
        basic.pause(1000)
    }
    if (input.logoIsPressed()) {
        default_position()
    }
    if (input.buttonIsPressed(Button.B)) {
        stand_up()
    }
    default_position()
})
