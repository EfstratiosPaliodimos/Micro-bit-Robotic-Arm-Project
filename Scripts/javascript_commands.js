input.onPinReleased(TouchPin.P2, function () {
    pins.servoWritePin(AnalogPin.P1, 100)
    basic.showLeds(`
        . . # . .
        . . # . .
        . # . # .
        # . . . #
        # . . . #
        `)
})
function move_motor_B () {
    if (input.buttonIsPressed(Button.A)) {
        flag_B = 1
        pins.digitalWritePin(DigitalPin.P13, 0)
        pins.analogWritePin(AnalogPin.P14, 750)
        basic.pause(50)
    } else if (input.buttonIsPressed(Button.B)) {
        flag_B = 2
        pins.digitalWritePin(DigitalPin.P13, 1)
        pins.analogWritePin(AnalogPin.P14, 750)
        basic.pause(50)
    } else {
        flag_B = 0
        pins.digitalWritePin(DigitalPin.P13, 0)
        pins.analogWritePin(AnalogPin.P14, 0)
        basic.pause(50)
    }
}
function reset_motor_B () {
    pins.analogWritePin(AnalogPin.P16, 0)
}
function reset_all () {
    reset_servo()
    reset_motor_A()
}
function reset_servo () {
    pins.servoWritePin(AnalogPin.P1, 0)
    basic.showIcon(IconNames.Square)
    basic.pause(100)
    basic.showIcon(IconNames.SmallSquare)
    basic.pause(100)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
}
input.onPinPressed(TouchPin.P2, function () {
    pins.servoWritePin(AnalogPin.P1, 0)
    basic.showLeds(`
        . . # . .
        . . # . .
        . # . # .
        . # . # .
        . . # . .
        `)
})
function move_motor_A () {
    if (pins.digitalReadPin(DigitalPin.P8) != 1) {
        flag_A = 1
        pins.digitalWritePin(DigitalPin.P8, 1)
        basic.pause(50)
        pins.digitalWritePin(DigitalPin.P15, 0)
        pins.analogWritePin(AnalogPin.P16, 635)
        basic.pause(200)
    } else {
        flag_A = 0
        pins.digitalWritePin(DigitalPin.P8, 1)
        basic.pause(50)
        pins.analogWritePin(AnalogPin.P16, 0)
    }
    if (pins.digitalReadPin(DigitalPin.P12) != 1) {
        flag_A = 1
        pins.digitalWritePin(DigitalPin.P12, 1)
        basic.pause(50)
        pins.digitalWritePin(DigitalPin.P15, 1)
        pins.analogWritePin(AnalogPin.P16, 635)
        basic.pause(200)
    } else {
        flag_A = 0
        pins.digitalWritePin(DigitalPin.P12, 1)
        basic.pause(50)
        pins.analogWritePin(AnalogPin.P16, 0)
    }
}
function reset_motor_A () {
    pins.analogWritePin(AnalogPin.P16, 0)
}
let flag_A = 0
let flag_B = 0
reset_servo()
basic.forever(function () {
    move_motor_A()
    move_motor_B()
})
