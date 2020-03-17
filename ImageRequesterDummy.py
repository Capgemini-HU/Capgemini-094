import cv2


class ImageRequesterDummy:
    def __init__(self, pathToImages, imagePrefix, imageCount):
        self.pathToImages = pathToImages
        self.imagePrefix = imagePrefix
        self.imageCount = imageCount
        self.lastImages = {}
        self.newImageAvailable = {}
        self.currentImageIndex = 0

    def requestImage(self, machineID):
        self.lastImages[machineID] = cv2.imread(self.pathToImages + self.imagePrefix + str(self.currentImageIndex), cv.IMREAD_GRAYSCALE)
        self.currentImageIndex = self.currentImageIndex + 1 if self.currentImageIndex + 1 < self.imageCount else 0
        self.newImageAvailable[machineID] = True

    
    def getLatestImage(self, machineID):
        self.newImageAvailable[machineID] = False
        return self.lastImages[machineID]
    
    def newImageAvailable(self, machineID):
        return self.newImageAvailable[machineID]
