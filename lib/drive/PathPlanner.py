class PathPlanner:
    
    metersPerSecond = 10
    anglePerSecond = 10
    
    __instance = None
    
    @staticmethod
    def getInstance():
        if ( PathPlanner.__instance == None ): PathPlanner.__instance = PathPlanner()
        
        return PathPlanner.__instance
    
    def __init__(self):
        
        if ( PathPlanner.__instance != None ): raise Exception("Pathplanner instance already exists")
        
        self.__populatedTable = []
        self.__milliSecondsElapsed = 0
        
    def getPopulatedTable(self):
        return self.__populatedTable
    
    def timeElapsed(self):
        return self.__milliSecondsElapsed 
    
    def nextMove(self):
        return self.__populatedTable[++self.__milliSecondsElapsed]
        
    def populateTable(self, x, z):
        populatedTable = []
        
        timeToZ = abs(
            z / PathPlanner.anglePerSecond if z != 0 else 0
        )
        
        for milliSeconds in range( ( timeToZ * 1000 ) + 2 ):
            if milliSeconds == ( ( timeToZ * 1000 ) + 1 ): # Turn motors off when on last index incase all we are doing is turning
                populatedTable.append({
                    'leftF': False,
                    'rightF': False,
                    'leftB': False,
                    'rightB': False
                })
            
            elif z == 0: 
                populatedTable.append({
                    'leftF': False,
                    'rightF': False,
                    'leftB': False,
                    'rightB': False
                })
                
            elif z > 0:
                populatedTable.append({
                    'leftF': False,
                    'rightF': True,
                    'leftB': True,
                    'rightB': False
                })
                
            elif z < 0:
                populatedTable.append({
                    'leftF': True,
                    'rightF': False,
                    'leftB': False,
                    'rightB': True
                })  
        
        
        timeToX = abs(
            x / PathPlanner.metersPerSecond if x != 0 else 0
        )
        
        for milliSeconds in range( ( timeToX * 1000 ) + 2 ):
            if milliSeconds == ( ( timeToX * 1000 ) + 1 ): # Turn motors off when on last index incase all we are doing is moving
                populatedTable.append({
                    'leftF': False,
                    'rightF': False,
                    'leftB': False,
                    'rightB': False
                })
            
            elif x == 0: 
                populatedTable.append({
                    'leftF': False,
                    'rightF': False,
                    'leftB': False,
                    'rightB': False
                })
                
            elif x > 0:
                populatedTable.append({
                    'leftF': True,
                    'rightF': True,
                    'leftB': True,
                    'rightB': True
                })
                
        self.__populatedTable = populatedTable
        
    def setDoneRunning(self):
        self.timeElapsed = self.__populatedTable.count()
        
    def doneRunning(self):
        return self.timeElapsed >= self.__populatedTable.count()
    
    def move(self, x, z ):
        self.resetTime()
        self.populateTable(x, z)
    
    def turn(self, z ):
        self.resetTime()
        self.populateTable(0, z)
    
    def resetTime(self):
        self.__milliSecondsElapsed = 0
    
