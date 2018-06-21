import turtle

# get number for random turtle and bg color
turtle_and_bg_color = int(
    input('Enter a number from 1 to 5 for a random background color and color for your turtle: '))

# random turtle and bg color logic
if turtle_and_bg_color == 1:
    turtle.color('#b7b6c1')
    turtle.bgcolor('#464655')

elif turtle_and_bg_color == 2:
    turtle.color('#d7be82')
    turtle.bgcolor('#515a47')

elif turtle_and_bg_color == 3:
    turtle.color('#1098f7')
    turtle.bgcolor('#000000')

elif turtle_and_bg_color == 4:
    turtle.color('#dc602e')
    turtle.bgcolor('#e7d7c1')

elif turtle_and_bg_color == 5:
    turtle.color('#e3d26f')
    turtle.bgcolor('#254441')


# get number for random spiral design
spiral_design = int(
    input('Enter a number from 1 to 4 for a random spiral design: '))

turtle.speed('fastest')

# random turtle design logic
if spiral_design == 1:
    # draw 300 circles, with turtle tilted by 5 degrees
    # after each circle is drawn
    for x in range(300):
        turtle.circle(100 + x)
        turtle.lt(5)

elif spiral_design == 2:
    # draw 800 lines, with turtle tilted 90.325 degrees left
    # after each line is drawn
    for x in range(800):
        turtle.fd(1 + x)
        turtle.lt(90.325)

elif spiral_design == 3:
    # draw 120 circles, with turtle tilted 10 degrees
    # after each circle is drawn
    for x in range(120):
        turtle.circle(360 + x)
        turtle.lt(10)

elif spiral_design == 4:
    # draw 600 lines, with turtle tilted 60.991 degrees left
    # # after each line is drawn
    for x in range(600):
        turtle.fd(1 + x)
        turtle.lt(60.911)


turtle.done()  # keep turtle on screen
turtle.exitonclick()  # click on screen to exit
