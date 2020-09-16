#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 10:37:24 2020

@author: u/Kurtopsy
"""

import praw
import os
import random

reddit = praw.Reddit(client_id='XXXXXXXXX',
                     client_secret="XXXXXXXXXXX", password='XXXXXXXXXXX',
                     user_agent='XXXXXXXXXXX', username='XXXXXXXXXXX')

yourFate = ['Council Rick','1 Day Ban', '3 Day Ban', '7 Day Ban', '14 Day Ban', '30 Day Ban']
messages = {
    "1 Day Ban": "You Teleported to Jerryboree (1 Day Ban)",
    "3 Day Ban": "You have Teleported to the Froopy Land and tommy has had his way with you (3 Day Ban)",
    "7 Day Ban": "You have Teleported to Matrix of Mortys (7 Day Ban)",
    "14 Day Ban": "You have Teleported to intergalactic Prison (14 Day Ban)",
    "30 Day Ban": "You have Teleported to the collectors menagerie (30 Day Ban)",
    "Council Rick": "You Teleported to the Council Chamber and won a seat for a week"
}


submission = reddit.submission(id='XXXXXXXX')

if not os.path.isfile("usernames.txt"):
    usernames = []
else:
   with open("usernames.txt", "r") as f:
       usernames = f.read()
       usernames = usernames.split("\n")
       usernames = list(filter(None, usernames))

with open("usernames.txt", "a") as f:
    for comment in submission.comments.list():
        lowercase_comment = comment.body
        cbody = lowercase_comment.lower()
        if comment.is_root:
            if "!portaljump" in cbody:
                if comment.author.name not in usernames:
                    f.write(comment.author.name + "\n")
                    f.close


for comment in submission.comments.list():
        lowercase_comment = comment.body
        cbody = lowercase_comment.lower() 
        if comment.is_root:
            if "!portaljump" in cbody and comment.author.name not in usernames:
                    my_option = (messages[random.choice(yourFate)])
                    if my_option == "You Teleported to Jerryboree (1 Day Ban)":
                        print(comment.author.name + my_option + "\n")
                        comment.reply("[{}](https://masterofallscience.com/meme/S02E02/82291.jpg?b64lines=WW91IFRlbGVwb3J0ZWQgdG8gSmVycnlib3JlZQoKCgoKCgoKCgoKCgoKKCAxIERheSBCYW4gKQ==) \n\n".format(my_option) + "***** \n\n " + "^beep, ^boop. ^What's ^my ^purpose?")
                        reddit.subreddit('TempConvertBot').banned.add(comment.author.name, duration=1, ban_reason='Portal Jump', ban_message='Poor luck on the spin, but thanks for playing.', note='Portal Jump')
                    elif my_option == "You have Teleported to the Froopy Land and tommy has had his way with you (3 Day Ban)":
                        print(comment.author.name + my_option + "\n")
                        comment.reply("[{}](https://masterofallscience.com/meme/S03E09/786744.jpg?b64lines=WW91IGhhdmUgVGVsZXBvcnRlZCB0byB0aGUgRnJvb3B5IExhbmQgCmFuZCB0b21teSBoYXMgaGFkIGhpcyB3YXkgd2l0aCB5b3UKCgoKCgoKCgoKCgoKKCAzIERheSBCYW4gKQ==) \n\n".format(my_option) + "***** \n\n " + "^beep, ^boop. ^What ^is ^my ^purpose?")
                        reddit.subreddit('TempConvertBot').banned.add(comment.author.name, duration=3, ban_reason='Portal Jump', ban_message='Poor luck on the spin, but thanks for playing.', note='Portal Jump')
                    elif my_option == "You have Teleported to Matrix of Mortys (7 Day Ban)":
                        print(comment.author.name + my_option + "\n")
                        comment.reply("[{}](https://masterofallscience.com/meme/S01E10/606356.jpg?b64lines=WW91IGhhdmUgVGVsZXBvcnRlZCB0byBNYXRyaXggb2YgTW9ydHlzCndoZXJlIHlvdSBnZXQgdG9ydHVyZWQgbGlrZSB0aGUgbW9ydHkgeW91IGFyZQoKCgoKCgoKCgoKCgooIDcgRGF5IEJhbiAp) \n\n".format(my_option) + "***** \n\n " + "^beep, ^boop. ^What ^is ^my ^purpose?")
                        reddit.subreddit('TempConvertBot').banned.add(comment.author.name, duration=7, ban_reason='Portal Jump', ban_message='Poor luck on the spin, but thanks for playing.', note='Portal Jump')
                    elif my_option == "You have Teleported to intergalactic Prison (14 Day Ban)":
                        print(comment.author.name + my_option + "\n")
                        comment.reply("[{}](https://masterofallscience.com/meme/S02E10/1276817.jpg?b64lines=WW91IGhhdmUgVGVsZXBvcnRlZCB0byB0aGUgSW50ZXJnYWxhY3RpYyBQcmlzb24KCgoKCgoKCgoKCgoKKCAxNCBEYXkgQmFuICk=) \n\n".format(my_option) + "***** \n\n " +  "^beep, ^boop. ^What ^is ^my ^purpose?")
                        reddit.subreddit('TempConvertBot').banned.add(comment.author.name, duration=14, ban_reason='Portal Jump', ban_message='Poor luck on the spin, but thanks for playing.', note='Portal Jump')
                    elif my_option == "You have Teleported to the collectors menagerie (30 Day Ban)":
                        print(comment.author.name + my_option + "\n")
                        comment.reply("[{}](https://masterofallscience.com/meme/S03E08/367784.jpg?b64lines=WW91IGhhdmUgVGVsZXBvcnRlZCB0byB0aGUgY29sbGVjdG9ycyBtZW5hZ2VyaWUKCgoKCgoKCgoKCgoKKCAzMCBEYXkgQmFuICk=) \n\n".format(my_option) + "***** \n\n " +  "^beep, ^boop. ^What ^is ^my ^purpose?")
                        reddit.subreddit('TempConvertBot').banned.add(comment.author.name, duration=30, ban_reason='Portal Jump', ban_message='Poor luck on the spin, but thanks for playing.', note='Portal Jump')
                    elif my_option == "You Teleported to the Council Chamber and won a seat for a week":
                        print(comment.author.name + my_option + "\n")
                        comment.reply("[{}](https://masterofallscience.com/meme/S01E10/286036.jpg?b64lines=T05FIE9GIFVTCgoKCgoKCgoKCgoKCgpOT1cgR08gQ0xFQU4gVEhFIFRPSUxFVFM=) \n\n".format(my_option) + "***** \n\n " +  "^beep, ^boop. ^What ^is ^my ^purpose?")
                    else:
                        comment.reply("You get nothing. You lose. Good day, sir." + "*****" +  "^beep, ^boop. ^What ^is ^my ^purpose?")
                                   

