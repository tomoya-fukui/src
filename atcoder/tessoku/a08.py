# 入力を受け取る
H, W = map(int, input().split())
X = [[] for i in range(H)]
Q = int(input())
A = [[] for i in range(Q)]
B = [[] for i in range(Q)]
C = [[] for i in range(Q)]
D = [[] for i in range(Q)]

# 累積和を取る
Z = [[] for i in range(H)]
# 横方向に累積和を取る
for i in range(H):
    for j in range(W):
        if j == 0:
            Z[i].append(X[i][j])
        else:
            Z[i].append(Z[i][j-1]+X[i][j])
# 縦方向に累積和を取る
for i in range(H):
    for j in range(W):
        if i != 0:
            Z[i][j] = Z[i][j-1]+Z[i][j]
            
# 質問に答える
        