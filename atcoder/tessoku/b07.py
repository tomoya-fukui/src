# 入力を受け取る
t = int(input())
n = int(input())
L = [None]*n
R = [None]*n
for i in range(n):
    L[i], R[i] = map(int, input().split())

# 前の時刻との比を取る
T = [0]*(t+1)
for i in range(n):
    T[L[i]] += 1
    T[R[i]] -=1

# 累積和をとる
A = [0]*(t+1)
A[0] = T[0]
for i in range(1, t+1):
    A[i] = A[i-1]+T[i]
for i in range(t):
    print(A[i])