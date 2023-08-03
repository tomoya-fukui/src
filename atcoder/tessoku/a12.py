# 入力
N, K = map(int, input().split())
A = list(map(int, input().split()))

# 答えである何秒であるかに対して2分探索を行う
L = 1
R = 10**9
while L < R:
    M = (L+R)//2
    total = 0
    for i in range(N):
        total += M//A[i]
    # 時間が足りず、枚数が足りないとき、右側にある
    if total < K:
        L = M+1
    # 時間が長すぎ、枚数を超えるとき、左側にある
    elif total >= K:
        R = M
print(R)