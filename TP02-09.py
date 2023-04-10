"""Intercalar  los  elementos  de  una  lista  entre  los  elementos  de  otra.
La  intercalacióndeberá  realizarse  exclusivamente mediante la técnica de rebanadas
y no se crearáuna lista nueva sino que se modificará la primera.
Por ejemplo, si lista1 = [8, 1, 3] y lista2 = [5, 9, 7], lista1 deberá quedar como [8, 5, 1, 9, 3, 7]."""

lista1 = [1,2,3]
lista2 = [6,9,12,65,99,89]

if len(lista1) > len(lista2) :
    mainLista = lista1
    secLista = lista2
else:
    mainLista = lista2
    secLista = lista1
 
print(mainLista)

for i in range(len(secLista)):
    mainLista[2*i+1:2*i+1] = [secLista[i]] #La vuelve lista para poder agregar el elemento en dicha posicion
    
print(mainLista)