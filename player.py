"""Das Spielerobject"""

from pygame import image as pyimage
from pygame import transform as pytransform
import drawer
from healthbar import Healthbar

path = 'img//player//'

class Player(object):

    def __init__(self):
        self.IMG_stand = loadIMG(path + 'stand.png')
        self.IMG_dodgeL = loadIMG(path + 'dodgeL.png')
        self.IMG_dodgeR = loadIMG(path + 'dodgeR.png')
        self.IMG_attack = loadIMG(path + 'attack.png')

        self.centerPos = (drawer.CENTER[0] - int(self.IMG_stand.get_rect().width/2), int(drawer.CENTER[1]*1.1) )
        self.leftPos = ( int(self.centerPos[0]*0.7), self.centerPos[1] )
        self.rightPos = ( int(self.centerPos[0]*1.3), self.centerPos[1] )
        self.attackPos = ( self.centerPos[0], int(self.centerPos[1]*0.7) )
    
        self.curImg = self.IMG_stand
        self.curPos = self.centerPos

        self.posMode = 0
        self.timeTillStand = 0
        self.dodgeTime = 0.5
        self.attackDuration = 0.3

        self.damage = 20

        self.killedBosses = 0

        self.maxHealth = 100
        self.health = self.maxHealth

        self.healthbar = Healthbar(self.maxHealth, int(drawer.DISPLAY_WIDTH / 2), int( drawer.DISPLAY_HEIGHT * 0.9 ), int(drawer.DISPLAY_WIDTH * 0.4), int(drawer.DISPLAY_HEIGHT*0.05) )

    def update(self, dt):
        if self.health <= 0:
            return 'dead'
        if self.timeTillStand > 0:
            self.timeTillStand -= dt
            return
        if self.posMode != 0:
            self.goMiddle()
            return 'goMiddle'
    
    def draw(self):
        drawer.showIMG(self.curPos[0], self.curPos[1], self.curImg)
        self.healthbar.draw()
    
    def dodgeL(self):
        if self.posMode == 0:
            self.posMode = 1
            self.curPos = self.leftPos
            self.curImg = self.IMG_dodgeL
            self.timeTillStand = self.dodgeTime

    def dodgeR(self):
        if self.posMode == 0:
            self.posMode = 2
            self.curPos = self.rightPos
            self.curImg = self.IMG_dodgeR
            self.timeTillStand = self.dodgeTime
    
    def goMiddle(self):
        self.posMode = 0
        self.curPos = self.centerPos
        self.curImg = self.IMG_stand

    def attack(self, boss):
        if self.posMode == 0:

            boss.hurt( self.damage )

            self.posMode = 3
            self.curPos = self.attackPos
            self.curImg = self.IMG_attack
            self.timeTillStand = self.attackDuration
    
    def hurt(self, amount):
        self.health -= amount

        if self.health < 0:
            self.health = 0
            self.die()

        self.healthbar.setVal(self.health)

    def die(self):
        print("You killed " + str(self.killedBosses) + " bosses!")
        self.killedBosses = 0

    def ressurect(self):
        self.health = self.maxHealth
        self.timeTillStand = 0
        self.goMiddle()
        self.healthbar.setVal(self.health)
        self.killedBosses = 0



def loadIMG(path):
    return pytransform.scale( pyimage.load( path ), (int(drawer.DISPLAY_HEIGHT*0.3), int(drawer.DISPLAY_HEIGHT*0.3)) )