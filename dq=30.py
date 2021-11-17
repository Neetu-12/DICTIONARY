a={'S  001': ['Math', 'Science'], 'S  002': ['Math', 'English']}
dic={}
for i in a:
    st=""
    for j in i:
        if j!=" ":
            st+=j
    dic[st]=a[i]
print(dic)
    