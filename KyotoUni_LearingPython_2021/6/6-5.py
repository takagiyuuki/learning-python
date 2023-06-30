tozai = ["三条", "四条", "五条"]
nanboku = ["堀川", "烏丸", "河原町"]

cross_table = []

for i in range(5):
    row = []
    for j in range(4):
        row.append("")
        cross_table.append(row)
        print("i, j ", i, j)
        print("row" , row)
        print("cross_table" , cross_table)
