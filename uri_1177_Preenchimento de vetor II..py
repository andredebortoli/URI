a = int(input())
b = []

for i in range(1000):
    j = 0
    while j < a:
        b.append(j)
        j += 1
    print(f'N[{i}] = {b[i]}')
