a={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
b={}
c={}
d={}
e={}
for i in a:
    b[i]=a[i][0]
    c[i]=a[i][1]
    d[i]=a[i][2]
    e[i]=a[i][3]
print([b,c,d,e])