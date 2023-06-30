while True:
    x = input("平方根を求めたい数字を入力して下さい ")
    if x == str("end"):
        exit()
    try:
        x = float(x)
    except ValueError:
        print(x, "は数値に変換できません")
        continue
    except:
        print("予期していないエラーです")
        exit()
    if x <= 0:
        print(x, "は正の数ではありません")
    elif x >= 0:
        rnew = x
        diff = rnew - x / rnew

        if diff < 0:
            diff = abs(diff)

        while diff > 1.0e-6:
            r1 = rnew
            r2 = x / r1
            rnew = (r1 + r2) / 2
            print(r1, rnew, r2)
            diff = r1 - r2
            if diff < 0:
                diff = abs(diff)