anterior = 0
proximo = 0
quero = int(input())

while proximo < quero:
    print(proximo)
    proximo += anterior
    anterior = proximo - anterior
    if(proximo == 0):
        proximo += 1