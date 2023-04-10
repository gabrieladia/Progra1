"""Escribir una función que reciba una lista de números enteros como parámetro y la normalice, es decir que todos sus
elementos deben sumar 1.0, respetando las proporcionesrelativas que cada elemento tiene en la lista original. Desarrollar
también un programa que permita verificar el comportamiento de la función. Por ejemplo, normalizar([1, 1, 2]) debe
devolver [0.25, 0.25, 0.50].
"""
def normalizar(numeros):
    
    total = 0
    
    for num in numeros:
        total = total + num
    
    for i , numero in enumerate(numeros):
        numeros[i] =  numero / total
    
    return numeros
    
    
lista = [1,1,2]

print(normalizar(lista))
    

    
    