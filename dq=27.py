a=[{'id': 1, 'success': True, 'name': 'Lary'},
 {'id': 2, 'success': False, 'name': 'Rabi'},
 {'id': 3, 'success': True, 'name': 'Alex'}]
s=0
n=input('enter the no')
for i in range(len(a)):
    for j in a[i]:
        if n in j:
            s=s+a[i][j]
print(s)