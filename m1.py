#Q-1
dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
dic4={}
for i in dic2:
    if i in dic1:
        dic2[i]=dic2[i]+dic1[i]
    dic4={**dic1,**dic2,**dic3}
print(dic4)


#Q-2
m = {
    'data1':100,
    'data2': -54,
    'data3': 247
    } 
s=0
for i in m:
    s=s+m[i]
print(s)
