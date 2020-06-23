import os
import cv2

from PersonTracker import PersonTracker
from ImageRequesterDummy import ImageRequesterDummy
from Vector2 import Vector2
from PersonDetection import PersonDetection

if __name__ == '__main__':
    imagesPath = os.path.join(".", "testImages")
    imagePrefix = "testImage"
    imageType = "jpg"

    imageRequesterDummy = ImageRequesterDummy(imagesPath, imagePrefix, imageType, 1)
    personDetection = PersonDetection()
    personTracker = PersonTracker(1, personDetection, imageRequesterDummy)

    for i in range(3):
        personTracker.update()
    
    listOfPersons = personTracker.getData()
    
    imagePath = os.path.join(imagesPath, imagePrefix + "0." + imageType)
    backgroundImage = cv2.imread(imagePath)
    height, width, channels = backgroundImage.shape
    xMultiplier = width/100
    yMultiplier = height/100
    color = (0, 0, 255)
    # mark all found persons
    for sensor in listOfPersons:
        for frameData in sensor:
            for personVector in frameData:
                coordinate = (int(round(personVector.x * xMultiplier)), int(round(personVector.y * yMultiplier)))
                cv2.circle(img = backgroundImage, center = coordinate, radius = 4, thickness=-1, color=color)

    cv2.imshow("found Persons", backgroundImage)
    cv2.waitKey()
