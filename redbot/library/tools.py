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
        "botname"   : False,
        "action"    : False
    }

    for arg in sys.argv:
        # Confirm with the user that he selected to delete found files
        if "-botname:" in arg:
            arguments["botname"] = arg[9:]
        elif "-action:" in arg:
            arguments["action"] = arg[8:]

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