# 入力
Q = int(input())
X = [None for i in range(Q)]
for i in range(Q):
    X[i] = int(input())

# Q解質問に答える
for i in range(Q):
    ans = "Yes"
    for j in range(2, int(X[i]**(1/2))+1):
        if X[i]%j == 0:
            ans = "No"
            break
    print(ans)