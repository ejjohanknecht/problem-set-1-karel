#====================================================
# Filename: Karel_Painting.py
# 
# Your name: Ella Johanknecht
# Who did you work with (if anyone)?:
# If you consulted AI, link to transcript: 
# Estimate for time spent on this prob (in hrs)?: 0.5
#====================================================

import karel

def main():
    orient_left()
    for i in range(3):
        paint_wall()
    go_home()
    yippee()

def orient_left():
# i've only seen karel spawn facing right but others have mentioned 
# seeing her spawn facing any direction so I wanted to cover any bases
    while left_is_clear():
        if right_is_blocked():
            for i in range(2):
                turn_left()
        if left_is_clear() and right_is_clear():
            turn_left()

def paint_wall():
    move()
    put_beeper()
    move()
    move()
    turn_left()
    move()

def go_home():
# the "paint_wall" functions get karel around the corner onto the 
# wall with their door, but this will make karel go inside
    move()
    turn_left()
    move()
    move()

def yippee():
    for i in range(6):
        turn_left()
