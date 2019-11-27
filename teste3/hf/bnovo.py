import sys

def moedas(l, tam, b):
    listalista = [[0 for x in range(tam)] for x in range(b+1)]
    for i in range(tam):
        listalista[0][i] = 1
    for i in range(1, b+1):
        for j in range(tam):
            x = listalista[i-l[j]][j] if i-l[j] >= 0 else 0
            y = listalista[i][j-1] if j >= 1 else 0
            listalista[i][j] = x+y
    return listalista[b][tam-1]

a = sys.stdin.readline()
b = int(a)
e = 15

lista = []
for i in range(1, 22):
    lista.append(i*i*i)
c = moedas(lista, len(lista), e)
print(lista)
print(c)
