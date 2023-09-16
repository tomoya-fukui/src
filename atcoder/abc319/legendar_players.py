# 入力を受け取る
S = input()

rate = {
    "tourist":3858,
    "ksun48":3679,
    "Benq":3658,
    "Um_nik":3648,
    "apiad":3638,
    "Stonefeang":3630,
    "ecnerwala":3613,
    "mnbvmar":3555,
    "newbiedmy":3516,
    "semiexp":3481
}

# rateに対して探索を行う
for name in rate.keys():
    if S == name:
        print(rate[name])