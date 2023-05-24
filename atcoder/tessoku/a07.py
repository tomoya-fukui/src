# 入力を受け取る
d = int(input())
n = int(input())
L = [None]*n
R = [None]*n
for i in range(n):
    L[i], R[i] = map(int, input().split())

# 前日比を求める
T = [0]*(d+2)
for i in range(n):
    T[L[i]] += 1
    T[R[i]+1] -= 1
    
# 累積和を取って出力
A = [0]*(d+1)
for i in range(1, d+1):
    A[i] = A[i-1]+T[i]

# 出力
for i in range(1, d+1):
    print(A[i])