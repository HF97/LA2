import sys


def primos(x):
	y=2
	while (y<=x):
		if (x%y==0):
			print (y)
			x=int(x/y)
		else: 
			y+=1

def prime(x):
    p=2
    if(x==0 or x==1):
        return False
    while(p<x):
        if(x%p==0):
            
            return False
        else:
            p+=1
    return True

def func(a):
    b=a[0]
    c=a[1]
    x=0
    # print(b)
    # print(c)
    if('?'not in b and '?' not in c):
        if(prime(int(b)+int(c))):
            return(x+1)
        else:
            return(x)
    
    if('?' not in b):
        for y in range(10):
            g=c
            k=''
            for e in g:
                if(e=='?'):
                    #print(e)
                    k+=str(y)
                else:
                    k+=e
            if(prime(int(b)+int(k))):
                x+=1
        return (x)
    if('?' not in c):
        for y in range(10):
            g=b
            k=''
            for e in g:
                if(e=='?'):
                    #print(e)
                    k+=str(y)
                else:
                    k+=e
            if(prime(int(c)+int(k))):
                x+=1
        return (x)
    for i in range(10):
        f=b
        o=''
        for j in f:
            if(j=='?'):
                o+=str(i)
            else:
                o+=j
        for y in range(10):
            g=c
            k=''
            for e in g:
                if(e=='?'):
                    #print(e)
                    k+=str(y)
                else:
                    k+=e
            # print(o+' '+k)
            #print(prime(int(o)+int(k)))
            if(prime(int(o)+int(k))):
                x+=1
    return(x)








a=sys.stdin.readline()
a=a.split()


print(func(a))