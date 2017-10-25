"""Startet youKnowWhat"""
import numpy as np
import pygame
import drawer
from mainMenu import mainMenu
from modulesMenu import modulesMenu
from optionsMenu import optionsMenu

from game import Game


def main():

    # keys erstellen
    numKeys = (pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9, pygame.K_BACKSPACE)
    numpadKeys = (pygame.K_KP0, pygame.K_KP1, pygame.K_KP2, pygame.K_KP3, pygame.K_KP4, pygame.K_KP5, pygame.K_KP6, pygame.K_KP7, pygame.K_KP8, pygame.K_KP9, pygame.K_BACKSPACE)

    # Zeitmanagement des Spiels
    CLOCK = pygame.time.Clock()

    # Frames per Second
    FPS = 30


    # 0=MainMenu, 1=Game, 2=Modules, 3=Options, 4=Stop
    mode = 0

    # Eigentliches Spiel erstellen
    GAME = Game()

    # Hauptmenu
    MAINMENU = mainMenu()
    # ModulesMenu
    MODULESMENU = modulesMenu()
    # OptionsMenu
    OPTIONSMENU = optionsMenu(numKeys, numpadKeys)

    SCREENS = (MAINMENU, GAME, MODULESMENU, OPTIONSMENU)


    # Startbildschirm auf mainMenu setzen
    curScreen = MAINMENU

    # GameLoop
    RUNNING = True
    while RUNNING:
        events = pygame.event.get()
        dt = CLOCK.get_time() / 1000

        curScreen = SCREENS[mode]
        mode = curScreen.update(events, dt)

        if curScreen == MAINMENU and mode == 2:
            MODULESMENU.updateModules()
        elif mode == 4:
            RUNNING = False
        

        # alles malen, was diesen Tick gemalt werden muss
        drawer.draw(curScreen.getDrawStuff())

        # 1 / 30 Sekunde warten, bis wir in den nächsten Tick gehen
        CLOCK.tick(FPS)

    # Pygame und Python nach Ausbruch aus Loop schließen
    pygame.quit()
    quit()


if __name__ == '__main__':
    main()
