al = input()
count=0
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in croatia:
    if i in al:
        count += al.count(i)
        al = al.replace(i,'^')
al = al.replace('^','')
print(count+len(al))