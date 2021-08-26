#!/usr/bin/env python3
'''
'''

import os
import praw
import sys
import sqlite3

# Normal import
try:
    from redbot.library.tools import load_arguments, load_config, create_tables
    from redbot.library.redtools import remove_all_comments, remove_all_posts
# Allow local import for development purposes
except ModuleNotFoundError:
    from library.tools import load_arguments, load_config, create_tables
    from library.redtools import remove_all_comments, remove_all_posts

def main():
    '''

    Args:

    Returns:
    '''
    # Get/load command parameters
    
    arguments   = load_arguments()
    config      = load_config("config.ini")
    botname     = False
    reddit      = False
    if arguments["botname"]:
        botname = arguments["botname"]
    elif config["OPTIONS"]:
        botname = config["OPTIONS"]["botname"]
    if botname:
        reddit = praw.Reddit(
            client_id       = config[botname]["client_id"],
            client_secret   = config[botname]["client_secret"],
            password        = config[botname]["password"],
            user_agent      = config[botname]["user_agent"],
            username        = config[botname]["username"]
        )
    
    if (arguments["action"] == "resetdb") and os.path.exists(config["OPTIONS"]["dbpath"]):
        os.remove(config["OPTIONS"]["dbpath"])

    sqlite     = sqlite3.connect('misc/redbot.db', detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    sqlite.row_factory = sqlite3.Row
    create_tables(sqlite)

    if reddit and (arguments["action"] == "delete_comments"):
        remove_all_comments(reddit)
    elif reddit and (arguments["action"] == "delete_posts"):
        remove_all_posts(reddit)
    elif reddit and (arguments["action"] == "delete_all"):
        remove_all_comments(reddit)
        remove_all_posts(reddit)

if __name__ == '__main__':
    main()