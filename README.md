# Python-Package
# Métodos de Optimización

Este repositorio contiene implementaciones en Python de varios métodos de optimización para encontrar mínimos y máximos de funciones. Los métodos implementados hasta ahora son:

## 1. Método de la Secante

El método de la secante es un algoritmo numérico para encontrar raíces de una función no lineal. A diferencia del método de Newton-Raphson, el método de la secante no requiere el cálculo de la derivada de la función. En su lugar, utiliza una aproximación de la derivada basada en dos puntos cercanos en la función.

## 2. Método de Bisección

El método de bisección es un algoritmo simple pero efectivo para encontrar raíces de una función continua en un intervalo dado. Divide repetidamente el intervalo por la mitad y selecciona el subintervalo que contiene la raíz, hasta alcanzar una precisión especificada.

## 3. Método de Newton-Raphson

El método de Newton-Raphson es un método iterativo para encontrar raíces de una función real. Utiliza la idea de la tangente a la curva de la función para encontrar iterativamente una mejor aproximación de la raíz.

## 4. Programación de Búsqueda Exhaustiva

La búsqueda exhaustiva, también conocida como fuerza bruta, es un método simple de optimización que evalúa sistemáticamente todas las posibles soluciones en un rango dado para encontrar el óptimo global.

## 5. Programación del Método de Fase de Delimitación

El método de fase de delimitación es una estrategia de búsqueda que divide repetidamente el intervalo de búsqueda en subintervalos más pequeños, evaluando la función objetivo en puntos estratégicos dentro de cada subintervalo para determinar la dirección de búsqueda y reducir el intervalo.

## 6. Programación del Método de Intervalo a la Mitad

El método de intervalo a la mitad es un algoritmo simple para encontrar el mínimo o máximo de una función en un intervalo dado. Divide repetidamente el intervalo por la mitad y selecciona el subintervalo que contiene el mínimo o máximo, hasta alcanzar una precisión especificada.

## 7. Programación del Método de Búsqueda de Fibonacci

El método de búsqueda de Fibonacci es un algoritmo de optimización que utiliza la secuencia de Fibonacci para encontrar el mínimo o máximo de una función en un intervalo dado. A diferencia de la búsqueda binaria, este método no requiere derivadas y puede ser útil cuando las derivadas no están disponibles o son difíciles de calcular.

## 8. Programación del Método de Búsqueda de la Sección Dorada

El método de búsqueda de la sección dorada es un algoritmo de optimización que divide iterativamente un intervalo en proporciones áureas y selecciona subintervalos basados en comparaciones de valores de función para encontrar el mínimo o máximo de una función en el intervalo dado.

## Funciones Implementadas

Se proporcionan implementaciones para las siguientes funciones de ejemplo:

- **f1(x) = x^2 + 54/x**
- **f2(x) = x^3 + 2x - 3**
- **f3(x) = x^4 + x^2 - 33**
- **f4(x) = 3x^4 - 8x^3 - 6x^2 + 12x**
- **V(L) = 200 * L - 60 * L^2 + 4 * L^3** (Función de Volumen)
- **lata_funcion(x) = 2 * pi * x^2 + (500 / x)** (Función para calcular el área de superficie de una lata)

## Uso

Cada método de optimización se implementa en una clase separada con un método `search` que toma la precisión como argumento y devuelve una lista de las aproximaciones sucesivas de la raíz o del mínimo/máximo de la función.

## Requisitos

- Python 3.x
- NumPy
- Matplotlib (solo para los ejemplos de visualización)
