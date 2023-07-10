from os import system
system("cls")

import numpy as np

while True:
    print("Menu de opciones entradas: ")
    print("1. Comprar entradas")
    print("2. Mostrar ubicaciones disponibles")
    print("3. Ver listado de asistentes")
    print("4. Mostrar ganancias totales")
    print("5. Salir")
    opcion = input("Ingrese su seleccion: ")
    
    if opcion == '1':
        cant_entradas = input("Elija la cantidad de entradas que desea (1 - 3): ")
        arr = [[1 for j in range (10)] for i in range (10)]
        num = 1 
        for i in range (10):
            for j in range(10):
                arr[i][j] = num
                num += 1
                
        for i in range (10):
            for j in range (10):
                print(arr[i][j], end="\t")
            print()
    pos = input(f"Ingrese sus asientos a eleccion segun su cantidad de entradas '{cant_entradas}' : ")
    row, col = map(int, pos.split(","))
    if arr [row][col] != "X":
        arr [row][col] = "X"
        print("Su asiento elegido es:", pos, "Y ha sido reservado ")
    else:
        print("Asiento no disponible", pos," Seleccione otro porfavor")
        
        