"""Modules-Screen"""

from copy import copy
import drawer
from button import Button
import modules
from pygame import QUIT as PYQUIT, MOUSEBUTTONUP as PYMOUSEBUTTONUP, mouse, KEYUP as PYKEYUP, K_ESCAPE

class modulesMenu(object):

    def __init__(self):
        self.buttonW = int(drawer.DISPLAY_WIDTH / 2)
        self.buttonH = int(drawer.DISPLAY_HEIGHT / 8)

        self.backButton = Button(int(drawer.CENTER[0]*0.1), int(drawer.CENTER[1]*0.1), int(self.buttonW/3), self.buttonH, (200, 74, 74), "Back")
        self.moduleSelector = moduleSelector()

    def update(self, events, dt):
        for event in events:
                if event.type == PYQUIT:
                    #Aufs rote Kreuz gedrückt
                    RUNNING = False
                elif event.type == PYMOUSEBUTTONUP and event.button == 1:
                    pressedButton = self.checkButtons(mouse.get_pos())
                    if pressedButton == 1:
                        return 0
                elif event.type == PYKEYUP:
                    # Taste losgelassen
                    if event.key == K_ESCAPE:
                        return 0
        return 2

    def checkButtons(self, mousePos):
        """Testet, ob irgendein Knopf gedrückt wurde"""
        if self.backButton.rect.collidepoint(mousePos):
            return 1
        elif self.moduleSelector.checkButtons(mousePos):
            pass
    
    def getDrawStuff(self):
        """Gibt ein Tuple mit allen Elementen, die gemalt werden sollen, zurück"""
        return ( 
            self.backButton,
            self.moduleSelector
            )
    
    def updateModules(self):
        self.moduleSelector = moduleSelector()



class moduleSelector(object):
    """Die Anzeige und Auswahl der Ordner und gespeicherten Module"""

    def __init__(self):
        # self.textX = int( drawer.DISPLAY_HEIGHT * 0.1 )
        # self.textY = int( drawer.DISPLAY_WIDTH * 0.15 )

        self.moduleDirs = modules.loadModules()
        txt = ''
        for mod in self.moduleDirs:
            txt += mod + '\n'
        self.links = self.getLinks()
    
    def draw(self):
        """Male die Links der Modulauswahl"""
        for link in self.links:
            link.draw()
    


    def getLinks(self):
        """Gibt die Links der Modulauswahl zurück"""
        temp = []

        for num, mod in enumerate(self.moduleDirs):
            temp.append( moduleLink(int(drawer.DISPLAY_WIDTH*0.1), int(drawer.DISPLAY_HEIGHT*(0.2+0.05*num)), mod, mod) )
            # temp.append( drawer.Text( int(drawer.DISPLAY_WIDTH*0.1), int(drawer.DISPLAY_HEIGHT*(0.2+0.05*num)), tempTextObj) )
        
        return temp

    def checkButtons(self, mousePos):
        """Testet, ob ein Link der Modulauswahl geklickt wurde"""
        for i, link in enumerate(self.links):
            if link.checkClick(mousePos):
                temp = link.click()
                if temp == False:
                    return False
                else:
                    if temp[0]:
                        # Ordner öffnen
                        link.offsetY = 0
                        for j, t in enumerate(temp[1]):
                            link.offsetY += t.rect.height
                            self.links.insert(i+j+1, t)
                        ind = i+len(link.childen)+1
                        while ind < len(self.links):
                            if self.links[ind] != link:
                                self.links[ind].y += link.offsetY
                            ind += 1
                        
                    else:
                        # Ordner schließen
                        for t in temp[1]:
                            self.links.remove(t)
                        ind = i
                        while ind < len(self.links):
                            if self.links[ind] != link:
                                self.links[ind].y -= link.offsetY
                            ind += 1

                    return True

class moduleLink(object):
    """Ein Link für die Module und Ordner"""
    def __init__(self, x, y, text, path):
        if text.endswith('.pcl'):
            # Typ Datei
            self.type = 0
            self.childrenOffset = 0
            self.children = []
            self.text = text[:-4]
        else:
            # Typ Ordner
            self.text = '> ' + text
            self.type = 1
        self.open = False
        self.path = path + '/'
        self.textObj = drawer.createTextObject( drawer.createFont(int(drawer.DISPLAY_HEIGHT*0.05)), self.text)
        self.x = x
        self.y = y
        self.rect = self.textObj.get_rect()

    def draw(self):
        """Male den Link"""
        drawer.write(self.x, self.y, self.textObj)
    
    def updateText(self):
        """Text des Links updaten"""
        self.textObj = drawer.createTextObject( drawer.createFont(int(drawer.DISPLAY_HEIGHT*0.05)), self.text)

    def click(self):
        """Link wurde geklickt"""
        if self.type == 0:
            # Ist ein Modul
            print( 'Loading module ' + self.text )
        elif '.' not in self.text:
            # Ist ein Ordner
            self.open = not self.open
            if self.open:
                self.text = '\ ' + self.text[1:]
                self.updateText()

                nextMods = modules.loadModulesFromPath(self.path)
                nModsLinks = []
                tempX = self.x + int(self.path.count('/')*0.02*drawer.DISPLAY_WIDTH)
                tempY = self.y + int(drawer.DISPLAY_HEIGHT*0.05)
                for mod in nextMods:
                    nModsLinks.append( moduleLink(tempX, tempY, mod, self.path + mod) )
                    tempY += int(drawer.DISPLAY_HEIGHT*0.05)

                self.childen = nModsLinks
                return [True, nModsLinks]

            else:
                for c in self.childen:
                    if c.open:
                        self.open = not self.open
                        return False

                self.text = '>' + self.text[2:]
                self.updateText()
                return [False, self.childen]

        return False

    
    def checkClick(self, point):
        tempRect = copy(self.rect)
        tempRect.left += self.x
        tempRect.top += self.y
        return tempRect.collidepoint(point)