import sys
from heapq import heappush, heappop
def dijkstra(al, source):
    dist = [-42] * len(al)
    dist[source] = 0
    heap = []
    for d, w in al[source]:
        heappush(heap, (w, d))
    num = 1
    while num != len(al):
        while len(heap) and dist[heap[0][1]] >= 0:
            heappop(heap)
        if len(heap):
            w, d = heappop(heap)
            dist[d] = w
            num += 1
            for d1, w1 in al[d]:
                if dist[d1] < 0:
                    heappush(heap, (dist[d] + w1, d1))
        else:
            break
    return dist
def main():
    for c in range(int(raw_input().strip())):
        n,k,x,m,s = map(int,raw_input().strip().split())
        al = [[] for i in range(n)]
        al1=[[] for i in range(n)]
        for i in range(m):
            s1,d,w = map(int,raw_input().strip().split())
            al[s1 - 1].append((d - 1, w))
            al[d - 1].append((s1 - 1, w))
            if s1<=k:
                s1=1
            elif d<=k:
                d=1
            al1[s1-1].append((d-1,w))
            al1[d-1].append((s1-1,w))
        cliqued_dist=dijkstra(al1,0) 
        sd = dijkstra(al, s-1)
        for i in range(n):
            if s<=k and i<k:
                if (sd[i]<0 and i!=s-1) or (sd[i]>x and i!=s-1):
                    sd[i]=x
                elif i==s-1:
                    sd[i]=0
            elif s<=k and i>=k:
                y=cliqued_dist[i]+x
                if s-1==i:
                    sd[i]=0
                elif y<sd[i] or sd[i]<0:
                    sd[i]=y
            elif s>k and i<k:
                y=cliqued_dist[s-1]
                if (sd[i]<0) or (sd[i]>y+x):
                    sd[i]=y+x
            elif s>k and i>=k:
                if i==s-1:
                    sd[i]=0
                else:
                    y1=cliqued_dist[s-1]
                    y2=cliqued_dist[i]
                    if y1+y2+x<sd[i] or sd[i]<0:
                        sd[i]=y1+y2+x
        for i in sd:
            print i,
        print       
            
    
main() 