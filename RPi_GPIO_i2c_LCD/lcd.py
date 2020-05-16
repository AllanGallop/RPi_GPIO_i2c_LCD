import threading, time, sys
from . import i2c_HD44780


buffer = {"1":"","2":"","3":"","4":""}

class HD44780:

    def set(self,string,line):
        try:
            line = str(line)
            buffer[line] = string
            return True
        except KeyError:
            return False
        

    def get(self,line):
        try:
            return buffer[str(line)]
        except KeyError:
            return False

    def clear(self):
           for line in buffer:
               buffer[line] = str("                                       ")

    def backlight(self,state):
        self.lcd.backlight(state)

    def updateDisplay(self, stop_event):
        global buffer
        while not stop_event.is_set():
            for line,string in buffer.items():
                self.lcd.display_string(str(string),int(line))
            if self.loopback is not None:
                try:
                    self.loopback(self)
                except:
                    print(sys.exc_info()[0])


    def stop(self):
        self.stop_event.set()

    def __init__(self,i2c_address,loopback=None):
        self.loopback = loopback
        self.lcd = i2c_HD44780.lcd(i2c_address)
        self.stop_event = threading.Event()
        self.th = threading.Thread(target=self.updateDisplay, args=[self.stop_event])
        self.th.setDaemon(True)
        self.th.start()
