# m = {
#     'data1':100,
#     'data2': -54,
#     'data3': 247
#     }
# i=0
# s=0
# while i<len(m):
#     a=m["data1"]
#     s=s+a
#     i=i+1
# print(s)


# from typing_extensions import IntVar


# m = {
#     'data1':100,
#     'data2': -54,
#     'data3': 247
#     }
# n={"data1":100}+{"data3":247}
# p={"data2":-54}
# # s={"data1":100,+"data3":247}-"data2"-54
# # print(n-p)

# n={101:"neetu",201:"suraj",301:"baby"}
# for i in n:
#     print(i,"-",n[i])


dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
dic4={}
for i in dic2:
    if i in dic1:
        dic2[i]=dic2[i]+dic1[i]
    dic4={**dic1,**dic2,**dic3}
print(dic4)




m = {
    'data1':100,
    'data2': -54,
    'data3': 247
    } 
s=0
for i in m:
    s=s+m[i]
print(s)
