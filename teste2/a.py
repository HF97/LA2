import sys

def adj(mapa, v):
    """ devolve a lista de adjacentes de v (dest e custo)"""
    adjs = [(v[0]-1,v[1]), (v[0],v[1]+1), (v[0]+1,v[1]), (v[0],v[1]-1)]
    res = []
    for (x,y) in adjs:
        if x>=0 and x < len(mapa) and y>=0 and y<len(mapa[x]):
            if mapa[x][y]==' ':
                res.append(((x,y),1))
    return res

def dijkstra(mapa,o):
	queue = []
	dist = {}
	dist[o] = 0
	queue.append(o)
	while queue:
		u = min(queue,key=lambda x : dist[x])
		queue.remove(u)
		for (v,w) in adj(mapa,u):
			alt = dist[u] + w
			if v in dist:
				dist[v] = alt
			else:
				dist[v]  = alt
				queue.append(v)
	return dist

txt = sys.stdin.readlines()
l,c = txt[0].split()
l = int(l)
c = int(c)
mapa = txt[1:]
dist = dijkstra(mapa,(0,0))
print(dist[(l-1,c-1)])