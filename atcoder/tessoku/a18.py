# 入力
N, S = map(int, input().split())
A = list(map(int, input().split()))
A = [0]+A
# 動的計画法
dp = [[None for j in range(S+1)] for i in range(N+1)]
# i=0 
dp[0][0] = True
for j in range(1, S+1):
    dp[0][j] = False
# i>=1
for i in range(1, N+1):
    for j in range(S+1):
        if j < A[i]:
            if dp[i-1][j]:
                dp[i][j] = True
            else:
                dp[i][j] = False
        if j >= A[i]:
            if dp[i-1][j] or dp[i-1][j-A[i]]:
                dp[i][j] = True
            else:
                dp[i][j] = False
if dp[N][S]:
    print("Yes")
else:
    print("No")