a={'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
for i in a:
    print(i,end=" ")
print(" ")
i=0
while i<len(a):
    for j in a:
        print(a[j][i],end=" ")
    print(" ")
    i+=1      

# my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# for row in zip(*([key] + (value) for key, value in sorted(my_dict.items()))):
#     print(*row)     


# a= {"a": 1, "b": 20, "c": 3}
# max_key = max(a, key=a.get)
# print(max_key)