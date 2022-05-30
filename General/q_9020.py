li_num = [False, False] + [True]*10002
for i in range(2,10002):
    if li_num[i]:
        for j in range(i*2,10002, i):
            li_num[j] = False
T=int(input())
for _ in range(T):
    n=int(input())
    a = n//2
    b = a
    while a>0:
        if li_num[a] and li_num[b]:
            print(a, b)
            break
        else:
            a -= 1
            b += 1