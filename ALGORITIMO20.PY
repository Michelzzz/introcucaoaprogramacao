numeros = []

for i in range(20):
    num = int(input(f"{i} número: "))
    numeros.append(num)

print("Os números lidos em ordem inversa são:")
for i in range(19, -1, -1):
    print(numeros[i])