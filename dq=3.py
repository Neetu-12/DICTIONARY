i=1
r={}
while i<=5:
    a=i**2
    r.update({i:a})
    i=i+1
print(r)