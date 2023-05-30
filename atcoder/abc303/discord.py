N, M = map(int, input().split())
A = [[] for i in range(M)]
for i in range(M):
    A[i] = list(map(int, input().split()))

S = set()

for i in range(M):
    for j in range(N-1):
        if A[i][j] < A[i][j+1]:
            S.add((A[i][j], A[i][j+1]))
        else:
            S.add((A[i][j+1], A[i][j]))
print((N*(N-1)//2)-len(S))