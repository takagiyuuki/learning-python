tozai = ["三条", "四条", "五条"]
nanboku = ["堀川", "烏丸", "河原町"]
cross_table = [["", "", ""], ["", "", ""], ["", "", ""]]

for i in range(len(tozai)):
    for j in range(len(nanboku)):
        cross = tozai[i] + nanboku[j]
        cross_table[i][j] = cross
        print(i, j)
        print(cross_table)