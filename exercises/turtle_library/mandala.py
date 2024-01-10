from turtle import *


def square(length):
    # four times
    for i in range(4):
        # move forward
        forward(length)
        # and turn 90 degrees
        right(90)


def spiral():
    for i in range(72):
        # draw a square of 100 units
        square(100)
        # and turn 5 degrees
        right(5)


speed(0)

# draw a spiral
spiral()

# keep the window open
done()
