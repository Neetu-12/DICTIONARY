# a={'M':1,'I':4,'S':4,'P':2}
# for i in a.items():
#     print(i)


# a="MISSISSIPPI" 
# c1=2
# c2=2
# c3=2
# c4=1
# i=0
# r={}
# while i<len(a):
#     if a[i]=="M":
#         c1=c1+1
#     if a[i]=="I":
#         c2=c2+1
#     if a[i]=="S":
#         c3=c3+1
#     if a[i]=="P":
#         c4=c4+1
#     r.update({a[i]:c1})
#     r.update({a[i]:c2})
#     r.update({a[i]:c3})
#     r.update({a[i]:c4})
#     i=i+1
# print(r)


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

# a="MISSISSIPPI" 
# i=0
# r=[]
# while i<len(a):
#     j=0
#     c=0
#     while j<len(a):
#         if a[i]==a[j]:
#             c=c+1
#         j=j+1
#         r.update(a[i])
#     i=i+1
# print(r)