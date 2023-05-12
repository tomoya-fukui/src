# 入力を受け取る
n, a, b = map(int, input().split())
total = 0

# 満たす数を求める
for i in range(1, n+1):
    i = str(i)
    nums = list(map(int, list(i)))
    if a <= sum(nums) <= b:
        i = int(i)
        total += i
print(total)