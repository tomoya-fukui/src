import random
# 入力を受け取る
C = [list(map(int, input().split())) for i in range(3)]

# try_num回やってみる
try_num = 1000
target_num = 0
for try_i in range(try_num):
    for i in range(9):
        
    target_num += 1
print(target_num/try_num)