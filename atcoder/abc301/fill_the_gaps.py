n = int(input())
a = list(map(int, input().split()))

def redo(n, a):
    for i in range(n-1):
        #print(i)
        if a[i]-a[i+1] < -1:
            a[i+1:i+1] = [d for d in range(a[i]+1, a[i+1])]
            redo(n, a)
        elif a[i]-a[i+1] > 1:
            a[i+1:i+1] = [d for d in range(a[i]-1, a[i+1], -1)]
            redo(n, a)
redo(n,a)
print(*a)