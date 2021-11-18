a={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
r={}
for i in a:
    if a[i]>170:
        r.update({i:a[i]})
print(r)
