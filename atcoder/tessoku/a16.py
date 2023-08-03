# 入力
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
# 配列の長さを合わせる
A = [0] + A
B = [0, 0] + B

# 動的計画法
dp = [None for i in range(N)]
dp[0] = 0
dp[1] = A[1]
for i in range(2, N):
    dp[i] = min(dp[i-1]+A[i], dp[i-2]+B[i])
print(dp[-1])