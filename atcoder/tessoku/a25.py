# 入力
H, W = map(int, input().split())
c = [None for i in range(H)]
for i in range(H):
    c[i] = input()

# 動的計画法
dp = [[0 for j in range(W)] for i in range(H)]
for i in range(H):
    for j in range(W):
        if i == 0 and j == 0:
            dp[i][j] = 1
        else:
            if c[i-1][j] == ".":
                dp[i][j] += dp[i-1][j]
            if c[i][j-1] == ".":
                dp[i][j] += dp[i][j-1]
print(dp[H-1][W-1])