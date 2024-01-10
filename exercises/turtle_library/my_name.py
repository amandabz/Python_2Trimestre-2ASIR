from turtle import *

# create a new Turtle object
t = Turtle()

# screen settings
screen = Screen()
screen.title("Amanda's name")

hideturtle()

# letter A
penup()
goto(-200, 0)
pendown()
goto(-160, 100)
goto(-120, 0)
penup()
goto(-180, 50)
pendown()
goto(-140, 50)
penup()

# letter M
goto(-100, 0)
pendown()
goto(-100, 100)
goto(-80, 50)
goto(-60, 100)
goto(-60, 0)
penup()

# letter A
goto(-40, 0)
pendown()
goto(0, 100)
goto(40, 0)
penup()
goto(-20, 50)
pendown()
goto(20, 50)
penup()

# letter N
goto(60, 0)
pendown()
goto(60, 100)
goto(100, 0)
goto(100, 100)
penup()

# letter D
goto(120, 0)
pendown()
goto(120, 100)
goto(160, 75)
goto(160, 25)
goto(120, 0)
penup()

# letter A
goto(180, 0)
pendown()
goto(220, 100)
goto(260, 0)
penup()
goto(200, 50)
pendown()
goto(240, 50)
penup()

# keeps the window open
screen.mainloop()





