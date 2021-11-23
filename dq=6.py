#method-1
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

#method-3
a= {0: 10, 1: 20}
r={}
r.update(a)
r.update({2:30})
print(r)
