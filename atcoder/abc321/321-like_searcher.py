K = int(input())

def is_321_like_num(N):
    N = str(N)
    ans = True
    for i in range(1, len(N)):
        if N[i-1]<=N[i]:
            ans = False
            break
    return ans

def next_step(N):
    N = str(N)
    first = int(N[0])+1
    result = str(first)
    result = result + "0"*(len(N)-1)
    return int(result)

cnt = 0
target = 0
while cnt < K:
    if target % 11 == 0:
        target = next_step(target)        
    else:
            target += 1
    if is_321_like_num(target):
        cnt += 1
        #print(target)
print(target)