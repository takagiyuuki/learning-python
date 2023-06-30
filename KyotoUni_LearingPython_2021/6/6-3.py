a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sum = 0

for row in a:
    for element in row:
        sum += element
        print(sum)
