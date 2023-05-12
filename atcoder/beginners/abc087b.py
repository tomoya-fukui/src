# 入力を受け取る
num_500 = int(input())
num_100 = int(input())
num_50 = int(input())
target = int(input())
# 0で初期化する
case = 0
total = 0

# 合計金額を計算。条件を満たすものを数える
for i in range(num_500+1):
    for j in range(num_100+1):
        for k in range(num_50+1):
            total = 500*i+j*100+k*50
            if total == target:
                case += 1
print(case)