l={'1':['a','b'], '2':['c','d']}
for x,y in l.values():
    for x in l["1"]:
        for y in l["2"]:
            print(x+y)