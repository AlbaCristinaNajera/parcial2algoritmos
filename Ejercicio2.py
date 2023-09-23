import sys

notas = [float(nota) for nota in sys.argv[1].split(",")]

def calcular_suma():
    suma = sum(notas)
    return suma  

def calcular_promedio():
    suma = calcular_suma()  
    promedio = suma / len(notas)
    return promedio

suma_resultado = calcular_suma()
promedio_resultado = calcular_promedio()

print("Resultado:")
print("La suma de los datos es:", suma_resultado)
print("El promedio de los datos es:", promedio_resultado)
