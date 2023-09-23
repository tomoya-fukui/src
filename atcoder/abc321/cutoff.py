N, X = map(int, input().split())
A = list(map(int, input().split()))

total = 0
for i in range(N-1):
    total += A[i]
    
min_score = min(A)
max_score = max(A)
result = total - min_score - max_score
if result + max_score < X:
    print(-1)
else:
    if result + min_score >= X:
        print(0)
    elif result + max_score == X:
        print(max_score)
    else:
        print(X-result)