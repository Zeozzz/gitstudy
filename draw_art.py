import turtle


def draw_square(brad):
    for i in range(4):
        brad.forward(100)
        brad.left(90)


def draw_art():
    window = turtle.Screen()
    window.bgcolor('red')
    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('yellow')
    brad.speed(10)
    for i in range(37):
        draw_square(brad)
        brad.left(10)
    window.exitonclick()


if __name__ == '__main__':
    draw_art()
