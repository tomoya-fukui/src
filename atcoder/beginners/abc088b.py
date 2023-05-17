# 入力を受け取る
n = int(input())
A = list(map(int, input().split()))
A = sorted(A, reverse=True)

score_a = 0
score_b = 0

# 何点取るか計算
for i in range(1, n+1):
    if i%2 == 1:
        score_a += A[i-1]
    else:
        score_b += A[i-1]

# 差を表示
print(score_a-score_b)