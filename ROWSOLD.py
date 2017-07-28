t=int(raw_input())
for k in range(t):
    c=0
    n1=raw_input()
    n=list(n1)
    n=map(int,n)
    l=len(n)
    L1=list()
    for i in n:
        if i==0:
            c=c+1
        else:
            break
    x=1
    count=0
    #print "c=",c
    for i in range(c,l):
        if n[i]==x:
            count=count+1
        if n[i]!=x:
            x=n[i]
            L1.append(count)
            count=1
        if i==l-1:
            L1.append(count)
    #print "L1=",L1
    l1=len(L1)
    cost=0
    #print l1
    if l1%2==1:
        L1=L1[:-1]
        l1=l1-1
    if l1>1:
        for i in range(0,l1-2,2):
            cost=cost+L1[i]+(L1[i]*L1[i+1])
            L1[i+2]=L1[i+2]+L1[i]
    
        cost=cost+L1[l1-2]+(L1[l1-2]*L1[l1-1])
    else:
        cost=0
    print cost