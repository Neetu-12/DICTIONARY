a="MISSISSIPPI" 
i=0
r={}
while i<len(a):
    j=0
    c=0
    while j<len(a):
        if a[i]==a[j]:
            c=c+1
        j=j+1
        r.update({a[i]:c})
    i=i+1
print(r)
