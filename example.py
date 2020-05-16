from RPi_GPIO_i2c_LCD import lcd
from time import sleep, strftime

def MyFunction(self):
    ## Show current time on line 3
    self.lcd.display_string(str(strftime("%d/%m %H:%M:%S").center(20,' ')),2)

## Initialise display with callback
lcdDisplay = lcd.HD44780(0x27,MyFunction)

## Write string to line 1
lcdDisplay.set("The time is:",1)

## Toggle backlight
while(True):
    lcdDisplay.backlight("off")
    sleep(1)
    lcdDisplay.backlight("on")
    sleep(1)
