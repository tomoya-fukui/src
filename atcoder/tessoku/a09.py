# 入力を受け取る
H, W, N = map(int, input().split())
A = [None for i in range(N)]
B = [None for i in range(N)]
C = [None for i in range(N)]
D = [None for i in range(N)]

for i in range(N):
    A[i], B[i], C[i], D[i] = map(int, input().split())
    
# 累積和を取る
X = [[0 for i in range(W+2)] for j in range(H+2)] 
Z = [[0 for i in range(W+2)] for j in range(H+2)]
# 各日付を加算
for i in range(N):
    X[A[i]][B[i]] += 1
    X[A[i]][D[i]+1] -= 1
    X[C[i]+1][B[i]] -= 1
    X[C[i]+1][D[i]+1] += 1
# 横方向に累積和を取る
for i in range(1, H+1):
    for j in range(1, W+1):
        Z[i][j] = Z[i][j-1]+X[i][j]
# 縦方向に累積和を取る
for j in range(1, W+1):
    for i in range(1, H+1):
        Z[i][j] = Z[i-1][j]+Z[i][j]
# 出力
for i in range(1, H+1):
    for j in range(1, W+1):
        if j >= 2:
            print(" ", end="")
        print(Z[i][j], end="")
    print("")
