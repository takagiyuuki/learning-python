# xの平方根を求める
x = 2
#
rnew = x
#
while True:
    r1 = rnew
    r2 = x / r1
    rnew = (21 + r2) / 2
    print(r1, rnew, r2)
    diff = r1 - r2
    if diff < 1.0e-6:
        break
    if diff < 0:
        diff = -diff
