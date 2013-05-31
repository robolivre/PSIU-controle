from BasicCommands import BasicCommands
from GenerationProtocol import GenerationProtocol

class BasicPSIU:
    var = "var"
    command = ""
    basicCommands = BasicCommands()
    generationProtocol = GenerationProtocol()
    
    def makeCommand(self, command):
        self.setCommand(command)
        self.switch(self.getCommand())
    
    

    
    def switch(self, command):
        #case paraFrente
        if(command == "paraFrente"):
            self.generationProtocol.commandOrder(self.basicCommands.forward())
        #case paraTras
        elif(command == "paraTras"):
            self.generationProtocol.commandOrder(self.basicCommands().backwards())
        #case giraEsquerda
        elif(command == "giraEsquerda"):
            self.generationProtocol.commandOrder(self.basicCommands().turnsLeft())
        #case giraDireita
        elif(command == "giraDireita"):
            self.generationProtocol.commandOrder(self.basicCommands().turnRight())
        else:
            print("Erro, basic command unrecognized.")
                
    
    def setCommand(self, command):
        self.command = command
        
    def getCommand(self):
        return self.command
    
    
    def imprime(self):
        print(self.basico.forward())
