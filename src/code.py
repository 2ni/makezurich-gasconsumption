"""
based on
https://github.com/Seeed-Studio/Seeed_Arduino_GroveAI/blob/master/Seeed_Arduino_GroveAI.cpp
https://github.com/Seeed-Studio/Seeed_Arduino_GroveAI/blob/master/Seeed_Arduino_GroveAI.h
"""

import board
import time
import digitalio
import neopixel
import busio

pixel_pin = board.GP22
num_pixels = 6
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.01, auto_write=False)
from adafruit_bus_device.i2c_device import I2CDevice

print("**********************************\nSeed Stuio AI Vision Camera.\n**********************************\n")

CAM_ADDR = 0x62
comm_port = busio.I2C(board.GP3, board.GP2)
device = I2CDevice(comm_port, CAM_ADDR)

def printhex(name, result):
    print(name, "".join("0x{:02x} ".format(x) for x in result))

def read(cmds, length):
    with device as bus_device:
        bus_device.write(cmds)
        result = bytearray(length)
        bus_device.readinto(result)

    return result

def write(cmds):
    with device as bus_device:
        bus_device.write(cmds)

def waitforidle():
    print("waiting...")
    state = 0x01
    while state != 0x00:
        state = read(bytes([0x80, 0x03]), 1)[0]
        time.sleep(.5)
        # print("state 0x{:02x}".format(state))

    print("Done.")

result = read(bytes([0x80, 0x01]), 2)
printhex("firmware", result)
# set algo
write(bytes([0xA0, 0x01, 0x01])) # can only set 0=object detection,1=object counting,2=classification
result = read(bytes([0xA0, 0x00]), 1)
printhex("algo (0x03):", result)

# set model
write(bytes([0xA0, 0x11, 0x11])) # can only set 0, 0x11: person detection, 0x13: meter reading
result = read(bytes([0xA0, 0x10]), 1)
printhex("model (0x01):", result)

# set confidence
write(bytes([0xA0, 0x41, 0x31]))
result = read(bytes([0xA0, 0x40]), 1)
printhex("confidence:", result)

# save config + wait for idle
print("saving config")
write(bytes([0xA0, 0xEE]))
state = read(bytes([0x80, 0x03]), 1)

waitforidle()

# invoke
print("invoking")
write(bytes([0xA0, 0xA0]))
waitforidle()

# read result
time.sleep(.02)
result = read(bytes([0xA0, 0xA1]), 2)
num = result[0]<<8 | result[1]
print("number of results", num)

# object detection returns object_counting_t : [target, count]
for i in range(num):
    data = read(bytes([0xA0, 0xA2]), 2)
    print("target: 0x{:02x}, count: 0x{:02x}".format(data[0], data[1])) # returns always [0, 0]...

RED = (255, 0, 0)
GREEN = (0, 255, 0)
pixels[1] = RED
pixels.show()
is_red = True

while True:
    time.sleep(.5)
    pixels[1] = GREEN if is_red else RED
    is_red = not is_red
    pixels.show()
