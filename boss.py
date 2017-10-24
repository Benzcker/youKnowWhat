"""Die Bossobjekte"""

from pygame import image as pyimage, transform as pytransform
import numpy as np
import drawer
from healthbar import Healthbar

class Boss(object):
    """Ein Gegner in dem Spiel"""

    def __init__(self, imgPath, name, damageMult, healthMult, player):
        self.player = player

        self.name = name
        self.nameTextObj = drawer.createTextObject( drawer.createFont(int(drawer.DISPLAY_HEIGHT*0.095)), self.name )
        self.nameX = int(drawer.DISPLAY_WIDTH / 2 - self.nameTextObj.get_rect().width/2)
        self.nameY = int(drawer.DISPLAY_HEIGHT * -0.01)

        self.IMG_stand = loadIMG(imgPath + 'stand.png')
        self.IMG_ausholen = loadIMG(imgPath + 'ausholen.png')
        self.IMG_attack = loadIMG(imgPath + 'attack.png')
        
        self.centerPos = (drawer.CENTER[0] - int(self.IMG_stand.get_rect().width/2), int(drawer.CENTER[1]*0.35) )
        self.attackPos = ( self.centerPos[0], int(self.centerPos[1]*2.1) )


        self.curIMG = self.IMG_stand
        self.curPos = self.centerPos

        self.posMode = 0
        self.clock = 0
        self.ausholDuration = 0.5
        self.attackDuration = 0.3
        self.standDuration = 2

        self.damageMult = damageMult
        self.damage = 10

        self.healthMult = healthMult
        self.maxHealth = 100
        self.health = self.maxHealth

        self.healthbar = Healthbar(self.maxHealth, \
            int(drawer.DISPLAY_WIDTH / 2), int(self.centerPos[1] * 0.5 ), \
            int(drawer.DISPLAY_WIDTH * 0.7), int(drawer.DISPLAY_HEIGHT*0.05) )
    
    def update(self, dt):
        if self.health <= 0:
            return True
        if self.posMode == 0:
            self.clock += np.random.rand() * dt / 2
        if self.clock > 0:
            self.clock -= dt
            return

        # Wenn der Code hier weitergeht, muss in die nächste Phase gegangen werden
        if self.posMode == 0:
            self.ausholen()
            return
        if self.posMode == 1:
            self.attack()
            return
        if self.posMode == 2:
            self.goMiddle()
            return

    
    def draw(self):
        drawer.showIMG(self.curPos[0], self.curPos[1], self.curIMG)
        self.healthbar.draw()
        drawer.write(self.nameX, self.nameY, self.nameTextObj)
    
    def ausholen(self):
        self.curIMG = self.IMG_ausholen
        self.posMode = 1
        self.clock = self.ausholDuration
    
    def attack(self):
        self.posMode = 2
        self.curIMG = self.IMG_attack
        self.curPos = self.attackPos
        self.clock = self.attackDuration

        if self.player.posMode == 0 or self.player.posMode == 3:
            self.player.hurt(self.damage)

    def goMiddle(self):
        self.posMode = 0
        self.curIMG = self.IMG_stand
        self.curPos = self.centerPos
        self.clock = self.standDuration
    
    def hurt(self, amount):
        self.health -= amount

        if self.health <= 0:
            self.health = 0
            self.die()
        
        self.healthbar.setVal(self.health)
    
    def die(self):
        self.player.killedBosses += 1
    
    def ressurect(self):
        self.goMiddle()
        self.health = self.maxHealth
        self.healthbar.maxVal = self.maxHealth
        self.healthbar.setVal(self.health)
        self.clock = 0


def loadIMG(path):
    return pytransform.scale( pyimage.load( path ), (int(drawer.DISPLAY_HEIGHT*0.3), int(drawer.DISPLAY_HEIGHT*0.3)) )