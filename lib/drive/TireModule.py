from machine import Pin
from time import sleep

class Tire:
    
    def __init__(self, _pin):
        self.pin = _pin;
        self.__pinController = Pin(self.pin, Pin.OUT)
    
    def getPin(self):
        return self.pin
        
    def move(self):
        self.__pinController.value(1)
        
    def stop(self, wait=False, time = 5):
        self.__pinController.value(0)
        
        if ( wait ):
            sleep(time)
        
    def isMoving(self):
        print( self.__pinController.value())
        return self.__pinController.value() == 1
        