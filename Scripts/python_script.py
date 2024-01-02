# Python Code for Controlling Motors and Servo using micro:bit

# Author: Efstratios Paliodimos
# Date: January 2, 2024
# Editor/IDE: Microsoft MakeCode
# Description: This code demonstrates motor and servo control 
# using a micro:bit for the "Robotic Arm" project from GigoToys.

def on_pin_released_p2():
    pins.servo_write_pin(AnalogPin.P1, 100)
    basic.show_leds("""
        . . # . .
        . . # . .
        . # . # .
        # . . . #
        # . . . #
        """)
input.on_pin_released(TouchPin.P2, on_pin_released_p2)

def move_motor_B():
    global flag_B
    if input.button_is_pressed(Button.A):
        flag_B = 1
        pins.digital_write_pin(DigitalPin.P13, 0)
        pins.analog_write_pin(AnalogPin.P14, 750)
        basic.pause(50)
    elif input.button_is_pressed(Button.B):
        flag_B = 2
        pins.digital_write_pin(DigitalPin.P13, 1)
        pins.analog_write_pin(AnalogPin.P14, 750)
        basic.pause(50)
    else:
        flag_B = 0
        pins.digital_write_pin(DigitalPin.P13, 0)
        pins.analog_write_pin(AnalogPin.P14, 0)
        basic.pause(50)
def reset_motor_B():
    pins.analog_write_pin(AnalogPin.P16, 0)
def reset_all():
    reset_servo()
    reset_motor_A()
def reset_servo():
    pins.servo_write_pin(AnalogPin.P1, 0)
    basic.show_icon(IconNames.SQUARE)
    basic.pause(100)
    basic.show_icon(IconNames.SMALL_SQUARE)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)

def on_pin_pressed_p2():
    pins.servo_write_pin(AnalogPin.P1, 0)
    basic.show_leds("""
        . . # . .
        . . # . .
        . # . # .
        . # . # .
        . . # . .
        """)
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def move_motor_A():
    global flag_A
    if pins.digital_read_pin(DigitalPin.P8) != 1:
        flag_A = 1
        pins.digital_write_pin(DigitalPin.P8, 1)
        basic.pause(50)
        pins.digital_write_pin(DigitalPin.P15, 0)
        pins.analog_write_pin(AnalogPin.P16, 635)
        basic.pause(200)
    else:
        flag_A = 0
        pins.digital_write_pin(DigitalPin.P8, 1)
        basic.pause(50)
        pins.analog_write_pin(AnalogPin.P16, 0)
    if pins.digital_read_pin(DigitalPin.P12) != 1:
        flag_A = 1
        pins.digital_write_pin(DigitalPin.P12, 1)
        basic.pause(50)
        pins.digital_write_pin(DigitalPin.P15, 1)
        pins.analog_write_pin(AnalogPin.P16, 635)
        basic.pause(200)
    else:
        flag_A = 0
        pins.digital_write_pin(DigitalPin.P12, 1)
        basic.pause(50)
        pins.analog_write_pin(AnalogPin.P16, 0)
def reset_motor_A():
    pins.analog_write_pin(AnalogPin.P16, 0)
flag_A = 0
flag_B = 0
reset_servo()

def on_forever():
    move_motor_A()
    move_motor_B()
basic.forever(on_forever)
