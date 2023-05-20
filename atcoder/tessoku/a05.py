# 入力を受け取る
n, k = list(map(int, input().split()))

cnt = 0

# 合計がkとなる組み合わせを考える
for r in range(1, n+1):
    for b in range(1, n+1):
        w = k-r-b
        if 1 <= w <= n:
            cnt+=1
print(cnt)