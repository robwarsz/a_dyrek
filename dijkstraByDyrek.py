import heapq   #kopiec binarny

INF = 2000000000

V, E = map(int, input().split())
dist = [INF] * (V+1)

adj = []

for _ in range(V+1):
    adj.append([])

for _ in range(E):
    a,b,w = map(int, input().split())
    adj[a].append((b,w))    #tuple
    adj[b].append((a,w))

start = 2
dist[start] = 0
li = [ (0,start)]     #(dystans, numerWierzcholka)
heapq.heapify([li])
while li:
    d,u = heapq.heappop(li)      # d,u -> dystans, numerWierzcholka
    for x in adj[u]:
        v,weight = x
        if dist[v] > dist[u]+weight:
            dist[v]=dist[u]+weight
            heapq.heappush(li, (dist[v],v))

print(dist[1:])
print(dist)