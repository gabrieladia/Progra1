lista = [1,2,3]
valor = [20,60,70]
num = 1
for i in range(len(lista)):
    if num in lista:
        lista.remove(num)
        valor.remove(valor[i])
        
print(lista)
print(valor)