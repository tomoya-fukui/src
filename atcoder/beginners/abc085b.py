# 入力を受け取る
n = int(input())
D = []
for i in range(n):
    d = int(input())
    D.append(d)

count = 1
D = sorted(D, reverse=True)

# 何段重ねできるか計算する
for i in range(1, n):
    if D[i-1] > D[i]:
        count += 1
print(count)