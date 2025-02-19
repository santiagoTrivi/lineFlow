
class QueueModel:
    def __init__(self, lambdaVal, mu, units):
        self.lambdaVal = lambdaVal
        self.mu = mu
        self.units = units
        self.rho = None
        self.po = None
        self.ls = None
        self.ws = None
        self.lq = None
        self.lambdaEff = None


    def getLambda(self):
        return self.lambdaVal
    
    def getMu(self):
        return self.mu
    
    def getUnits(self):
        return self.units
    
    def getRho(self):
        self.rho = self.lambdaVal / self.mu
        return self.rho
    
    def getPo(self):
        if self.rho is None:
            self.getRho()
        self.po = 1 - self.rho
        return self.po

    
    def getLs(self):
        self.ls = self.lambdaVal / (self.mu - self.lambdaVal)
        return self.ls
    def getLq(self):
        if self.ls is None:
            self.getLs()
        self.lq = self.ls - self.lambdaVal
        return self.lq
    
    def getWs(self):
        if self.ls is None:
            self.getLs()            
        self.ws = self.ls / self.lambdaVal
        return self.ws
    
    def getWq(self):
        if self.lq is None:
            self.getLq()
        self.wq = self.lq / self.lambdaVal
        return self.wq
    
    
    def getLambdaEff(self):
        if self.getPo is None:
            self.getPo()
        self.lambdaEff = self.lambdaVal * self.po
        return self.lambdaEff
    
