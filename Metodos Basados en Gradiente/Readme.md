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

## Método de Cauchy con Barzilai-Borwein
En este método, se utiliza una aproximación de Barzilai-Borwein para determinar el tamaño del paso. Esto permite una convergencia más rápida comparada con el método tradicional de Cauchy.

## Método del Gradiente Conjugado
El método del gradiente conjugado es un método iterativo para resolver sistemas de ecuaciones lineales grandes y dispersos, que aparecen a menudo en problemas de optimización.

## Método de Newton
El método de Newton utiliza el gradiente y la matriz Hessiana de la función objetivo para encontrar los mínimos. Este método es conocido por su rápida convergencia cuando se encuentra cerca del mínimo.

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
Copiar código
pip install numpy scipy
```