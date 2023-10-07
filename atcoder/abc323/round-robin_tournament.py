N = int(input())
S = [None for i in range(N)]
for i in range(N):
    S[i] = input()

# マルの数を数える
result = [0 for i in range(N)]
for i in range(N):
    for d in S[i]:
        if d == "o":
            result[i] += 1

ans = []
for j in range(N-1, 0, -1):
    ans += [str(i) for i, x in enumerate(result) if x == j]
    
print(" ".join(ans))