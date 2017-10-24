"""Enthaelt die Button Class"""

from pygame import Rect as pyRect
import drawer


class Button(object):
    """Ein Button Objekt"""
    
    def __init__(self, left, top, width, height, _color, text):
        """Initialisierung eines Buttons"""
        self.rect = pyRect(left, top, width, height)
        self.color = _color
        self.textObj = drawer.createTextObject( drawer.createFont(height), text)
        self.textX = self.rect.left + int(self.rect.width/2) - int(self.textObj.get_rect().width/2)
        self.textY = self.rect.top - int( self.textObj.get_rect().height * 0.05 )


    def draw(self):
        """Male diesen Button"""
        drawer.rect(self.rect, self.color)
        drawer.write(self.textX, self.textY, self.textObj)