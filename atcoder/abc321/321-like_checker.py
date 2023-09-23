N = input()
ans = "Yes"
for i in range(1, len(N)):
    if N[i-1]<=N[i]:
        ans = "No"
        break
print(ans)