"""Handhabung aller Modules"""

import os

modulePath = 'modules/'

def loadModules():
    """Module aus modules/ laden. """
    try:
        return os.listdir(modulePath)
    except:
        raise Exception('ERROR while loading modules from ' + modulePath)
        return []

def loadModulesFromPath(path):
    """Module aus modules/[path] laden"""
    try:
        return os.listdir(modulePath + path)
    except:
        raise Exception('ERROR while loading modules from ' + modulePath + path)
        return []
