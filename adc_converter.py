#External imports
import time
import busio
import board
import digitalio
from enum import Enum
import RPi.GPIO as GPIO
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn


# ADC converter setup

# RaspberryPi pins
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.D5)
mcp_converter = MCP.MCP3008(spi, cs)

# Input channels
channel_0 = AnalogIn(mcp_converter, MCP.P0)
channel_1 = AnalogIn(mcp_converter, MCP.P1)
channel_2 = AnalogIn(mcp_converter, MCP.P2)
channel_3 = AnalogIn(mcp_converter, MCP.P3)
channel_4 = AnalogIn(mcp_converter, MCP.P4)
channel_5 = AnalogIn(mcp_converter, MCP.P5)
channel_6 = AnalogIn(mcp_converter, MCP.P6)
channel_7 = AnalogIn(mcp_converter, MCP.P7)


def get_channel_value(channel_no):
    return globals()[f'channel_{channel_no}'].value
    #return getattr(other, f'channel_{channel_no}')

# Main program thread
while True:
    print('Raw ADC Value: ', channel_0.value)
    print('ADC Voltage: ' + str(channel_0.voltage) + 'V')
    time.sleep(0.5)
  



# TODO:
# - listening thread to return a requested channel value
# - web api (?) to enable reading channels values
# - function to return a list of all channels values every X hours
