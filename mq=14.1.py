a=[4,3,8,6,7,1,9,]
for i in range(1,len(a)):
    key=a[i]
    j=i-1
    while j>=0 and key<a[j]:
        a[j+1]=a[j]
        j=j-1
    else:
        a[j+1]=key
print(a)