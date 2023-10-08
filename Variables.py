

class Variable:
    
    sport = 'None'
    gameMode = 'None'
    website = 'None'

    def setWebsite(self, n):
        self.website = n
        
    def setSport(self, n):
        self.sport = n
        
    def setGameMode(self, n):
        self.gameMode = n
        
    def getWebsite(self):
        return self.website
      
    def getGameMode(self):
        return self.gameMode
    
    def getSport(self):
        return self.sport
      
      