x,y,w,h = map(int, input().split())
height = h-y
length = w-x
mins = [x,y,height,length]
print(min(mins))