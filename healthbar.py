"""Eine Healthbar"""

import drawer
from pygame import rect as pyrect

class Healthbar(object):
    def __init__(self, maxVal, x, y, width, height):
        self.maxVal = maxVal
        self.val = self.maxVal
        self.rect = pyrect.Rect(x - int(width/2), y, width, height)
        self.backgroundRect = self.rect.copy()
    
    def setVal(self, val):
        self.val = val

        if self.val > self.maxVal:
            self.val = self.maxVal

        self.rect.width = int(self.backgroundRect.width * self.val / self.maxVal)

    
    def draw(self):
        drawer.rect( self.backgroundRect, (100, 100, 100) )
        if self.val > 0:
            drawer.rect( self.rect, (255, 0, 0) )