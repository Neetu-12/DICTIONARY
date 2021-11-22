a={'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
r={}
for i in a:
    r.update({i:[]})
print(r)