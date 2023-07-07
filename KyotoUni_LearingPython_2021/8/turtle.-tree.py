import turtle
# 再帰的に木を描く
def tree(n):
    # 引数が 1 以下なら 5 歩すすむ
    if n<=1:
        turtle.forward(5)
    else:
        # 引数は 1 より大きいとき
        # 引数の値に応じて前進(幹)
        turtle.forward(5*(1.1**n))
        # 今の位置と向きを記録
        xx = turtle.pos()
        h = turtle.heading()
        # 左へ 30 度回転
        turtle.left(30)
        # 大きさ n-2 で木を描く(左の枝)
        tree(n-2)
        # ペンを挙げて軌跡を残さない
        turtle.up()
        # 先に記録した位置(幹の先端)に戻る
        turtle.setpos(xx)
        turtle.setheading(h)
        # ペンを降ろす
        turtle.down()
        # 右へ 15 度
        turtle.right(15)
        # 大きさ n-1 で木を描く(右の枝)
        tree(n-1)
        # ペンを上げてもどる
        turtle.up()
        turtle.setpos(xx)
        turtle.setheading(h)
        # ペンを降ろす
        turtle.down()
# 時間がかかるので最も早い描画
turtle.speed(0)
# 大きさ 12 の木を描く
tree(12)