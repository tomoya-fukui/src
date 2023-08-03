#import bisect

# 入力
N = int(input())
A = list(map(int, input().split()))

# 配列 T の作成（重複も消す）
T = list(set(A))
T.sort()

# 答えを求める
B = [ None ] * N
for i in range(N):
    """
	B[i] = bisect.bisect_left(T, A[i])
	B[i] += 1
    """
    L = 0
    R = len(T)
    while L <= R:
        M = (L+R)//2
        if A[i] < T[M]:
            R = M-1
        elif A[i] == T[M]:
            B[i] = M+1
            break
        else:
            L = M+1
# 答えを空白区切りで出力
Answer = [str(i) for i in B]
print(" ".join(Answer))