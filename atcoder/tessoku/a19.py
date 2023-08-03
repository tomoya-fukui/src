# 入力
N, W = map(int, input().split())
w = [None for i in range(N+1)]
v = [None for i in range(N+1)]
for i in range(1, N+1):
    w[i], v[i] = map(int, input().split())
    
# 動的計画法
dp = [[-1 for j in range(W+1)] for i in range(N+1)]
# i=0
dp[0][0] = 0
# i>=1
for i in range(1, N+1):
    for j in range(W+1):
        if j < w[i]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]]+v[i])
# 出力
print(max(dp[N]))