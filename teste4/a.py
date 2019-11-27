import sys
import itertools

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()
a = int(a)

alpha="abcdefghijklmnopqrtsvwxyz"

P = 31
M = 2^64
def  Hash(s) :
    x = 0
    for i in range(len(s)):
        x+= ord(s[i]) * P^i
    return(x%M)


# print(b)
# print(Hash(b))
p=2
x=0
while(p<a):
    p*=2
    x+=1
x+=1

g=list(itertools.combinations(alpha,x))
# while(hash(y)==0):
#     combinations(alpha,x)

l=[]
c=b
# f=g[0]
# f=set(f)
# print(f)
# for i in f:
#     print(i)
for i in g:
    k=set(i)
    for j in k:
        c+=j
    #print(c)
    if(hash(c)>0):
        l.append(hash(c))
    c=b

print(min(l))
