# Métodos de Optimización Basados en Gradiente

Este repositorio contiene implementaciones de varios métodos de optimización para encontrar los mínimos de la función de Himmelblau. La función de Himmelblau es una función utilizada comúnmente para probar algoritmos de optimización debido a su forma compleja y múltiples mínimos locales.

## Función de Himmelblau

La función de Himmelblau está definida por la siguiente ecuación:

```python
def himmelblau(x):
    return (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2
```
# Métodos de Optimización Implementados
## Método de Búsqueda de Cauchy con Búsqueda Dorada
Este método utiliza el gradiente y una búsqueda unidimensional (búsqueda dorada) para encontrar la dirección de descenso. La búsqueda dorada se usa para encontrar el paso óptimo a lo largo de la dirección del gradiente.

## Pseudocódigo
1. Inicializar x con un valor inicial x0.
2. Mientras no se cumpla el criterio de convergencia:
    - Calcular el gradiente ∇f(x).
    - Definir la dirección de búsqueda d = -∇f(x).
    - Usar la búsqueda dorada para encontrar el paso óptimo α que minimiza f(x + αd).
    - Actualizar x ← x + αd.

## Método de Cauchy con Barzilai-Borwein
En este método, se utiliza una aproximación de Barzilai-Borwein para determinar el tamaño del paso. Esto permite una convergencia más rápida comparada con el método tradicional de Cauchy.

## Pseudocódigo
1. Inicializar x con un valor inicial x0.
2. Calcular el gradiente g0 = ∇f(x0).
3. Inicializar α con un valor pequeño.
4. Mientras no se cumpla el criterio de convergencia:
    - Actualizar x_{k+1} = x_k - α_k g_k.
    - Calcular s_k = x_{k+1} - x_k.
    - Calcular y_k = ∇f(x_{k+1}) - g_k.
    - Actualizar α_{k+1} = (s_k^T y_k) / (y_k^T y_k).
    - Actualizar g_{k+1} = ∇f(x_{k+1}).


## Método del Gradiente Conjugado
El método del gradiente conjugado es un método iterativo para resolver sistemas de ecuaciones lineales grandes y dispersos, que aparecen a menudo en problemas de optimización.

## Pseudocódigo
1. Inicializar x con un valor inicial x0.
2. Calcular el gradiente g0 = ∇f(x0).
3. Establecer la dirección inicial d0 = -g0.
4. Mientras no se cumpla el criterio de convergencia:
    - Calcular el paso óptimo α_k.
    - Actualizar x_{k+1} = x_k + α_k d_k.
    - Calcular el nuevo gradiente g_{k+1} = ∇f(x_{k+1}).
    - Calcular β_k para la nueva dirección.
    - Actualizar d_{k+1} = -g_{k+1} + β_k d_k.

## Método de Newton
El método de Newton utiliza el gradiente y la matriz Hessiana de la función objetivo para encontrar los mínimos. Este método es conocido por su rápida convergencia cuando se encuentra cerca del mínimo.

## Pseudocódigo
1. Inicializar x con un valor inicial x0.
2. Mientras no se cumpla el criterio de convergencia:
    - Calcular el gradiente ∇f(x).
    - Calcular la Hessiana H(x).
    - Calcular la dirección de Newton d = -H(x)^{-1} ∇f(x).
    - Determinar el paso α usando un método de línea de búsqueda.
    - Actualizar x ← x + αd.

## Uso
Cada método tiene su propio archivo Python que contiene la implementación de las funciones necesarias. A continuación se muestra un ejemplo de cómo llamar a uno de los métodos para optimizar la función de Himmelblau:

```python
# Ejemplo de uso del Método de Newton
x0 = [0.0, 0.0]
minimo = newton_method(himmelblau, grad_himmelblau, x0)
print(f"Resultado Método de Newton: {minimo}")
```
Para más detalles sobre cada método, consulte los archivos individuales en este repositorio.

## Requisitos
Python 3.x
Bibliotecas adicionales: numpy, scipy

## Instalación
Puede instalar las bibliotecas necesarias utilizando pip:

```bash
pip install numpy scipy
```