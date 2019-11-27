import sys
b={} #contactos
c={} #lista chamadas
d={} 

y=0 #ver se é -

for a in sys.stdin:
    string=""
    a=a.split()
    if(len(a)!=0):
        p=1
        if(a[0]=="-"):
            y=1
        if(y==0):
            while(p<len(a)):
                string+=a[p]+" "
                b[a[0]]=string
                p+=1
                c[a[0]]=0
        if(y==1 and a[0]!="-"):
            if(a[0] not in c):
                c[a[0]]=1
            else:
                c[a[0]]+=1


s=sorted(set(c.values()))
s=s[::-1]

e={}

for i in s:
    a=[]
    for key,value in c.items():
        if(value == i):
            a.append(key)
        if(len(a)==1):
            e[i]=a







for key, value in b.items():
    for i in e.values():
        x=[]
        for k in range(len(i)):
            if(i[k]==key):
                i[k]=value
                # print(k)




for i in e.values():
    i.sort()




for key,value in e.items():
    for i in value:
        if(key!=0):
            print(str(key)+" "+i)