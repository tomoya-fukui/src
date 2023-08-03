# 入力
N, X = map(int, input().split())
A = list(map(int, input().split()))

# 二分探索
L = 0
R = N-1
# 探索範囲がなくなるまで
while L <= R:
    # 中間をとる、インデックスにしたいから切り捨て
    M = (L+R)//2
    # 左にある時
    if X < A[M]:
        R = M-1
    # 当たったとき
    elif X == A[M]:
        print(M+1)
        break
    # 右にあるとき
    else:
        L = M+1