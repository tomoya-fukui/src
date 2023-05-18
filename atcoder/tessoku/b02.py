# 入力を受け取る
a, b = list(map(int, input().split()))

# 100の約数はあるか計算
for i in range(a, b+1):
    if 100%i == 0:
        print("Yes")
        break
    elif i == b:
        print("No")