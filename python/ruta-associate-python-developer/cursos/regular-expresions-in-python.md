
## 1. Conceptos básicos de manipulación de cadenas:

---
### 1.1 Introducción a la manipulación de cadenas:

Ya que las cadenas son tipos de datos iterables estos incluyen el uso de ciertas funciones para determinadas cosas, por ejemplo:

- `str()`: permite convertir otros tipos de datos a String como pueden ser números
- `len()`: permite saber la longitud del String - `len('Hola')` dará como resultado = 4

Para acceder a determinado carácter en una cadena podemos usar `my_string[n]` siendo `n` la posición del carácter menos uno, ya que en Python se empieza desde 0. Y para acceder a un determinado rango usamos `my_string[0:3]` que en este ejemplo irá desde el carácter de posición 0 hasta el carácter de posición 2 que seria en el 3ro, es decir la expresión se detiene un carácter antes del indicado como ultimo valor.

Si queremos acceder a ciertos caracteres podemos hacer uso de `my_string[0:6:2]` que ira desde el 0 hasta el valor anterior a 6 pero de 2 en 2, es decir que imprimirá `0, 2, 4`

>[!note] Nota:
>Si queremos imprimir una cadena de forma invertida podemos hacerlo con: `my_string[::-1]`

---
### 1.2 Operaciones con cadenas:

En caso de que necesitemos llevar toda una misma cadena a un solo tipo de formato (mayúsculas/minúsculas) podemos hacerlo con:

- `string.lower()`: convierte todos los caracteres a minúsculas
- `string.upper()`: convierte todos los caracteres a mayúsculas
- `string.capitalize()`: convertirá todo el texto a minúsculas a excepción de la primera letra que se convertirá en mayúscula

Para operar las cadenas y por ejemplo poder dividir sus datos (palabras) en listas podemos hacer uso de:

- `string.split(sep=' ', maxsplit=2)` siendo `sep` lo que será el separador y siendo `maxsplit` la cantidad de separaciones que queramos
- `string.rsplit(sep=' ')` en este caso hace lo mismo solo que a diferencia de `split` que inicia de izquierda a derecha, `rsplit` inicia de derecha a izquierda. Psdt: como podemos ver `maxsplit` no es un argumento obligatorio, en caso de colocarse lo que la función hará es dividir en la máxima cantidad posible
- `string.splitlines()`: separa el String teniendo como separador los saltos de línea que en Python se escriben en medio del String con `\n`
- `sep.join(iterable)`: lo que hace es que concatena un iterable uniendo todos los String con el `sep` que le pasemos
- `string.strip()`: eliminara los caracteres que le especifiquemos, en caso de no hacerlo eliminara los espacios al inicio y al final del String. Existen también:
	- `rstrip()`: elimina el espacio en blanco a la derecha 
	- `lstrip()`: elimina el espacio en blanco a la izquierda

---
### 1.3 Buscar y remplazar:

Para buscar y remplazar en las cadenas disponemos de los siguiente métodos:

- `string.find(subtring, start, end)`: busca la `substring` y es el parámetro obligatorio, para `start` y `end` son parámetros opcionales y se indican en caso en que queramos busca nuestro `substring` entre determinado rango de caracteres. En caso de no encontrar el `substring` va a retornar como valor el `-1`
- `string.index(subtring, start, end)`: tiene el mismo formato pero a diferencia de `find`, este si nos retorna un error en caso de no encontrar el `substring`, se puede manejar perfectamente con `try - exception`
- `string.count(subtring, start, end)`: los parámetros son los mismos pero esta función nos permite contar cuantas veces sale el `substring` en el String completo
- `string.replace(old, new, count)`: esta función nos permite remplazar en el String, los parámetros inician siendo la cadena a remplazar, el nuevo texto y `count` es un parámetro opcional que nos elije marcar cuantas veces se desea remplazar de izquierda a derecha

---
### 1.4 Formato posicional:

