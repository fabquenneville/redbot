#!/usr/bin/env python3
'''
    These are various tools used by mediacurator
'''

import sys

def load_arguments():
    '''Get/load command parameters 

    Args:

    Returns:
        arguments: A dictionary of lists of the options passed by the user
    '''
    arguments = {
        "directories":list(),
        "files":list(),
        "inputs":list(),
        "filters":list(),
        "outputs":list(),
        "printop":list(),
    }

    for arg in sys.argv:
        # Confirm with the user that he selected to delete found files
        if "-in:" in arg:
            arguments["inputs"] += arg[4:].split(",")
        elif "-filters:" in arg:
            arguments["filters"] += arg[9:].split(",")
        elif "-out:" in arg:
            arguments["outputs"] += arg[5:].split(",")
        elif "-print:" in arg:
            arguments["printop"] += arg[7:].split(",")
        elif "-files:" in arg:
            arguments["files"] += arg[7:].split(",,")
        elif "-dirs:" in arg:
            arguments["directories"] += arg[6:].split(",,")

    return arguments
