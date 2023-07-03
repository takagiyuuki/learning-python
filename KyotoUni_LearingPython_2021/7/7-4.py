def f():
    print("f says Hello")


# 関数を引数でもらって実行する関数
def F(y):
    print("In F, ", end="")
    y()


# f を実行
f()
F(f)
