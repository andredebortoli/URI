x = int(input())
a,b,c,d,e = map(int, input().split())
cont = 0
lista = []

lista.append(a)
lista.append(b)
lista.append(c)
lista.append(d)
lista.append(e)

for item in lista:
    if item == x:
        cont += 1
print(cont)



