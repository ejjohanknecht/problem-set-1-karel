#========================================================
# Filename: Karel_Newspaper.py
# 
# Your name: Ella Johanknecht
# Who did you work with (if anyone)?:
# If you consulted AI, link to transcript:
# Estimate for time spent on this problem (in hrs)?: 0.5
#========================================================

import karel

def main():
    creep_along_left_wall()
    brave_the_outdoors()
    yoink()
    yippee()
    go_home()
    yippee()


def creep_along_left_wall():
    while left_is_blocked():
        if front_is_clear():
            move()
        if front_is_blocked():
            turn_right()

def brave_the_outdoors():
    turn_left()
    move()

def yoink():
    pick_beeper()

def turn_right():
    for i in range(3):
        turn_left()


def yippee():
    for i in range(6):
        turn_left()

def go_home():
    move()
    turn_right()
    move()
    turn_left()
    for i in range(2):
        move()
