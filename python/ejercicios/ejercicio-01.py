numero = []

def analizar(numeros):
    if not numeros:
        raise ValueError("La lista no puede estar vacía")
    return {
        "total": len(numeros),       # cantidad de números
        "suma": sum(numeros),        # suma de todos
        "maximo": max(numeros),      # el más grande
        "minimo": min(numeros),      # el más pequeño
        "promedio": sum(numeros)/len(numeros)    # suma / total
    }

resultado = analizar(numero)
print(resultado) 