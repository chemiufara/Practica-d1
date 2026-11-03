"""Gestiona notas mediante un menú de opciones.

El programa permite introducir notas, consultar cuántas se han introducido,
calcular su media y mostrar la nota máxima y mínima.

Módulo 0485 Programación · UD 3
Autor: Jose María Mas Chicharro
Fecha: 03/11/2026
"""

# Inicialización de los patrones
cantidad = 0
suma = 0
nota_maxima = None
nota_minima = None


# Menú principal
while True:
    print("\n--- MENÚ DE NOTAS ---")
    print("1. Introducir una nota")
    print("2. Ver número de notas introducidas")
    print("3. Ver la media")
    print("4. Ver nota más alta y más baja")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    # Opción 1: introducir y validar una nota
    if opcion == "1":
        nota = float(input("Introduce una nota entre 0 y 10: "))

        if 0 <= nota <= 10:
            cantidad += 1
            suma += nota

            # Inicialización y actualización de los extremos
            if nota_maxima is None:
                nota_maxima = nota
                nota_minima = nota
            else:
                if nota > nota_maxima:
                    nota_maxima = nota

                if nota < nota_minima:
                    nota_minima = nota

            print("Nota guardada correctamente.")

        else:
            print("Error: la nota debe estar entre 0 y 10.")

    # Opción 2: mostrar el contador
    elif opcion == "2":
        print("Se han introducido", cantidad, "notas.")

    # Opción 3: calcular y mostrar la media
    elif opcion == "3":
        if cantidad > 0:
            media = suma / cantidad
            print(f"La media de las notas es: {media:.2f}")
        else:
            print("No se puede calcular la media porque no hay notas.")

    # Opción 4: mostrar los extremos
    elif opcion == "4":
        if cantidad > 0:
            print(f"Nota más alta: {nota_maxima:.2f}")
            print(f"Nota más baja: {nota_minima:.2f}")
        else:
            print("No se han introducido notas.")

    # Opción 5: finalizar
    elif opcion == "5":
        print("Programa finalizado.")
        break

    # Control de opciones incorrectas
    else:
        print("Error: opción no válida.")