# 入力を受け取る
N, M, P = map(int, input().split())

# 計算する
moon_cnt = 0
# 最初の日はM日後
if N >= M:
    N -= M
    moon_cnt += 1
    # 以後、P日ごと
    moon_cnt = moon_cnt + (N // P)

# 出力する
print(moon_cnt)