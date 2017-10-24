import json


def loadBosses():
    bosses = json.load( open('data//bosses.json'))
    return bosses
