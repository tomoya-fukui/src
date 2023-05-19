# 入力を受け取る
n = int(input())

ans = ""

# nを2進法に、10桁で表示する
for i in range(10):
    ans = str(n%2) + ans
    n = n//2
    if n == 0:
        break
ans = int(ans)
print(f"{ans:010}")