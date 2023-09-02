# 入力を受け取る
N = int(input())
A = [None for i in range(N)]
B = [None for i in range(N)]
C = [None for i in range(N)]
D = [None for i in range(N)]
for i in range(N):
    A[i], B[i], C[i], D[i] = map(int, input().split())
    A[i] += 1
    B[i] += 1
    C[i] += 1
    D[i] += 1

T = [[False for i in range(100)]for i in range(100)]
for i in range(N):
    for j in range(A[i], B[i]):
        for k in range(C[i], D[i]):
            T[j][k] = True
            
# 面積を数える
Answer = 0
for i in range(100):
	for j in range(100):
		if T[i][j]:
			Answer += 1
# 出力
print(Answer)