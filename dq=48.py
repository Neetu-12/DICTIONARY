a={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
c1={}
for i in a:
    c=0
    b=a[i]
    for j in a[i]:
        c=c+1
    c1.update({b:c})
print(c1)