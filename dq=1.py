# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# d3={}
# for i in d1:
#     for j in d2:
#         if i==j:
#             s=d1[i]+d2[j]
#             d3.update({i:s})
# d3.update(d1)
# d3.update(d2)
# print(d3)


d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3={}
for i in d1:
    for j in d2:
        if i==j:
            s=d1[i]+d2[j]
            d3.update({i:s})
b=d3
b.update({"c":300})
b.update({"d":400})
print(b)