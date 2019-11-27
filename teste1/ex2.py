import sys

b={}
c={}
d={}

y=0

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

print(s)

e={}
for i in s:
    a=[]
    for key,value in c.items():
        if(value == i):
            a.append(key)
    a=sorted(a)
    a=a[::-1]
    l=[]
    for p in a:
        l.append(b[p])
    l=sorted(l)
    q=0
    f=[]
    for key,value in b.items():
        if(l[q]==value):
            f.append(l[0])
        if(q<len(l)-1):
            q+=1
    print(f)
