import sys


def mcd (b,c):

	while c != 0:
		(b, c) = (c, b % c)
	return (b)

def mdc(i):
    x=mcd(a[0],a[1])
    for y in range(len(a)-1):
        p=y
        u=mcd(a[y],a[y+1])
        while(a[p]%x==0 and p<len(a)-1):
            p+=1
        if(p==len(a) and u>x):
            x=u
    print(x)


a=[]

for i in sys.stdin:
    i=i.strip()
    if(len(i)!=0):
        i=abs(int(i))
        a.append(i)

mdc(a)