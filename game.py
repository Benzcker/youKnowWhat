"""Das eigentliche Spiel"""

from player import Player
from boss import Boss
from jsonLoader import loadBosses
from pygame import QUIT as PYQUIT, KEYUP as PYKEYUP, KEYDOWN as PYKEYDOWN, K_a, K_d, K_w, K_ESCAPE



class Game(object):

    def __init__(self):
        self.player = Player()
        self.bosses = []
        bossData = loadBosses()
        for bossD in bossData:
            self.bosses.append( Boss(bossD["imgPath"], bossD["name"], bossD["damageMult"], bossD["healthMult"], self.player) )
        self.bossInd = -1

        self.newBoss()

        # Multiplikator für Bilder die Sekunde (nur mathematisch, optisch bleibt immer 60)
        self.timeMultiplier = 0 # (Index!!)
        self.timeMultipliers = [1, 0.2]
        
    def update(self, events, dt):
        for event in events:
                if event.type == PYQUIT:
                    #Aufs rote Kreuz gedrückt
                    return 4
                elif event.type == PYKEYUP:
                    # Eine Taste wurde losgelassen
                    if event.key == K_ESCAPE:
                        return 0
                elif event.type == PYKEYDOWN:
                    if event.key == K_a:
                        self.player.dodgeL()
                        # self.timeMultiplier = 1
                    elif event.key == K_d:
                        self.player.dodgeR()
                        # self.timeMultiplier = 1
                    elif event.key == K_w:
                        self.player.attack( self.boss )
                        # self.timeMultiplier = 1
        
            
        bossDead = self.boss.update(dt * self.timeMultipliers[self.timeMultiplier])
        if bossDead:
            self.newBoss()

        
        playerUpd = self.player.update(dt * self.timeMultipliers[self.timeMultiplier])
        if playerUpd == 'goMiddle':
            timeMultiplier = 0
        elif playerUpd == 'dead':
            # Spieler ist gestorben
            self.bossInd = -1
            self.newBoss()
            self.player.ressurect()
            return 0
        
        return 1
    
    def newBoss(self):
        self.bossInd += 1
        if self.bossInd >= len(self.bosses):
            self.bossInd = 0
        self.boss = self.bosses[self.bossInd]
        self.boss.damage = (self.player.killedBosses+1) * self.boss.damageMult
        self.boss.maxHealth = (self.player.killedBosses+1)*60 + (self.player.killedBosses+1)*self.boss.healthMult
        print("NextBossHealth: " + str(self.boss.maxHealth))
        self.boss.ressurect()

    def getDrawStuff(self):
        return (
            self.boss, 
            self.player
            )