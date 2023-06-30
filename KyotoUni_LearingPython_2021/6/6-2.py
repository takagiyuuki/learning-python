a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(a)
# print(a[0])
# print(a[0][1])

sum = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        sum += a[i][j]
        print(i, j)
        print(sum)
