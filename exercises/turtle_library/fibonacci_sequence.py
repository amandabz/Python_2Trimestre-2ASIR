import turtle


def draw_window():
    window = turtle.Screen()
    window.bgcolor("white")

    draw_spiral()
    window.exitonclick()


def draw_spiral():
    # draw the Fibonacci spiral
    t = turtle.Turtle()
    t.shape("classic")
    t.pensize(5)

    # size of the spiral from (6, 13)
    for x in range(6, 13):
        a = fibonacci(x)
        print(a)
        t.circle(a, 90)


def fibonacci(n):
    fib1 = 0
    fib2 = 1

    if n == 0:
        return fib1

    elif n == 1:
        return fib2

    else:
        for i in range(n - 1):
            fib = fib1 + fib2
            fib1 = fib2
            fib2 = fib
            
        return fib


draw_window()
