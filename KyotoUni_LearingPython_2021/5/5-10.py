import math

print(math.pi, math.sqrt(2))

x = "abc" + "def"
print(x)
x = "abc" + str(1.2)
print(x)
x = "abc" * 2
print(x)


c = 2.99792458e8
na = 6.02214076e23
form = "光速は{0:12.8g} m/s, アボガドロ数は {1:12.8g} mol**(-1) です"
print(form.format(c, na))
