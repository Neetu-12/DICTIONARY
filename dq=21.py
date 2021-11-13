a=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
r=[]
for i in range(len(a)):
    for j in a[i]:
        if a[i][j] not in r:
            r.append(a[i][j])
print(set(r))