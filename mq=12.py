n=int(input("enter the no."))
r={}
i=1
while i<=n:
    a=i**2
    r.update({i:a})
    i=i+1
print(r)

