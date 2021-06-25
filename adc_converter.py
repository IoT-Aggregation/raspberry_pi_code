#External imports
import time
import busio
import board
import digitalio
from enum import Enum
import RPi.GPIO as GPIO
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
from config import INPUT_PINS_LIST


# ADC CONVERTER SET UP:

# 1. RaspberryPi pins
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.D5)
mcp_converter = MCP.MCP3008(spi, cs)

# 2. Input pins
pin_0 = AnalogIn(mcp_converter, MCP.P0)
pin_1 = AnalogIn(mcp_converter, MCP.P1)
pin_2 = AnalogIn(mcp_converter, MCP.P2)
pin_3 = AnalogIn(mcp_converter, MCP.P3)
pin_4 = AnalogIn(mcp_converter, MCP.P4)
pin_5 = AnalogIn(mcp_converter, MCP.P5)
pin_6 = AnalogIn(mcp_converter, MCP.P6)
pin_7 = AnalogIn(mcp_converter, MCP.P7)


def get_pin_value(channel_no):
    return globals()[f'channel_{channel_no}'].value

def get_all_pins_values():
    return dict(f'\"pin_{pin_number}\": \"{get_pin_value(pin_number)}\"'
                for pin_number in INPUT_PINS_LIST)
