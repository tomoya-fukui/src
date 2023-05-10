# 入力を受け取る
s = input()
# 0でカウントを初期化する
count = 0

# 1つずつ取り出す
for d in s:
    if d == "1":
        count += 1
        
print(count)