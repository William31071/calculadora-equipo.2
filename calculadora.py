# Responsable: Hugo Peralta Galván
def obtener_numeros():
    numeros = []
    for orden in ("primer", "segundo"):
        while True:
            texto = input(f"Ingresa el {orden} número: ").strip()
            try:
                # Los enteros se convierten con int porque float pierde dígitos
                # a partir de 2**53.
                numero = int(texto) if texto.lstrip("+-").isdigit() else float(texto)
                # float también acepta "nan" e "inf", que no sirven para operar.
                if not abs(numero) < float("inf"):
                    raise ValueError
            except ValueError:
                print("Entrada no válida. Escribe un número, por ejemplo 7 o -2.5.")
                continue
            numeros.append(numero)
            break
    return tuple(numeros)


# Responsable: Hugo Peralta Galván
def sumar(a, b):
    return a + b


# Responsable: Hugo Peralta Galván
def restar(a, b):
    raise NotImplementedError


# Responsable: Diego Uriel Valerio Mora
def multiplicar(a, b):
    raise NotImplementedError


# Responsable: Diego Uriel Valerio Mora
def dividir(a, b):
    raise NotImplementedError


# Responsable: William de Jesús Carmona Chi
def mostrar_resultado(operacion, a, b, resultado):
    raise NotImplementedError


# Responsable: por definir
def main():
    raise NotImplementedError


if __name__ == "__main__":
    main()
