#!/usr/bin/env python3
'''
    These are various tools used by redbot
'''

import sys
import configparser

def load_arguments():
    '''Get/load command parameters 

    Args:

    Returns:
        arguments: A dictionary of lists of the options passed by the user
    '''
    arguments = {
        "action"    : False,
        "botname"   : False,
        "count"     : False,
        "id"        : False,
        "search"    : False,
        "url"       : False
    }

    for arg in sys.argv:
        # Confirm with the user that he selected to delete found files
        if "-action:" in arg:
            arguments["action"]     = arg[8:]
        elif "-botname:" in arg:
            arguments["botname"]    = arg[9:]
        elif "-count:" in arg:
            arguments["count"]      = int(arg[7:])
        elif "-id:" in arg:
            arguments["id"]         = arg[4:]
        elif "-search:" in arg:
            arguments["search"]     = arg[8:]
        elif "-url:" in arg:
            arguments["url"]        = arg[5:]

    return arguments

def load_config(filepath):
    '''Get/load command parameters 

    Args:

    Returns:
        arguments: A dictionary of lists of the options passed by the user
    '''
    config = configparser.ConfigParser()
    config.read(filepath)
    return config._sections


def create_tables(sqlite):
    cursor = sqlite.cursor()
    # Create table
    cursor.execute('''''')

    sqlite.commit()