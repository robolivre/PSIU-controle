#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
from time import sleep
import serial
import glob

from BasicProtocol.GenerationProtocol import GenerationProtocol
from BasicProtocol.PCName import PCName
from BasicProtocol.RobotName import RobotName
from BasicProtocol.BasicPSIU import BasicPSIU
from BasicProtocol.Parameter import Parameter

def scan():
    return glob.glob('/dev/ttyU*') +  glob.glob('/dev/ttyA*')

class PSIUControle:
    robotName = RobotName()
    basicPSIU = BasicPSIU()
    parameter = Parameter()
    robots = ["robo1", "robo2", "robo3", "robo4", "robo5"]
    port = []
    numberOfCommands = ''
    #robots = []
        
    def searchRobot(self):
        search = GenerationProtocol()
        message = search.whatsYourName()
        for i in range(len(scan())):
            #robotPort = serial.Serial('/dev/tty.usbserial', 9600)
            robotPort = serial.Serial(scan()[i])
            #robotPort = serial.Serial("/dev/ttyACM1", 9600)
            robotPort.close()
            robotPort.open()
            if (robotPort.portstr.find("/dev/ttyACM") != -1):
                sleep(1.5)
            print("menssagem: " + message)
            answer = self.sendMessage(robotPort, message)
            print("resposta: " + answer)
            self.robotName.setRobotName(answer.split(" ")[3])
#            robos = []
#            robos = {"robo0", "robo1", "robo2", "robo3", "robo4"}
#            self.robotName.setRobotName(robos)
            robots = self.robotName.getRobotName(0)
            print(robots[0])
            
            print("nome: " + self.robotName.getRobotName(i))
            self.robots.append(self.robotName.getRobotName(i))
            self.port.append(self.robotName.portstr)
            
            robotPort.close()
    
    def setMainRobot(self, n):
        self.robotName.setRobotName(self.robots[n])
            
    def showBots(self):
        for i in range (len(self.robots)):
            print("Robot: " + self.robots[i])
            
    def selectRobot(self, index):
        print self.robots[index] 

    def sendMessage(self, robotPort, message):
            robotPort.write(str(message))
            sleep(0.2)
            answer = ''
            while (robotPort.inWaiting() > 0):
                answer = answer + robotPort.read() 
                
            return answer
    
    def whatsYourName(self):
        pcName = PCName()
        gerarProtocolo = GenerationProtocol()
        message = "?? 000 qualseunome " + pcName.getPCName() + " "
        message = gerarProtocolo.protocolSize(message)
        message = gerarProtocolo.calculatesChecksum(message)
        return message
        
    def howManyCommands(self):
        pcName = PCName()
        robotName = RobotName()
        gerarProtocolo = GenerationProtocol()
        message = robotName.getRobotName() + " " +"000" + " " +  "quantoscomandos" + " " + pcName.getPCName() + " "
        message = gerarProtocolo.protocolSize(message)
        message = gerarProtocolo.calculatesChecksum(message)
        return message
    
    def showCommand(self, numberOfCommand):
        pcName = PCName()
        robotName = RobotName()
        gerarProtocolo = GenerationProtocol()
        message = robotName.getRobotName() + " " +"000" + " " + "exibecomando" + " " + numberOfCommand + " " + pcName.getPCName() + " "
        message = gerarProtocolo.protocolSize(message)
        message = gerarProtocolo.calculatesChecksum(message)
        return message
        