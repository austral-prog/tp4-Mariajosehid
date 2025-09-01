import math

def line():
    # Entrada de datos
    A = float(input("Ingrese el coeficiente A: "))
    B = float(input("Ingrese el coeficiente B: "))
    X1 = float(input("Ingrese el coeficiente X1: "))
    X2 = float(input("Ingrese el coeficiente X2: "))

    # Calcular Y1 y Y2
    Y1 = A * X1 + B
    Y2 = A * X2 + B

    # Calcular distancia entre puntos
    distancia = math.sqrt((X2 - X1)**2 + (Y2 - Y1)**2)

    # Guardar resultados en lista (no solo imprimir)
    results = [
        f"El coeficiente A de su ecuación de la recta es: {A}",
        f"El coeficiente B de su ecuación de la recta es: {B}",
        f"El coeficiente X1 de su ecuación de la recta es: {X1}",
        f"El coeficiente X2 de su ecuación de la recta es: {X2}",
        f"Para la siguiente ecuación:",
        f"\tY = {A}X + {B}",
        f"Dados los siguientes puntos:",
        f"\tP1 ({X1}, {Y1})",
        f"\tP2 ({X2}, {Y2})",
        f"La distancia entre ellos es: {distancia}"
    ]

    # Imprimir si se ejecuta manualmente
    if __name__ == "__main__":
        for line in results:
            print(line)

    # Retornar lista para los tests
    return results


# Ejecutar como script
if __name__ == "__main__":
    line()
