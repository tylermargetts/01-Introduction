#!/usr/bin/env python3

import utils
import time

utils.check_version((3,7))
utils.clear()

print("My name is Tyler Margetts.")
print("My favorite game is chess, but my favorite videogame is FIFA.")
print("I am concerned about not being able to know how to code what I want to make in a game.")
print("I am really excited for my electricity of the brain laboratory class.")
print("My stackoverflow username is: 11990752.")
print("The URL to my github profile is: https://github.com/tylermargetts")

answer = input("Would you like to hear a joke? ")
if answer.lower().strip() == 'yes':
    print("Why did the old man fall in the well? ")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("Because he couldn't see that well.")
else:
    print("Alright then, have a nice day!")

