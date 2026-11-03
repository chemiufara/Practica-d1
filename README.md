# Práctica D1 - Menú de opciones con patrones

## Descripción

Este programa permite gestionar una serie de notas mediante un menú que se repite hasta que el usuario decide salir.

Las opciones disponibles son:

1. Introducir una nota.
2. Ver el número de notas introducidas.
3. Ver la media de las notas.
4. Ver la nota más alta y la más baja.
5. Salir del programa.

## Funcionamiento

El programa utiliza un bucle `while` para mantener activo el menú y una estructura `if / elif / else` para gestionar las distintas opciones.

Cada vez que se introduce una nota válida se actualizan los siguientes datos:

- Un contador con el número de notas introducidas.
- Un acumulador con la suma de todas las notas.
- La nota máxima.
- La nota mínima.

Las notas deben estar comprendidas entre 0 y 10. Si se introduce una nota fuera de este intervalo, el programa muestra un mensaje de error y no la guarda.

También se comprueba que exista al menos una nota antes de calcular la media o mostrar la nota máxima y mínima.

## Patrones utilizados

### Contador

La variable `cantidad` comienza en 0 y aumenta en una unidad cada vez que se introduce una nota válida.

```python
cantidad += 1
```

### Acumulador

La variable `suma` almacena la suma de todas las notas introducidas.

```python
suma += nota
```

### Máximo y mínimo

Las variables `nota_maxima` y `nota_minima` permiten conservar los valores más alto y más bajo introducidos.

La primera nota válida se utiliza para inicializar ambos extremos y las siguientes se comparan con ellos.

## Validación de las notas

Solo se aceptan notas comprendidas entre 0 y 10:

```python
if 0 <= nota <= 10:
```

Si la nota no cumple esta condición, se muestra un mensaje de error.

## Pruebas realizadas

Se han realizado diferentes pruebas para comprobar el funcionamiento del programa:

| Prueba | Resultado esperado |
|---|---|
| Consultar la media sin introducir notas | Muestra un aviso |
| Introducir una nota de 7 | La nota se guarda correctamente |
| Introducir una nota de 12 | Muestra un error |
| Introducir 5, 8 y 7 | Se contabilizan 3 notas |
| Consultar la media de 5, 8 y 7 | Muestra 6.67 |
| Consultar los extremos de 5, 8 y 7 | Máxima 8 y mínima 5 |
| Introducir 0 | Se acepta como nota válida |
| Introducir 10 | Se acepta como nota válida |
| Introducir una opción incorrecta | Muestra un mensaje de error |
| Seleccionar la opción 5 | Finaliza el programa |

## Documentación

El programa incluye un `docstring` inicial que explica su finalidad y comentarios que dividen el código en bloques para facilitar su lectura.

También se han seguido las principales convenciones de PEP 8, como el uso de nombres descriptivos en `snake_case`, una indentación de cuatro espacios y espacios alrededor de los operadores.

## Archivos

- `menu_notas.py`: contiene el código del programa.
- `README.md`: contiene la descripción y documentación de la práctica.

## Autor

Jose María Mas Chicharros