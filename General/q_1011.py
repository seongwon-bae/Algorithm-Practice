T = int(input())
for _ in range(T):
    x,y=map(int,input().split())
    distance = y-x
    if distance <= 3:
        print(distance)
    else:
        n = int(distance**0.5)
        if distance == n**2:
            print(n*2-1)
        elif n**2 < distance <= n**2+n:
            print(2*n)
        else:
            print(2*n+1)