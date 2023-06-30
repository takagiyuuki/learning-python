tozai = ["三条", "四条", "五条"]
nanboku = ["堀川", "烏丸", "河原町"]
cross_table = []

for i in range(len(tozai)):
    street = []
    for j in range(len(nanboku)):
        cross = tozai[i] + nanboku[j]
        street.append(cross)
        # print("i, j = ", i, j, "cross = ", cross, "street = ", street)
    cross_table.append(street)
    # print("street = ", street, "cross_table = ", cross_table)

print(street)

for i in range(len(street)):
    if i < len(street) - 1:
        print(street[i], end=",")
    else:
        print(street[i])

street = ["三条河原町", "三条烏丸", "三条堀川"]
print(*street, sep=", ", end=" --- ")