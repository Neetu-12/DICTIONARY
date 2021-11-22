1)
a=[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
r={}
for i in range(len(a)):
    for j in a[i]:
        b=(int(a[i][j]))
        r.update({j:b})
print([r])

2)
b=[{'x': '10.12', 'y': '20.23', 'z': '30'}, {'p': '40.00', 'q': '50.19', 'r': '60.99'}]
r1={}
for i in range(len(b)):
    for j in b[i]:
        c=float(b[i][j])
        r1.update({j:c})
print([r1])
