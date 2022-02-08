x = int(input())
y = int(input())
while y <= x:
    y = int(input())
cont = 0
soma = 0
while soma < y:
    soma += x
    x += 1
    cont += 1
print(cont)
