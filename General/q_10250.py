T=int(input())
all_room=[]
for i in range(T):
    H,W,N = map(int, input().split())
    count=0
    floor = 0
    room = 1
    while count<N:
        if floor<H:
            floor += 1
        else:
            floor = 1
            room += 1
        count += 1
    if room < 10:
        room = f'0{str(room)}'
    full_room = f'{floor}{room}'
    all_room.append(full_room)
for i in all_room:
    print(i)