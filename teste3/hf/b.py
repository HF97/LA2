import sys


a = int(sys.stdin.readline())
if(a==0):
    print(0)

lista = []
for i in range(1, 22):
    lista.append(i*i*i)

def novafunc(a,l):
    x=1
    b={}
    while(x<len(l)+1):
        while



def moedas (a, l):
    i=0
    nova = []
    while(i<len(l)):
        if l[i]<a:
            nova.append(l[i])
        i+=1
    return (novafunc(a,nova))

moedas(a,lista)

