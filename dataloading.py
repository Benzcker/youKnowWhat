"""Management für Datentransfer und Speicherung"""

import os, sys, sqlite3


class m(object):
    """Erstellungsklasse für module handler. Nicht das hier importieren!!!"""

    def __init__(self):
        """moduleHandler erstellen"""
        self.path = 'data/modules.db'

    def loadModules(self):
        """ Module laden und ggf. Datenbank erstellen 
        
        Pfad: /data/modules.db"""

        connection = sqlite3.connect( self.path )
        cursor = connection.cursor()

        if not os.path.exists(self.path):
            # Datenbank exitstiert nicht, wird nun angelegt
            print('Datenbank modules.db nicht vorhanden - Datenbank wird angelegt')

            sql = 'CREATE TABLE modules('\
                'questName STRING, rightAnswer STRING, falseAnswer1 STRING, falseAnswer2 STRING, falseAnswer3 STRING, richtig INTEGER, falsch INTEGER '\
                ')'
            cursor.execute(sql)

            print('Anlegen der Datenbank modules.db mit ' + sql + ' abgeschlossen')
        
        connection.commit()
        connection.close()



moduleHandler = m()
moduleHandler.loadModules()
