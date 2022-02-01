n = int(input())

if n == 2:
    print(f'{n} casas brancas e {n} casas pretas')
elif n % 2 == 0:
    x = n**2
    y = x//2
    print(f'{y} casas brancas e {y} casas pretas')
elif n % 2 == 1:
    x = n**2
    y = x//2
    print(f'{y+1} casas brancas e {y} casas pretas')
    
