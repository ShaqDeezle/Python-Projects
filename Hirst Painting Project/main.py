import colorgram as cg
import turtle as t
import random

colors = cg.extract("hirst_dot_painting.jpg", 30)

rgb_colors = []

pointer = t.Turtle()

for i in colors:
    # print(i.rgb)
    # rgb_colors.append(i.rgb)
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b

    my_tuple = (r, g, b)

    rgb_colors.append(my_tuple)

# print(rgb_colors)

list_of_colors = rgb_colors

my_window = t.Screen()

my_window.colormode(255)

pointer.speed("fastest")


def draw(length, x):
    for i in range(length):
        for j in range(length):
            c = random.choice(list_of_colors)
            # c = list_of_colors[z]
            # pointer.pendown()

            pointer.dot(20, c)
            pointer.penup()
            pointer.forward(length)

        pointer.back(length * x)
        pointer.right(90)
        pointer.forward(length)
        pointer.left(90)


draw(20, 20)

pointer.hideturtle()  # hide the turtle
my_window.exitonclick()
