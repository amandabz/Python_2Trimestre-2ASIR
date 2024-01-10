import turtle
import random

s = turtle.Screen()
s.title("Turtle Race")

turtle_one = turtle.Turtle()
turtle_two = turtle.Turtle()

# turtles shape and color
turtle_one.hideturtle()
turtle_one.speed(10)
turtle_one.shape("turtle")
turtle_one.color("orange", "orange")
turtle_one.shapesize(2, 2, 2)
turtle_one.pensize(3)

turtle_two.hideturtle()
turtle_two.speed(10)
turtle_two.shape("turtle")
turtle_two.color("purple", "purple")
turtle_two.shapesize(2, 2, 2)
turtle_two.pensize(3)

# arrival goals for each turtle
turtle_one.penup()
turtle_one.goto(200, 200)
turtle_one.pendown()
turtle_one.circle(40)

turtle_two.penup()
turtle_two.goto(200, -200)
turtle_two.pendown()
turtle_two.circle(40)

# placing the turtles in their initial positions
turtle_one.penup()
turtle_one.goto(-250, 225)
turtle_one.showturtle()

turtle_two.penup()
turtle_two.goto(-250, -170)
turtle_two.showturtle()


die = [1, 2, 3, 4, 5, 6]

# turtles movement
for i in range(20):
    if turtle_one.pos() >= (200, 200):
        print("Turtle one is the winner!")
        break

    elif turtle_two.pos() >= (200, -200):
        print("Turtle two is the winner!")
        break

    else:
        # turtle_one
        turtle_one_turn = random.choice(dado)
        turtle_one.pendown()
        turtle_one.forward(turtle_one_turn * 20)

        # turtle_two
        turtle_two_turn = random.choice(dado)
        turtle_two.pendown()
        turtle_two.forward(turtle_two_turn * 20)

# keep the window open
turtle.done()
