import sys

def parse(adj,o,d, w,a):
	if o not in adj and o not in a:
		adj[o] = []
	if d not in adj and d not in a:
		adj[d] = []
	if o == d and o in adj and d in adj:
		adj[o].append((d,w))
	else:
		if o in adj:
			adj[o].append((d,w))
		if d in adj:
			adj[d].append((o,w))
	return adj

def parse2(adj,o,d, w):
	if o not in adj:
		adj[o] = []
	if d not in adj:
		adj[d] = []
	if o == d:
		adj[o].append((d,w))
	else:
		adj[o].append((d,w))
		adj[d].append((o,w))
	return adj

def dijkstra(adj,o):
	queue = []
	parent = {}
	dist = {}
	for v in adj:
		dist[v] = float('inf')
		queue.append(v)
	dist[o] = 0
	while queue:
		u = min(queue,key=lambda x : dist[x])
		queue.remove(u)
		for (v,w) in adj[u]:
			alt = dist[u] + w
			if alt < dist[v]:
				dist[v] = alt
				parent[v] = u
	return parent,dist









adj={}
adj2={}


a=sys.stdin.readline()
a=a.strip().split(',')



for i in sys.stdin:
	i=i.strip().split(',')
	g=i[0]
	h,j=i[1].split(':')
	adj=parse(adj,g,h,int(j),a)

p=9999999999999999
final=[]
for x in a:
	l,k=dijkstra(adj,x)
	t=0
	final.append(k)



final2=[]

for i in range(len(final)):
	final3=[]
	asdf=list(final[i].values())
	final2.append(asdf)


asd=0
panados=[]
lol=999999999999
bananas=final2[0]
for i in range(len(bananas)):
	cenas=0
	res=0
	while(res<len(final2)):
		cenas+=final2[res][i]
		res+=1
	if(cenas<lol):
		lol=cenas
		p=i


for i in range(len(final2)):
	panados.append(final2[i][p])
print(max(panados))
