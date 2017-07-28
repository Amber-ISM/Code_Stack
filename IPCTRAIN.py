from operator import itemgetter
import heapq
t=int(raw_input())
for i in range(t):
    ND=map(int,raw_input().split())
    N=ND[0]
    D=ND[1]
    l= [[] for x in xrange(D+1)]
    for j in range(N):
        DTS=raw_input().split()
        Di=int(DTS[0])
        Ti=int(DTS[1])
        Si=int(DTS[2])*-1
        l[Di].append([Ti,Si])
    heap=[]
    sum1=0
    for k in range(1,D+1):
        if len(l[k])>0:
            for data in l[k]:
                heapq.heappush(heap,(data[1],data))
        if len(heap)>0:
            z=heapq.heappop(heap)
            if z[1][0]>1:
                heapq.heappush(heap,(z[0],[z[1][0]-1,z[1][1]]))
    for k in heap:
        sum1=sum1+abs(k[1][0]*k[1][1])
    print sum1
 
