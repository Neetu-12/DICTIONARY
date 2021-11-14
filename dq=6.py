#method-2
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


#methode-2
d = {0:10, 1:20}
print(d)
d.update({2:30})
print(d)
