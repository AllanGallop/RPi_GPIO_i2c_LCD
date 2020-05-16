import smbus
from time import *

class i2c:
    def __init__(self, addr, port=1):
        self.addr = addr
        self.bus = smbus.SMBus(port) 

    # Write a single command
    def write_cmd(self, cmd):
        self.bus.write_byte(self.addr, cmd)
        sleep(0.0001)

    # Write a command and argument
    def write_cmd_arg(self, cmd, data):
        self.bus.write_byte_data(self.addr, cmd, data)
        sleep(0.0001)

    # Write a block of data
    def write_block_data(self, cmd, data):
        self.bus.write_block_data(self.addr, cmd, data)
        sleep(0.0001)


class lcd:
    def __init__(self,address):
        self.lcd = i2c(address)
        ##Backlight Status
        self.bl = 0x08
        self.write(0x03)
        self.write(0x02)
        self.write(0x20 | 0x08 | 0x00 | 0x00)
        self.write(0x08 | 0x04)
        self.write(0x01)
        self.write(0x04 | 0x02)
        sleep(0.2)

    def strobe(self, data):
        self.lcd.write_cmd(data | 0b00000100 | self.bl)
        sleep(.0005)
        self.lcd.write_cmd(((data & ~0b00000100) | self.bl))
        sleep(.0001)

    def write_four_bits(self, data):
        self.lcd.write_cmd(data | self.bl)
        self.strobe(data)

    def write(self, cmd, mode=0):
        self.write_four_bits(mode | (cmd & 0xF0))
        self.write_four_bits(mode | ((cmd << 4) & 0xF0))

    def backlight(self, state):
        if state.lower() == "on":
            self.bl=0x08
        elif state.lower() == "off":
            self.bl=0x00

    def display_string(self, string, line):
        line_cmd = [0x00,0x80,0xC0,0x94,0xD4]
        self.write(line_cmd[line])
        for char in string:
            self.write(ord(char), 0b00000001)

    def clear(self):
        self.write(0x03)
        self.write(0x02)
        self.write(0x20 | 0x08 | 0x00 | 0x00)
        self.write(0x08 | 0x04)
        self.write(0x01)
        self.write(0x04 | 0x02)

