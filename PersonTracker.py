import Vector2
import PersonDetection

class PersonTracker:
    def __init__(self, inputDeviceCount, personDetection, imageRequester):
        self.savedPositions = [list() for i in range(inputDeviceCount)]
        self.personDetection = personDetection
        self.imageRequester = imageRequester
        self.currentMachineIndex = 0
    
    def setup(self):
        self.imageRequester.requestImage(0)

    def update(self):
        # get image
        if(not self.imageRequester.newImageAvailable(self.currentMachineIndex)):
            return  # No new image available yet
        image = self.imageRequester.getLatestImage(self.currentMachineIndex)

        # process image and save vectors
        self.savedPositions[self.currentMachineIndex].append(self.personDetection.detectPersons(image))

        self.currentMachineIndex = self.currentMachineIndex + 1 if self.currentMachineIndex + 1 < len(self.savedPositions) else 0

    def getData(self):
        returnValue = self.savedPositions
        self.savedPositions = [list() for i in range(inputDeviceCount)]
        return returnValue
