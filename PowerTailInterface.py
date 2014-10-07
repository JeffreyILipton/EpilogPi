import time
import RPi.GPIO as io

class PowerTailInterface:
    def __init__(self):
        self.power_pin = 23
        io.setmode(io.BCM)
        io.setup(self.power_pin,io.OUT)
        io.output(self.power_pin,True) ## set the powertail on by default
        self.on = True
        
    def __del__(self):
        self.ser.close()

    def isready(self):
        return self.on

    def setPower(self,power):
        self.on = power
        io.output(self.power_pin, power) 
    

if __name__ == '__main__':
    ir = PowerTailInterface()
    print ir.isready()
    loopVar=True
    while(loopVar):
        val = raw_input('Command:')
        b = (val == "O")
        ir.write(b)
        if (val == 'Q'):
            loopVar = False