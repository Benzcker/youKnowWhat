"""Startet youKnowWhat"""


def main():
    import numpy as np
    import pygame
    import drawer
    from mainMenu import mainMenu
    from modulesMenu import modulesMenu
    from optionsMenu import optionsMenu

    from game import Game

    # keys erstellen
    numKeys = (pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9, pygame.K_BACKSPACE)
    numpadKeys = (pygame.K_KP0, pygame.K_KP1, pygame.K_KP2, pygame.K_KP3, pygame.K_KP4, pygame.K_KP5, pygame.K_KP6, pygame.K_KP7, pygame.K_KP8, pygame.K_KP9, pygame.K_BACKSPACE)

    # Zeitmanagement des Spiels
    CLOCK = pygame.time.Clock()

    # Frames per Second
    FPS = 30

    # Multiplikator für Bilder die Sekunde (nur mathematisch, optisch bleibt immer 60)
    timeMultiplier = 0 # (Index!!)
    timeMultipliers = [1, 0.2]

    drawStuff = []

    # update & draw
    def update(thing, dt):
        """Updatet und malt Zeug"""
        res = thing.update(dt)
        drawStuff.append(thing)
        return res

    # Mode
    # 0=MainMenu, 1=Game, 2=Modules, 3=Options
    mode = 0

    # Hauptmenu
    MAINMENU = mainMenu()
    # ModulesMenu
    MODULESMENU = modulesMenu()
    # OptionsMenu
    OPTIONSMENU = optionsMenu()


    # Eigentliches Spiel erstellen
    GAME = Game()

    # GameLoop
    RUNNING = True
    while RUNNING:
        # drawStuff zurücksetzen
        drawStuff = []
        events = pygame.event.get()
        if mode == 0:
            # Event Handling in Main Menu
            for event in events:
                if event.type == pygame.QUIT:
                    #Aufs rote Kreuzgedrückt
                    RUNNING = False
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    pressedButton = MAINMENU.checkButtons(pygame.mouse.get_pos())
                    if pressedButton == 1:
                        # Wechsel ins Spiel
                        mode = 1
                    if pressedButton == 2:
                        # Wechsel ins Modulmenu
                        MODULESMENU.updateModules()
                        mode = 2
                    elif pressedButton == 3:
                        # Wechsel ins Optionenmenu
                        mode = 3
                    elif pressedButton == 4:
                        # Spiel stoppen
                        RUNNING = False
        

            
            drawStuff.extend(MAINMENU.getDrawStuff())

        elif mode == 1:
            # Event Handling in game
            dt = CLOCK.get_time() / 1000
            for event in events:
                if event.type == pygame.QUIT:
                    #Aufs rote Kreuz gedrückt
                    RUNNING = False
                elif event.type == pygame.KEYUP:
                    # Eine Taste wurde losgelassen
                    if event.key == pygame.K_ESCAPE:
                        mode = 0
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        GAME.player.dodgeL()
                        # timeMultiplier = 1
                    elif event.key == pygame.K_d:
                        GAME.player.dodgeR()
                        # timeMultiplier = 1
                    elif event.key == pygame.K_w:
                        GAME.player.attack( GAME.boss )
                        # timeMultiplier = 1
            
            bossDead = update(GAME.boss, dt * timeMultipliers[timeMultiplier])
            if bossDead:
                GAME.newBoss()

            
            playerUpd = update(GAME.player, dt * timeMultipliers[timeMultiplier])
            if playerUpd == 'goMiddle':
                timeMultiplier = 0
            elif playerUpd == 'dead':
                mode = 0
                GAME.bossInd = -1
                GAME.newBoss()
                GAME.player.ressurect()

        
        elif mode == 2:
            # Event handling in Modules Menu
            for event in events:
                if event.type == pygame.QUIT:
                    #Aufs rote Kreuz gedrückt
                    RUNNING = False
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    pressedButton = MODULESMENU.checkButtons(pygame.mouse.get_pos())
                    if pressedButton == 1:
                        mode = 0
                elif event.type == pygame.KEYUP:
                    # Taste losgelassen
                    if event.key == pygame.K_ESCAPE:
                        mode = 0


            drawStuff.extend(MODULESMENU.getDrawStuff())


        elif mode == 3:
            # Event handling in Options Menu
            for event in events:
                if event.type == pygame.QUIT:
                    #Aufs rote Kreuz gedrückt
                    RUNNING = False
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    pressedButton = OPTIONSMENU.checkButtons(pygame.mouse.get_pos())
                    if pressedButton == 1:
                        mode = 0
                elif event.type == pygame.KEYUP:
                    # Taste losgelassen
                    if OPTIONSMENU.selected == 0:
                        if event.key == pygame.K_ESCAPE:
                            mode = 0
                    else:
                        if event.key == pygame.K_ESCAPE:
                            OPTIONSMENU.select(0)
                        else:
                            OPTIONSMENU.write(event.key, numKeys, numpadKeys)


            drawStuff.extend(OPTIONSMENU.getDrawStuff())

            update(OPTIONSMENU.resolutionOptions, 1/FPS * timeMultipliers[timeMultiplier])


        # alles malen, was diesen Tick gemalt werden muss
        drawer.draw(drawStuff)

        # 1 / 30 Sekunde warten, bis wir in den nächsten Tick gehen
        CLOCK.tick(FPS)

    # Pygame und Python nach Ausbruch aus Loop schließen
    pygame.quit()
    quit()


if __name__ == '__main__':
    main()
