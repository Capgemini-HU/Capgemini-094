import cv2
import os

class ImageRequesterDummy:
    def __init__(self, pathToImages, imagePrefix, imageType, imageCount):
        self._pathToImages = pathToImages
        self._imagePrefix = imagePrefix
        self._imageType = imageType
        self._imageCount = imageCount
        self._lastImages = {}
        self._newImageAvailable = {}
        self._currentImageIndex = 0

    def requestImage(self, machineID):
        fullPath = os.path.join(self._pathToImages, self._imagePrefix + str(self._currentImageIndex)) + "." + self._imageType
        self._lastImages[machineID] = cv2.imread(fullPath, cv2.IMREAD_GRAYSCALE)
        self._currentImageIndex = self._currentImageIndex + 1 if self._currentImageIndex + 1 < self._imageCount else 0
        self._newImageAvailable[machineID] = True

    
    def getLatestImage(self, machineID):
        self._newImageAvailable[machineID] = False
        return self._lastImages[machineID]
    
    def newImageAvailable(self, machineID):
        if not machineID in self._newImageAvailable:
            self._newImageAvailable[machineID] = False
            return False
        return self._newImageAvailable[machineID]
