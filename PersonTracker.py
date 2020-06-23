from Vector2 import Vector2
from PersonDetection import PersonDetection

class PersonTracker:
    def __init__(self, inputDeviceCount, personDetection, imageRequester):
        self.savedPositions = [list() for i in range(inputDeviceCount)]
        self.personDetection = personDetection
        self.imageRequester = imageRequester
        self.currentMachineIndex = 0

    def update(self):
        # get image
        if(not self.imageRequester.newImageAvailable(self.currentMachineIndex)):
            self.imageRequester.requestImage(self.currentMachineIndex)
            return
        image = self.imageRequester.getLatestImage(self.currentMachineIndex)

        # process image and save vectors
        self.savedPositions[self.currentMachineIndex].append(self.personDetection.detectPersons(image))

        self.currentMachineIndex = self.currentMachineIndex + 1 if self.currentMachineIndex + 1 < len(self.savedPositions) else 0

    def getData(self):
        returnValue = self.savedPositions
        self.savedPositions = [list() for i in range(len(self.savedPositions))]
        return returnValue
