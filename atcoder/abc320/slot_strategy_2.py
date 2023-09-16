# 入力を受け取る
M = int(input())
S_1 = input()
S_2 = input()
S_3 = input()

second_dict1 = dict()
second_dict2 = dict()
second_dict3 = dict()
ans_dict = dict()
# 1,2,3において、それぞれの数字の、一番早いインデックスを調べる
for i in range(M):
    if S_1[i] not in second_dict1.keys():
        second_dict1[S_1[i]] = i
    if S_2[i] not in second_dict2.keys():
        second_dict2[S_2[i]] = i
    if S_3[i] not in second_dict3.keys():
        second_dict3[S_3[i]] = i

# 答えを合算する 
for target in second_dict1.keys():
    if second_dict1[target] == second_dict2[target] == second_dict3[target]:
        ans_dict[target] = second_dict1[target] + 2*M
    else:
        sor = sorted([second_dict1[target], second_dict2[target], second_dict3[target]])
        if sor[0] == sor[1]:
            ans_dict[target] = sor[0]+(sor[2]-sor[0])+(M-sor[2])
        elif sor[1] == sor[2]:
            ans_dict[target] = sor[0]+(sor[1]-sor[0])+M
        else:
            ans_dict[target] = sor[0]+(sor[1]-sor[0])+(sor[2]-sor[1])
print(min(ans_dict.values()))    