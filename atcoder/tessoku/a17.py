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
# 1つ前の頂点を記録する
pred = [None for i in range(N)]
pred[1] = 0
for i in range(2, N):
    #dp[i] = min(dp[i-1]+A[i], dp[i-2]+B[i])
    if dp[i-1]+A[i] <= dp[i-2]+B[i]:
        dp[i] = dp[i-1]+A[i]
        pred[i] = i-1
    else:
        dp[i] = dp[i-2]+B[i]
        pred[i] = i-2
# 経路を復元する
path = [N]
node = pred[-1]
while node != 0:
    path.append(node+1)
    node = pred[node]
path.append(1)
path.reverse()
# 出力
print(len(path))
for node in path:
    if node != path[-1]:
        print(node, end=" ")
    else:
        print(node, end="")