from enum import Enum
from re import I


# class Position:
#     def __init__(self, pan, tilt,zoom):
#         self.pan = pan
#         self.tilt = tilt
#         self.zoom =  zoom

#     def log(self):
#         print(str(self.pan), str(self.tilt), str(self.zoom))

# # pos = Position(2,4,6)

# # pos.log()

# class Camera:
#     def __init__(self,serialNumber,position,cameraType):
#         self.serialNumber = serialNumber
#         self.position = position
#         self.cameraType = cameraType

#     def log(self):
#         print(self.serialNumber,  str(self.cameraType))
#         self.position.log()

#     class CameraType(Enum):
#         ptz = 0
#         eptz = 1
#         stationary = 2


# cam = Camera('123bec',Position(3,2,1),Camera.CameraType.stationary)
# cam.log()


# class SecurityDevice:
#     def __init__(self,active):
#         self.active = active

#     def reset(self):
#         self.active = True

# class Sensor(SecurityDevice):   #inheritance
#     def __init__(self,silent,distance):
#         self.silent = silent
#         self.distance = distance

# class Stack:
#     def __init__(self):
#         self._data = []

#     def push(self,item):
#         self._data.append(item)

#     def remove(self):
#         return self._data.pop()

#     def peek(self):
#         return self._data[len(self._data) - 1]


# mystack = Stack()

# mystack.push(3)
# mystack.push(5)
# mystack.push(42)
# print(mystack.peek())
# print(mystack.remove())
# mystack.remove()
# print(mystack.peek())

# class Car:
#     def __init__(self, model, color):
#         self.model = model
#         self.color = color

#     def printDetails(self):
#         print("Model:", self.model)
#         print("Color:", self.color)


# class SedanEngine:
#     def start(self):
#         print("Car has started.")

#     def stop(self):
#         print("Car has stopped.")


# class Sedan(Car):
#     def __init__(self, model, color):
#         super().__init__(model, color)
#         self.engine = SedanEngine()

#     def setStart(self):
#         self.engine.start()

#     def setStop(self):
#         self.engine.stop()


# car1 = Sedan("Toyota", "Grey")
# car1.setStart()
# car1.printDetails()
# car1.setStop()


# Player class
class Player:
    def __init__(self, ID, name, teamName):
        self.ID = ID
        self.name = name
        self.teamName = teamName


# Team class contains a list of Player
# Objects
class Team:
    count = 0

    def __int__(self, name):
        super().__init__(name)
        self.players = Player()

    def addPlayer(self, ID, name, team):
        self.player += Player(ID, name, team)

    def getTotalPlayersInSchool(self):
        return count

    # Complete the implementation


# School class contains a list of Team
# objects.
class School:
    pass


# Complete the implementation


arr = [2, 3, 4, 5]
count = 0

for i in arr:
    print(i)
    count = count + i

print(count)
