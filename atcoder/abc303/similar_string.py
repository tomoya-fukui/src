N = int(input())
S = input()
T = input()
ans = "Yes"
for i in range(N):
    #print(S[i], T[i])
    if S[i] != T[i]:
        if S[i] ==("0" or "o"):
            #print(S[i], T[i])
            if not(T[i] == "0" or "o"):
                ans = "No"
                print(S[i], T[i])
        elif S[i] == ("1" or "l"):
            #print(S[i], T[i])
            if not(T[i] == "1" or "l"):
                ans = "No"
                print(S[i], T[i])
        else:
            #print("")
            ans = "No"
print(ans)    