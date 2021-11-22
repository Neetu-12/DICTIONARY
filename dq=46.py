a=[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
r={}
for i in range(len(a)):
    for j in a[i]:
        b=(int(a[i][j]))
        r.update({j:b})
print(r)
