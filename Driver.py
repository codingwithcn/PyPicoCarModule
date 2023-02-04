from TireModule import Tire
from DriverConstants import DriverConstants

class Driver:
    
    __instance = None
    
    @staticmethod
    def getInstance():
        if ( Driver.__instance == None ):
            Driver.__instance = Driver()
            
        return Driver.__instance;
    
    def __init__(self):
        
        if ( Driver.__instance != None ): raise Exception("Driver instance already created")
        
        self.leftFrontTire = Tire(DriverConstants.leftFrontMotorPin)
        self.leftBackTire = Tire(DriverConstants.leftBackMotorPin)
        
        self.rightFrontTire = Tire(DriverConstants.rightFrontMotorPin)
        self.rightBackTire = Tire(DriverConstants.rightBackMotorPin)
        
    def forward(self):
        self.leftFrontTire.move()
        
        self.leftBackTire.move()
        
        self.rightFrontTire.move()
        
        self.rightBackTire.move()
        
    def stopAll(self):
        self.leftFrontTire.stop()
        
        self.leftBackTire.stop()
        
        self.rightFrontTire.stop()
        
        self.rightBackTire.stop()
        
    def left(self):
       self.rightFrontTire.stop()
       self.rightBackTire.stop()
       
       self.leftFrontTire.move()
       self.leftBackTire.move()
       
    def right(self):
       self.leftFrontTire.stop()
       self.leftBackTire.stop()
       
       self.rightFrontTire.move()
       self.rightBackTire.move()