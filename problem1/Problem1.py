list_numeros = [x for x in range(1, 1000)]
multiplos = []

for list_numero in list_numeros:
    if list_numero % 3 == 0 or list_numero % 5 == 0:
        multiplos.append(list_numero)

print(sum(multiplos))