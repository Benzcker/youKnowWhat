"""Enthält die Hauptmenuklasse"""

import drawer
from button import Button 
from pygame import QUIT as PYQUIT, MOUSEBUTTONUP as PYMOUSEUP, mouse

class mainMenu(object):
    """Das Hauptmenu object"""

    def __init__(self):
        self.buttonW = int(drawer.DISPLAY_WIDTH / 2)
        self.buttonH = int(drawer.DISPLAY_HEIGHT / 8)

        self.startButton = Button(drawer.CENTER[0] - int(self.buttonW/2), drawer.CENTER[1] - int(self.buttonH*1.3), self.buttonW, self.buttonH, (150, 250, 180), "START")
        self.moduleButton = Button(drawer.CENTER[0] - int(self.buttonW/2), drawer.CENTER[1], self.buttonW, self.buttonH, (150, 250, 180), "MODULES")
        self.optionsButton = Button(drawer.CENTER[0] - int(self.buttonW/2), drawer.CENTER[1] + int(self.buttonH*1.3), self.buttonW, self.buttonH, (150, 250, 180), "OPTIONS")
        self.exitButton = Button(drawer.CENTER[0] - int(self.buttonW/2), drawer.CENTER[1] + int(self.buttonH*2.6), self.buttonW, self.buttonH, (150, 250, 180), "EXIT")

        tempTitleObj = drawer.createTextObject(drawer.createFont(int(drawer.DISPLAY_HEIGHT/5)), 'YouKnowWhat?')
        self.title = drawer.Text( 
            drawer.CENTER[0] - int(tempTitleObj.get_rect().width/2), 
            drawer.CENTER[1] - int(tempTitleObj.get_rect().height*2),
            tempTitleObj
            )


    def update(self, events, dt):
        for event in events:
            if event.type == PYQUIT:
                #Aufs rote Kreuzgedrückt
                RUNNING = False
            elif event.type == PYMOUSEUP and event.button == 1:
                pressedButton = self.checkButtons(mouse.get_pos())
                if pressedButton == 1:
                    # Wechsel ins Spiel
                    return 1
                if pressedButton == 2:
                    # Wechsel ins Modulmenu
                    return 2
                elif pressedButton == 3:
                    # Wechsel ins Optionenmenu
                    return 3
                elif pressedButton == 4:
                    # Spiel stoppen
                    return 4
        return 0



    def checkButtons(self, mousePos):
        """Testet, ob irgendein Knopf gedrückt wurde"""
        if self.startButton.rect.collidepoint(mousePos):
            return 1
        elif self.moduleButton.rect.collidepoint(mousePos):
            return 2
        elif self.optionsButton.rect.collidepoint(mousePos):
            return 3
        elif self.exitButton.rect.collidepoint(mousePos):
            return 4
        else:
            return 0
    
    def getDrawStuff(self):
        """Gibt ein Tuple mit allen Elementen, die gemalt werden sollen, zurück"""
        return ( 
            self.startButton,
            self.moduleButton,
            self.optionsButton,
            self.exitButton,
            self.title
            )
