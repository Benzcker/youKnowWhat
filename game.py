"""Das eigentliche Spiel"""

from player import Player
from boss import Boss
from jsonLoader import loadBosses

class Game(object):

    def __init__(self):
        self.player = Player()
        self.bosses = []
        bossData = loadBosses()
        for bossD in bossData:
            self.bosses.append( Boss(bossD["imgPath"], bossD["name"], bossD["damageMult"], bossD["healthMult"], self.player) )
        self.bossInd = -1

        self.newBoss()
        
    
    def newBoss(self):
        self.bossInd += 1
        if self.bossInd >= len(self.bosses):
            self.bossInd = 0
        self.boss = self.bosses[self.bossInd]
        self.boss.damage = (self.player.killedBosses+1) * self.boss.damageMult
        self.boss.maxHealth = (self.player.killedBosses+1)*60 + (self.player.killedBosses+1)*self.boss.healthMult
        print("NextBossHealth: " + str(self.boss.maxHealth))
        self.boss.ressurect()
