"""Nummernfeld"""

import drawer
from pygame import Rect as pyrect

class Numfield(object):
    """Nummernfeld"""


    def __init__(self, x, y, width, height, color, value=0):
        """Erstellt ein Nummernfeld Object"""
        self.value = str(value)
        self.selected = False
        self.rectangle = pyrect(x, y, width, height)
        self.color = color

        self.textObj = drawer.createTextObject( drawer.createFont(self.rectangle.height), str(self.value) )
        self.updateTextObj()

    def update(self):
        """Das Nummernfeld aktualisieren"""
        pass
    
    def draw(self):
        """Malt das Nummernfeld"""
        drawer.rect(self.rectangle, self.color)
        drawer.write(self.rectangle.left + int(self.rectangle.width*0.05), self.rectangle.top - int(self.rectangle.height*0.05), self.textObj)
    
    def updateTextObj(self):
        tempTxt = self.value
        if self.selected:
            tempTxt += '|'
        self.textObj = drawer.createTextObject( drawer.createFont(self.rectangle.height), tempTxt )

    def setValue(self, newValue):
        self.value = newValue
    
    def write(self, nr):
        if nr == -1:
            self.value = self.value[:-1]
        else:
            if self.value == '0':
                self.value = ''
            if len(self.value) <= 3:
                self.value += str(nr)
        
        if len(self.value) == 0:
            self.value = '0'

        self.updateTextObj()