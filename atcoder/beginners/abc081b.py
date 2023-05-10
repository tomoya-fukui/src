# 入力を受け取る
N = int(input())
A = list(map(int, input().split()))
# 0で初期化する
count = 0

# 操作を何回できるか求める
while all(a % 2 == 0 for a in A):
    A = [a/2 for a in A]
    count += 1
print(count)