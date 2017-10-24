"""Speichern und laden von Einstellungen"""

import _pickle as pickle

optionsLocation = "data//options.pcl"

def loadOptions():
    """Lade bereits gespeicherte (falls nicht vorhanden Standart-) Einstellungen"""
    try:
        with open(optionsLocation, "rb") as f:
            d = pickle.load(f)
    except:
        print("No " + optionsLocation + " found. Loading default settings")
        d = {
            "DISPLAY_WIDTH": 1000,
            "DISPLAY_HEIGHT": 700
        }
    return d

def saveOptions(_options):
    """Speichere die derzeitigen Einstellungen"""
    with open(optionsLocation, "wb") as f:
        pickle.dump(_options, f)