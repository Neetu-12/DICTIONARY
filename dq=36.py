a={'key1': 1, 'key2': 3, 'key3': 2}
b={'key1': 1, 'key2': 2}
for i in a:
    for j in b:
        if i==j:
            if a[i]==b[j]:
                print(i,":",a[i],"is present in both")
            else:
                pass