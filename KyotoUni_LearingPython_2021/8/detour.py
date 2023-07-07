import turtle
def detour(L):
    if L < 10:
        turtle.forward(L)
    else:
        LL = L/3
        detour(LL)
        turtle.left(60)
        detour(LL)
        turtle.right(120)
        detour(LL)
        turtle.left(60)
        detour(LL)
for i in range(6):
    detour(100)