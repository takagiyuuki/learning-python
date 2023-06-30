from os import sep


a = [5, 1, 3, 4]
print(a)
print(a[0])
print(a[1])
print(a[2])
print(a[3])

b = ["三条", "四条", "五条", "七条"]
c = 5
a = [c, 1, 3, 4]
d = [c + 1, c + 1, c + 1, c + 1]
print(a)
print(b)
print(c)
print(d)

a = [1] * 4
print(a)

e = list()
n = list(range(5))

print(e)
print(n)

s = list("abcde")
print(s)

t = "a textbook of Python"
tlist = t.split()
print(tlist)

t = "a-textbook-of-Python"
tlist = t.split("-")
print(tlist)

tlist = "a textbook of Python".split()
print(tlist)

tlist = "a-textbook-of-Python".split("-")
print(tlist)

a = [5, 1, 3, 4]
print(a[0])

a[1] = 2
print(a)

print(len(a))

a = [5, 1, 3, 4]
print(a[-1])

a = [5, 1, 3, 4]
b = a[1:3]
print(b)

a = [5, 1, 3, 4]
a.append(2)
print(a)

a = [5, 1, 3, 4]
a.append(2)
print(a)

a = [5, 1, 3, 4]
b = [2, 6]
a.extend(b)
print(a)

a = [5, 1, 3, 4]
b = [2, 6]
a.append(b)
print(a)

a = [1, 2, 3]
b = a
print(a)
print(b)

b[0] = 0
a[1] = 0
print(a)
print(b)

print(id(a), id(b))

a = 1
b = a
b = 2
print(a, b)

a = [[1, 2], [3, 4]]
b = a.copy()
print(a, b)

b.append([5, 6])
print(a)
print(b)

b[0][0] = 0
print(a)
print(b)

print(id(a[0]), id(b[0]))
