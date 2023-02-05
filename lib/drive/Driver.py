from lib.drive.TireModule import Tire
from lib.drive.DriverConstants import DriverConstants
from lib.drive.PathPlanner import PathPlanner

from time import sleep, sleep_ms

class Driver:
    
    __instance = None
    
    @staticmethod
    def getInstance():
        if ( Driver.__instance == None ): Driver.__instance = Driver()
            
        return Driver.__instance;
    
    def __init__(self):
        
        if ( Driver.__instance != None ): raise Exception("Driver instance already created")
        
        self.__leftFrontTire = Tire(DriverConstants.leftFrontMotorPin)
        self.__leftBackTire = Tire(DriverConstants.leftBackMotorPin)
        
        self.__rightFrontTire = Tire(DriverConstants.rightFrontMotorPin)
        self.__rightBackTire = Tire(DriverConstants.rightBackMotorPin)
        
        self.pathPlanner = PathPlanner.getInstance()
        
    def move(self, x, z):
        self.pathPlanner.move(x, z)
        
        while not self.pathPlanner.doneRunning():
            currentMove = self.pathPlanner.getPopulatedTable()[
                self.pathPlanner.timeElapsed()
            ]
            if ( currentMove['leftF'] ):
                self.__leftFrontTire.move()
            else:
                self.__leftFrontTire.stop()
            
            if ( currentMove['leftB'] ):
                self.__leftBackTire.move()
            else:
                self.__leftBackTire.stop()
            
            if ( currentMove['rightF'] ):
                self.__rightFrontTire.move()
            else:
                self.__rightFrontTire.stop()
            
            if ( currentMove['rightB'] ):
                self.__rightBackTire.move()
            else:
                self.__rightBackTire.stop()
                
            sleep_ms(1) # Path planner is based on milliseconds so we will need the path to run for at least one milliseconds
            
            self.pathPlanner.nextMove()
            
            
        
    def forward(self):
        self.__leftFrontTire.move()
        
        self.__leftBackTire.move()
        
        self.__rightFrontTire.move()
        
        self.__rightBackTire.move()
        
    def stopAll(self):
        self.__leftFrontTire.stop()
        
        self.__leftBackTire.stop()
        
        self.__rightFrontTire.stop()
        
        self.__rightBackTire.stop()
        
    def left(self):
       self.__rightFrontTire.stop()
       self.__rightBackTire.stop()
       
       self.__leftFrontTire.move()
       self.__leftBackTire.move()
       
    def right(self):
       self.__leftFrontTire.stop()
       self.__leftBackTire.stop()
       
       self.__rightFrontTire.move()
       self.__rightBackTire.move()