# m = {
#     'a':50, 
#     'b':58, 
#     'c':56,
#     'd':40, 
#     'e':100, 
#     'f':20
#     }
# max=0
# sec=0
# thirmax=0
# r=[]
# for i in m:
#     if m[i]>max:
#         sec=max
#         max=m[i]
#     if m[i]>sec and m[i]<max:
#         sec=m[i]
# a=sec
# b=max
# r.append(a)
# r.append(b)
# print(r)




# m = {
#     'a':50, 
#     'b':58, 
#     'c':56,
#     'd':40, 
#     'e':100, 
#     'f':20
#     }
# max=0
# r=[]
# for i in m:
#     if m[i]>max:
#         max=m[i]
# b=max
# r.append(b)
# print(r)


m = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
    }
max=0
sec=0
thirmax=0
r=[]
for i in m:
    if m[i]>max:
        thirdmax=sec
        sec=max
        max=m[i]
    if m[i]>sec and m[i]<max:
        sec=max
        max=m[i]
    if m[i]>sec>m[i]<max:
       thirdmax=m[i]
a=thirdmax
b=sec
c=max
r.append(a)
r.append(b)
r.append(c)
print(r)