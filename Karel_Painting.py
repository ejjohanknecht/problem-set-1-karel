#====================================================
# Filename: Karel_Painting.py
# 
# Your name: Ella Johanknecht
# Who did you work with (if anyone)?:
# If you consulted AI, link to transcript: 
# Estimate for time spent on this prob (in hrs)?: 1
#====================================================

import karel

def main():
    orient_left()
    for i in range(3):
        paint_wall()
    go_inside()
    yippee()


def orient_left():
# this ensures karel paints their house counterclockwise
    while left_is_clear():
        if right_is_blocked():
            for i in range(2):
                turn_left()
        if left_is_clear() and right_is_clear():
            turn_left()

def paint_wall():
# i wasn't sure how to put the beepers in a pretty or symmetrical way 
# along the walls, but this accomplishes the same thing
    put_beeper()
    while left_is_blocked():
        if front_is_clear():
            move()
    if left_is_clear():
        turn_left()
        move()

def go_inside():
# gets karel inside their house with enough room for karel to celebrate
    while left_is_blocked():
        if front_is_clear():
            move()
    if left_is_clear():
        turn_left()
        move()
        move()

def yippee():
    for i in range(6):
        turn_left()
