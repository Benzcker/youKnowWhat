"""Options-Screen"""

import drawer
from button import Button
from numberInput import Numfield
from pygame import Rect as pyrect
import options

OPTIONS = options.loadOptions()

class optionsMenu(object):

    def __init__(self):
        self.buttonW = int(drawer.DISPLAY_WIDTH / 2)
        self.buttonH = int(drawer.DISPLAY_HEIGHT / 8)

        self.selected = 0

        self.backButton = Button(int(drawer.CENTER[0]*0.1), int(drawer.CENTER[1]*0.1), int(self.buttonW/3), self.buttonH, (200, 74, 74), "Back")

        self.resolutionOptions = resolutionOptions(int(drawer.CENTER[1]*0.4), int(drawer.DISPLAY_WIDTH*0.15), int(drawer.DISPLAY_HEIGHT/15), "Bildschirmauflösung*: ")

        self.credits = Credits( ("CREDITS:", "Programming: Benito Zenz", "Graphics: Richard Ernst", "", "* Spiel neu starten, um Änderungen anzuwenden"))

    def checkButtons(self, mousePos):
        """Testet, ob irgendein Knopf gedrückt wurde"""
        if self.backButton.rect.collidepoint(mousePos):
            return 1
        elif self.resolutionOptions.widthField.rectangle.collidepoint(mousePos):
            self.select(1)
        elif self.resolutionOptions.heightField.rectangle.collidepoint(mousePos):
            self.select(2)
    
    def select(self, nr):
        """Festlegen, welches Feld derzeit ausgewählt ist
        
        0=None, 1=resolutionWidth, 2=resolutionHeight"""
        self.selected = nr
        if nr == 0:
            self.deselectAll()
            return
        elif nr == 1:
            self.deselectAll()
            self.resolutionOptions.widthField.value = '0'
            self.resolutionOptions.widthField.selected = True
            self.resolutionOptions.widthField.updateTextObj()
        elif nr == 2:
            self.deselectAll()
            self.resolutionOptions.heightField.value = '0'
            self.resolutionOptions.heightField.selected = True
            self.resolutionOptions.heightField.updateTextObj()

    def deselectAll(self):
        self.resolutionOptions.widthField.selected = False
        self.resolutionOptions.widthField.updateTextObj()
        self.resolutionOptions.heightField.selected = False
        self.resolutionOptions.heightField.updateTextObj()

    def write(self, key, numKeys, numpadKeys):
        

        found = False
        for i in range(len(numKeys)):
            if key == numKeys[i] or key == numpadKeys[i]:
                if i == 10:
                    nr = -1
                else:
                    nr = i
                found = True
                break
        
        if not found:
            return

        if self.selected == 0:
            return
        elif self.selected == 1:
            self.resolutionOptions.widthField.write(nr)
            OPTIONS['DISPLAY_WIDTH'] = int(self.resolutionOptions.widthField.value)
        elif self.selected == 2:
            self.resolutionOptions.heightField.write(nr)
            OPTIONS['DISPLAY_HEIGHT'] = int(self.resolutionOptions.heightField.value)
        options.saveOptions(OPTIONS)



    
    def getDrawStuff(self):
        """Gibt ein Tuple mit allen Elementen, die gemalt werden sollen, zurück"""
        return ( 
            self.backButton,
            self.credits
            )

class resolutionOptions(object):
    """Die Einstellungen für die Auflösung"""

    def __init__(self, y, numfWidth, numfHeight, description):
        """Erstelle die Auflösungsoptionen"""
        self.descriptionObj = drawer.createTextObject( drawer.createFont( numfHeight), description )
        self.width = int(self.descriptionObj.get_rect().width + numfWidth*2.1)
        self.descriptionX = drawer.CENTER[0] - int(self.width/2)

        self.widthField = Numfield(self.descriptionX + self.descriptionObj.get_rect().width + int(numfWidth*0.05), y, numfWidth, numfHeight, (240, 240, 240), drawer.DISPLAY_WIDTH)
        self.heightField = Numfield(self.descriptionX + self.descriptionObj.get_rect().width + int(numfWidth*1.1), y, numfWidth, numfHeight, (240, 240, 240), drawer.DISPLAY_HEIGHT)
        self.rect = pyrect(self.descriptionX, y, self.descriptionObj.get_rect().width + int(numfWidth*2.1), numfHeight)

        self.widthField.updateTextObj()
        self.heightField.updateTextObj()
    
    def update(self, dt):
        """Auflösungsoptionen aktualisieren"""
        pass
    
    def draw(self):
        """Auflösungsoptionen malen"""
        drawer.write(self.descriptionX, self.rect.top, self.descriptionObj)
        self.widthField.draw()
        self.heightField.draw()


class Credits(object):
    """Die Credits im Optionsmenu"""
    def __init__(self, textList):
        self.creditObjs = []
        self.xs = []
        self.ys = []

        c = 0
        for text in textList:
            self.creditObjs.append( drawer.createTextObject(drawer.createFont(int(drawer.DISPLAY_HEIGHT/30)), text) )
            self.xs.append( drawer.CENTER[0] - int(self.creditObjs[c].get_rect().width / 2) )
            self.ys.append( int(drawer.DISPLAY_HEIGHT * 0.98) - int( self.creditObjs[c].get_rect().height * (len(textList)-c) ) )
            c += 1
            pass
    
    def draw(self):
        c = 0
        for creditObj in self.creditObjs:
            drawer.write(self.xs[c], self.ys[c], creditObj)
            c += 1