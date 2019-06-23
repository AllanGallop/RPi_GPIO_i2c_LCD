from RPi_GPIO_i2c_LCD import lcd
from time import sleep, strftime

def MyFunction(self):
    ## Show current time on line 3
    self.lcd.display_string(str(strftime("%d/%m %H:%M:%S").center(20,' ')),2)

lcdDisplay = lcd.HD44780(0x27,MyFunction)
lcdDisplay.set("The time is:",1)
sleep(6)