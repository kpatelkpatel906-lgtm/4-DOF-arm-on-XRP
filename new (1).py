# Import necessary modules
from machine import Pin, ADC
import bluetooth
import time
import math

from XRPLib.defaults import *
from pestolink import PestoLinkAgent


robot_name = "4DOF"

# Create an instance of the PestoLinkAgent class
pestolink = PestoLinkAgent(robot_name)

# Initialize toggle before the loop to prevent NameError
toggle = 0

# Start an infinite loop
while True:
    if pestolink.is_connected():  # Check if a BLE connection is established
        board.set_rgb_led(2, 247, 2)
        rotation = -1 * pestolink.get_axis(0)
        throttle = -1 * pestolink.get_axis(1)

        # Corrected button check chain
        if pestolink.get_button(2):
            toggle = 0
        elif pestolink.get_button(3):
            toggle = 1

        # Mode 0 Logic
        if toggle == 0:
            drivetrain.arcade(throttle, rotation)

            if pestolink.get_button(0):
                servo_four.set_angle(90)
                servo_three.set_angle(90)
                servo_two.set_angle(0)
                servo_one.set_angle(90)
                board.set_rgb_led(2, 2, 247)

            if pestolink.get_button(1):
                servo_four.set_angle(90)
                servo_three.set_angle(180)
                servo_one.set_angle(180)
                board.set_rgb_led(251, 255, 2)

            if pestolink.get_button(6):
                servo_two.set_angle(0)
                board.set_rgb_led(5, 255, 255)

            if pestolink.get_button(7):
                servo_two.set_angle(120)
                board.set_rgb_led(255, 5, 255)

        # Mode 1 Logic
        elif toggle == 1:
            if pestolink.get_button(6):
                servo_two.set_angle(0)
                board.set_rgb_led(5, 255, 255)

            if pestolink.get_button(7):
                servo_two.set_angle(120)
                board.set_rgb_led(255, 5, 255)

            servo_four.set_angle((-1 * pestolink.get_axis(0)) + 90)
            servo_three.set_angle((-1 * pestolink.get_axis(2)) + 90)
            servo_two.set_angle((-1 * pestolink.get_axis(3)) + 90)

        batteryVoltage = (ADC(Pin("BOARD_VIN_MEASURE")).read_u16()) / (
            1024 * 64 / 14
        )
        pestolink.telemetryPrintBatteryVoltage(batteryVoltage)

    else:
        drivetrain.arcade(0, 0)
        board.set_rgb_led(247, 2, 2)
        board.led_on()