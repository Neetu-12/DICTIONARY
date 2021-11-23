a={'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
c=0
for i in a:
    for j in range(len(a[i])):
        c=c+1
print(c)