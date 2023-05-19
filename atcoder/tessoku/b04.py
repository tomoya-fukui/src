# 入力を受け取る
n = input()
length = len(n)
ans = 0

# nを10進法に変換、出力する
for i in range(length):
    ans += 2**(length-1-i) * int(n[i])
print(ans)