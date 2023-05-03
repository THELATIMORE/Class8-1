def sumar_5_enteros():
    lista = []
    contadorWhile = 0
    tamano = 5
    suma = 0

    while contadorWhile < tamano:
        lista.append(int(input("ingrese numero" + str(contadorWhile+1) + ": ")))
        contadorWhile +=1

    contadorWhile = 0
    while contadorWhile < tamano:
        suma += lista[contadorWhile]
        contadorWhile +=1


    print("los elementos de la lista son: ")
    for numero in lista:
        print(numero, end=', ')


    print("\nla suma de todos los elementos es: ")
    print(suma)