
class QueueModel:
    def __init__(self, lambdaVal, mu, units):
        self.lambdaVal = lambdaVal
        self.mu = mu
        self.units = units
        self.rho = None
        self.ls = None
        self.ws = None
        self.lq = None


    def getLambda(self):
        return self.lambdaVal
    
    def getMu(self):
        return self.mu
    
    def getUnits(self):
        return self.units
    

    def getRho(self):
        if self.rho is None:
            if self.mu <= 0:
                return "Mu must be greater than 0"
            self.rho = self.lambdaVal / self.mu
        return self.rho
    
    def getLs(self):
        if self.mu <= self.lambdaVal:
            return "Mu must be greater than Lambda"
        self.ls = self.lambdaVal / (self.mu - self.lambdaVal)
        return self.ls
    
    def getWs(self):
        if self.mu <= self.lambdaVal:
            return "Mu must be greater than Lambda"
        self.ws = 1 / (self.mu - self.lambdaVal)
        return self.ws
    
    def getLq(self):
        self.getRho()
        self.getLs()
        self.lq = self.rho * self.ls
        return self.lq
    

    def getPCero(self):
        self.getRho()
        return 1 - self.rho
    
