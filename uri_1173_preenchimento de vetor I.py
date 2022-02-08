a = 10*[0]
x = int(input())

for i in range(10):
    a[i] = x
    x *= 2
    print(f'N[{i}] = {a[i]}')
