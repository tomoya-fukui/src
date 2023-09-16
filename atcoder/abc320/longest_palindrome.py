# 入力を受け取る
S = input()
ans = 1
for i in range(len(S)):
    for j in range(i+1, len(S)):
        string = S[i:j+1]
        reversed_string = string[::-1]
        if string == reversed_string:
            if len(string) > ans:
                ans = len(string)
print(ans)