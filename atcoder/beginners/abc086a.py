# 整数の入力を半角スペースで受け取る
a, b = map(int, input().split())

# 積の偶数、奇数で場合分け
if (a * b) % 2 == 0:
    print("Even")
else:
    print("Odd") 