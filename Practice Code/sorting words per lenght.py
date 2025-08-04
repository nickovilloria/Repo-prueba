lista_inicial = ["C#","Python","Javascript"]
cuantos = []
for item in lista_inicial:
    cuantos.append(len(item))
cuantos.sort(reverse=True)
mayor=cuantos[0]
lista_inicial.sort(key=len, reverse=True)
mas_larga=lista_inicial[0]
print(f'La cadena más larga es {mas_larga} con {mayor} caracteres')