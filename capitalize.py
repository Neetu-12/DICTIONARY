def solve(s):
    i=0
    while i<len(s):
        a=s[i].capitalize()
        print(a,end=" ")
        i+=1
solve(input("").split(" "))