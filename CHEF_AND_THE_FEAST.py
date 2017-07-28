def binarysearchlessthanequalto(array,target,low,high):
    if target<array[low]:
        return -2
    elif target>=array[high]:
        return high
    while low!=high:
        mid=(low+high)/2
        if array[mid]>target:
            high=mid
        else:
            low=mid+1
    return low-1
 
t=int(raw_input())
for i in range(t):
    s=0
    N=int(raw_input())
    A=sorted(list(map(int,raw_input().split())))
    q=binarysearchlessthanequalto(A,-1,0,N-1)+1
    if q<N and q>=0:
        for j in range(q,N):
            s=s+A[j]
        temp=s*(N-q)
        newtemp=temp
        r=q-1
        while r>=0:
            s=s+A[r]
            newtemp=s*(N-r)
            if newtemp>=temp:
                temp=newtemp
                r=r-1
            else:
                break
        if r>=0:
            for j in range(0,r+1):
                temp=temp+A[j]
    elif q<0:
        for j in range(0,N):
            s=s+A[j]
        temp=s*N
    else:
        for j in range(0,N):
            s=s+A[j]
            temp=s
        
    print temp
 
