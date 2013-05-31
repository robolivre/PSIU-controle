from RobotName import RobotName
from Parameter import Parameter
from PCName import PCName

class GenerationProtocol:
    pcName = PCName()
    robotName = RobotName()
    parameter = Parameter()
    
    
    def commandOrder(self, command):
        protocol = self.robotName.getRobotName() + ' ' + "000" + ' ' + command + ' ' + str(self.parameter.getParameter()) + ' ' + self.pcName.getPCName() + ' '
        protocol = protocol.replace('[', '')
        protocol = protocol.replace(']', '')
        protocol = self.calculatesChecksum(protocol)
        protocol = self.protocolSize(protocol)
        print (protocol)
        
        #MNERIM 034 parafrente 100 PC 02123
    
    def protocolSize(self, message):
        sizeMessage = len(message)
        sizeSize = str(sizeMessage)
        if (len(sizeSize) < 3):
            sizeSize = '0' + sizeSize
        message = message.replace("000", sizeSize)
        return message
    
    
    def calculatesChecksum(self, message):
        checksum = 0
        for i in range(len(message)):
                checksum = checksum + ord(str(message[i]))       
        
        checksumStr = str(checksum)    
        
        if len(str(checksum)) < 5:
            for i in range(5 - len(str(checksum))):
                checksumStr = '0' + checksumStr
        
        message = message + str(checksum)
        
        return message