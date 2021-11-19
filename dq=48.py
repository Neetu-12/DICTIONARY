1.)
a={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
c1={}
for i in a:
    c=0
    b=a[i]
    for j in a[i]:
        c=c+1
    c1.update({b:c})
print(c1)


2.)
a={'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
r={}
for i in a:
    c=0
    for j in a[i]:
        c=c+1
        b=a[i]
    r.update({b:c})
print(r)
