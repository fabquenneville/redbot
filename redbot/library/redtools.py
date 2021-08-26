#!/usr/bin/env python3
'''
    These are various tools used by redbot
'''


def remove_all_comments(reddit):
    print("Removing comments")
    count = 0
    for comment in reddit.user.me().comments.new(limit=None):
        count += 1
        comment.delete()
    print("Removed " + str(count) + " comments total")

def remove_all_posts(reddit):
    print("Removing posts")
    count = 0
    for post in reddit.user.me().submissions.new(limit=None):
        count += 1
        post.delete()
    print("Removed " + str(count) + " posts total")