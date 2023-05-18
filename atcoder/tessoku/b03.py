# 入力を受け取る
n = int(input())
A = list(map(int, input().split()))
ans = "No"

# 3つの商品の合計金額が1000になるか
for i in range(n):
    for j in range(n):
        for k in range(n):
            if A[i]+A[j]+A[k] == 1000 and i != j and j != k and k != i:
                ans = "Yes"
print(ans)