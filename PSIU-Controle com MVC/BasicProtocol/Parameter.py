class Parameter:
    numberOfParameters = 1
    parameters = []
    
    def setNumberOfParameters(self, num):
        self.numberOfParameters = num
    
    def setParameter(self, parameters):
        self.parameters.append(parameters)
    
    def getParameter(self):
        return self.parameters