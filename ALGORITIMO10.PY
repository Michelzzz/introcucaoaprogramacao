VETOR = []
LOCAL = []


for i in range(10):
    num = int(input("Digite um número: "))
    VETOR.append(num)


for i in range(len(VETOR)):
    for j in range(i+1, len(VETOR)):
        if VETOR[i] == VETOR[j] and VETOR[i] not in LOCAL:
            LOCAL.append(i)
            LOCAL.append(j)


if len(LOCAL) > 0:
    print("Os números repetidos foram estão nas posições:")
    for pos in LOCAL:
        print(pos)
else:
    print("Não existe números repetidos no vetor.")