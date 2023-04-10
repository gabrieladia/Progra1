socios = [1,11,1]
socioNoRepetidos =[]
for socio in socios:
    if socio not in socioNoRepetidos:
        socioNoRepetidos.append(socio)
        cantidad = socios.count(socio)
        print("El socio numero: ",socio, "salio: ",cantidad," veces." )

print(list(range(101,201,2)))