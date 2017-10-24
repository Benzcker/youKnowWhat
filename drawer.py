"""Kümmert sich um alles, was mit dem Bildschirm zu tun hat"""

from pygame import draw as pydraw, display as pydisplay, font as pyfont
from options import loadOptions, saveOptions

# Pyfont initialisieren
pyfont.init()


OPTIONS = loadOptions()
if OPTIONS['DISPLAY_WIDTH'] < 600:
    OPTIONS['DISPLAY_WIDTH'] = 600
elif OPTIONS['DISPLAY_WIDTH'] > 2500:
    OPTIONS['DISPLAY_WIDTH'] = 2500

if OPTIONS['DISPLAY_HEIGHT'] < 600:
    OPTIONS['DISPLAY_HEIGHT'] = 600
elif OPTIONS['DISPLAY_HEIGHT'] > 2000:
    OPTIONS['DISPLAY_HEIGHT'] = 2000

# Display 
DISPLAY_WIDTH = OPTIONS['DISPLAY_WIDTH']
DISPLAY_HEIGHT = OPTIONS['DISPLAY_HEIGHT']



CENTER = (int(DISPLAY_WIDTH / 2), int(DISPLAY_HEIGHT / 2) )

def createTextObject(font, text):
    """Erstellt ein textObject für drawer.write(x, y, textObject)
    
    Es muss ein Font angegeben werden. siehe drawer.createFont(size)"""
    return font.render(text, False, (0, 0, 0))

def createFont(size):
    return pyfont.SysFont('Arial', size)



# Fenster erstellen
DISPLAY = pydisplay.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pydisplay.set_caption("YouKnowWhat?")




def draw(drawStuff):
    """Alles malen, was in diesem Tick gemalt werden soll"""
    # Hintergrund zurücksetzen
    DISPLAY.fill((255, 240, 200))

    # Zeug malen
    for thing in drawStuff:
        thing.draw()
    
    # Texte malen
    # TODO

    # Screen updaten (alles davor wurde nur in Speicher geladen, aber nicht wirklich gemalt)
    pydisplay.update()


def circle(x, y, radius, color, width=0):
    """Zeichnet einen Kreis.

        X und y sind der Mittelpunkt"""
    pydraw.circle(DISPLAY, color, (x, y), radius, width)

def rect(Rect, color, width=0):
    """Zeichnet ein Rechteck.

    Erstes Argument muss ein pygame.Rect() object sein"""
    pydraw.rect(DISPLAY, color, Rect, width)

def write(x, y, textObject):
    """Schreibt einen Text auf den Bildschirm.

    Der Text muss als textObject angegeben werden. Dieses kann mit drawer.createTextObject(font, text) erstellt werden"""
    DISPLAY.blit(textObject, (x, y))


def showIMG(x, y, img):
    DISPLAY.blit(img, (x, y))

class Text(object):
    """Ein simples Textobjekt"""

    def __init__(self, x, y, textObj):
        """Erstelle ein simples Textobject"""
        self.x = x
        self.y = y
        self.textObj = textObj
    
    def draw(self):
        write(self.x, self.y, self.textObj)