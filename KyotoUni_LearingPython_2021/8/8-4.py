import turtle


def come(x, y):
    (xx, yy) = turtle.pos()
    newxy = ((xx + x) / 2, (yy + y) / 2)
    print(x, y)
    turtle.goto(newxy)


turtle.onscreenclick(come)
turtle.done
