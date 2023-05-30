# 入力を受け取る
N = int(input())
S = input()
T = input()
ans = "Yes"

# 与えられた条件を調べる
for i in range(N):
    if S[i] != T[i]:
        if not(S[i] == "1" and T[i] == "l"):
            if not(S[i] == "l" and T[i] == "1"):
                if not(S[i] == "0" and T[i] == "o"):
                    if not(S[i] == "o" and T[i] == "0"):
                        ans = "No"
print(ans)