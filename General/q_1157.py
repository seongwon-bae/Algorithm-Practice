import sys
word = sys.stdin.readline().rstrip()
word = word.upper()
char_dict = {}
for i in word:
    if i in char_dict:
        char_dict[i] += 1
    else:
        char_dict.update({i:1})
max=0
max_str = ''
answer=[]
for i, (k,v) in enumerate(char_dict.items()):
    if max < v:
        max_str = k
        max = v
answer.append(max_str)
for i, (k,v) in enumerate(char_dict.items()):
    if k!=max_str and max==v:
        answer.append(k)
if len(answer) <= 1:
    for i in answer:
        print(i)
else:
    print('?')