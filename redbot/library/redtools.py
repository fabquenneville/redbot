#!/usr/bin/env python3
'''
    These are various tools used by redbot
'''


def remove_all_comments(reddit):
    print("Removing comments")
    count = 0
    comments = list(reddit.user.me().comments.new(limit=None))
    while len(comments) > 0:
        for comment in comments:
            count += 1
            comment.delete()
        comments = list(reddit.user.me().comments.new(limit=None))
    print("Removed " + str(count) + " comments total")

def remove_all_posts(reddit):
    print("Removing posts")
    count = 0
    posts = list(reddit.user.me().submissions.new(limit=None))
    while len(posts) > 0:
        for post in posts:
            count += 1
            post.delete()
        posts = list(reddit.user.me().submissions.new(limit=None))
    print("Removed " + str(count) + " posts total")