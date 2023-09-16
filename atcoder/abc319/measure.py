# 入力を受け取る
N = int(input())
S = ""

# Nの約数を求める
yakusuu = []
for j in range(1,10):
    if N%j == 0:
        yakusuu.append(j)
# Siを求める
for i in range(N+1):
    for j in yakusuu:
        if i % (N/j) == 0:
            S += str(j)
            break
        if j == yakusuu[-1]:
            S += "-"
print(S)