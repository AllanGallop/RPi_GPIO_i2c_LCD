## RPi_GPIO_i2c_LCD
> HD44780 / PCF8574 LCD Module


### Sections
* Description
* Features
* Install
* Usage


### Description
>A simple module for working with the HD44780 LCD over I²C using the PCF8574 Backpack

### Features
* Non-Blocking update loop
* Supports 2x16 and 4x20 Displays
* Easy to use
* Callback loop for updating display directly


### Install
#### Using PyPi: 
```
pip3 install RPi-GPIO-I2C-LCD
```

### Usage
##### Simple

```
from RPi_GPIO_i2c_LCD import lcd
from time import sleep

## Address of backpack
i2c_address = 0x27

## Initalize display
lcdDisplay = lcd.HD44780(i2c_address)

## Set string value to buffer
lcdDisplay.set("Hello",1)
lcdDisplay.set("World",2)

sleep(1)
```

#### Callback Loop
```
from RPi_GPIO_i2c_LCD import lcd
from time import sleep, strftime

## Callback function that will run on every display loop
def MyFunction(self):
    ## Show current time on line 2
    self.lcd.display_string(str(strftime("%d/%m %H:%M:%S").center(20,' ')),2)

## Initalize display with callback
lcdDisplay = lcd.HD44780(0x27,MyFunction)

## Set string value to buffer
lcdDisplay.set("The time is:",1)
sleep(6)
```
