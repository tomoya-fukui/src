n = int(input())
s = input()

cnt_t = 0
cnt_a = 0

for d in s:
    if d == "T":
        cnt_t += 1
        if cnt_t >= n/2:
            print("T")
            break
    else:
        cnt_a += 1
        if cnt_a >= n/2:
            print("A")
            break