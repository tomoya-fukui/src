# 入力を受け取る
n, q = list(map(int, input().split()))
A = list(map(int, input().split()))

# 累積和を求める
T = [0]
for i in range(n):
    T.append(T[i]+A[i])
# 質問を受け取る
Q = []
for i in range(q):
    Q.append(list(map(int, input().split())))

for d in Q:
    print(T[d[1]]-T[d[0]-1])