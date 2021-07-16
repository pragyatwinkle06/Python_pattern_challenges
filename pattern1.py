#pattern 1

n=int(input("enter a no"))
s=n
for a in range(n,0,-1):
    for l in range(n,0,-1):
        if (a==s or l==s )and l<=s:
            print(s,end="")
        else:
            print(l,end="")
    for p in range(2,n+1):
        if (a==s or p==s )and p<=s:
            print(s,end="")
        else:
            print(p,end="")
        
        
    s=s-1
        
    print()
s=s+2
for a in range(2,n+1):
    for l in range(n,0,-1):
        if (a==s or l==s )and l<=s:
            print(s,end="")
        else:
            print(l,end="")
    for p in range(2,n+1):
        if (a==s or p==s )and p<=s:
            print(s,end="")
        else:
            print(p,end="")
        
        
    s=s+1
        
    print()