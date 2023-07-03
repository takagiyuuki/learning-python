def get_positive_numeral():
    """
    入力された値が正しいかどうか判断する
    """
    while True:
        x = input("> ")
        if x == str("end"):
            exit()
        try:
            x == float(x)
        except ValueError:
            print(x, "は数値に変換できません")
            continue
        except Exception as e:
            print(f"How exceptional! {e}")
            print("予期していないエラーです")
            exit()
        if float(x) <= 0:
            print(x, "は正の数ではありません")
        else:
            break
    return x


def square_root(x):
    """
    引数Xの平方根を求める
    """
    x = float(x)
    rnew = x
    diff = rnew - x / rnew
    while diff > 1.0e-6:
        r1 = rnew
        r2 = x / r1
        rnew = (r1 + r2) / 2
        # print(r1, rnew, r2)
        diff = r1 - r2
        if diff < 0:
            diff = -diff
    return rnew


while True:
    t = get_positive_numeral()
    r = square_root(t)
    print("結果は ", r)
