# 入力を受け取る
n, x = list(map(int, input().split()))
A = list(map(int, input().split()))

# xをAが含むか
if x in A:
    print("Yes")
else:
    print("No")