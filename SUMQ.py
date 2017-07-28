def binarysearchlessthanequalto(array,target,low,high):
    #print "hii"
    if target<array[low]:
        return -1
    elif target>=array[high]:
        #print "hehe"
        return high
    while low!=high:
        mid=(low+high)/2
        if array[mid]>target:
            high=mid
        else:
            low=mid+1
    return low-1
 
mod=1000000007
t=int(raw_input())
for i in range(t):
    pqr=raw_input().split()
    p=int(pqr[0])
    q=int(pqr[1])
    r=int(pqr[2])
    s1=[]
    s2=[]
    A=sorted(list(map(int,raw_input().split())))
    B=sorted(list(map(int,raw_input().split())))
    C=sorted(list(map(int,raw_input().split())))
    prev1=0
    prev2=0
    for q in A:
        x=(q+prev1)%mod
        s1.append(x)
        prev1=x
    for q in C:
        x=(q+prev2)%mod
        s2.append(x)
        prev2=x
    sum1=0
    for j in B:
        a1=binarysearchlessthanequalto(A,j,0,p-1)
        c=binarysearchlessthanequalto(C,j,0,r-1)
        if a1>=0 and c>=0:
            sum1 += ( ( s1[a1] + ((a1+1)*j) % mod )%mod * ( s2[c] + ((c+1)*j) % mod )%mod )%mod
    print sum1%mod
        
