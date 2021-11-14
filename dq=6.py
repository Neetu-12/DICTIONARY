i=0
k=10
r={}
while i<=2:
    j=i
    while j<=i:
        r.update({i:k})
        j=j+1
    k=k+10
    i=i+1
print(r)