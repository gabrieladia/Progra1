"""Resolver el siguiente problema, utilizando funciones:
Se desea llevar un registro de los socios que visitan un club cada día. Para ello, se ingresa el número de socio de cinco
dígitos hasta ingresar un cero como fin de carga.
Se solicita:
a. Informar para cada socio, cuántas veces ingresó al club (cada socio debe aparecer una sola vez en el informe).
b. Solicitar un número de socio que se dio de baja del club y eliminar todos sus ingresos. Mostrar los registros de
entrada al club antes y después de eliminarlo. Informar cuántos ingresos se eliminaron."""

def vecesIngreso(socios):
    socioNoRepetidos = []
    listaDeVeces = []
    contDeVecesBorrado = 0
    for socio in socios:
        
        if socio not in socioNoRepetidos:
            
            socioNoRepetidos.append(socio)
            cantidad = socios.count(socio)
            listaDeVeces.append(cantidad)
            print("El socio numero: ",socio, "salio: ",cantidad," veces." )

    return socioNoRepetidos , listaDeVeces

def bajaDeSocio(socioBuscado,socioNoRepetidos,listaDeVeces,cont):
    
    for i, socio in enumerate(socioNoRepetidos):
        
        if socioBuscado == socio:
            socioNoRepetidos.remove(socio)
            listaDeVeces.remove(valor[i])
            
    cont = cont + 1
    
    return socioNoRepetidos , listaDeVeces ,cont
    
listaDeSocios = []

while True:
    numeroDeSocio = int(input("Ingrese el numero de socio: "))
    
    if numeroDeSocio == 0:
        break
    
    while numeroDeSocio < 0 or numeroDeSocio > 99999:
        numeroDeSocio = int(input("Ingrese el numero de socio valido: "))
        
    listaDeSocios.append(numeroDeSocio)
    
socioNoRepetidos ,  listaDeVeces = vecesIngreso(listaDeSocios)

