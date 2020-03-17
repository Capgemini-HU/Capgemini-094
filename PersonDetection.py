import cv2
from imutils.object_detection import non_max_suppression
import numpy as np

# Custom packages
import Vector2

# Class definitions
class PersonDetection:
    def __init__(self):
        self.hog = cv2.HOGDescriptor()
        self.hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    def detectPersons(self, image):
        # image (CV2 image): The image to detect persons on.
        (rects, weights) = self.hog.detectMultiScale(image, winStride=(4, 4), padding=(8, 8), scale=1.05)
        rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects]) # Is this necessary?
        pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)
        
        returnList = []
        height, width, channels = image.shape
        xDivide = width/100
        yDivide = height/100
        for (xA, yA, xB, yB) in pick:
            returnList.append(Vector2( (xA + xB)/(2 * xDivide), (yA + yB)/(2 * yDivide)))  # Append the center of the found rectangles as coordinates between 0 and 100
        
        return returnList

