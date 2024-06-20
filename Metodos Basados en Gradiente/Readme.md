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

1. Inicializar $\mathbf{x}$ con un valor inicial $\mathbf{x}_0$.
2. Mientras no se cumpla el criterio de convergencia:
    - Calcular el gradiente $\nabla f(\mathbf{x})$.
    - Definir la dirección de búsqueda $\mathbf{d} = -\nabla f(\mathbf{x})$.
    - Usar la búsqueda dorada para encontrar el paso óptimo $\alpha$ que minimiza $f(\mathbf{x} + \alpha \mathbf{d})$.
    - Actualizar $\mathbf{x} \leftarrow \mathbf{x} + \alpha \mathbf{d}$.



## Método de Cauchy con Barzilai-Borwein
En este método, se utiliza una aproximación de Barzilai-Borwein para determinar el tamaño del paso. Esto permite una convergencia más rápida comparada con el método tradicional de Cauchy.

## Pseudocódigo
1. Inicializar $\mathbf{x}$ con un valor inicial $\mathbf{x}_0$.
2. Calcular el gradiente $\mathbf{g}_0 = \nabla f(\mathbf{x}_0)$.
3. Inicializar $\alpha$ con un valor pequeño.
4. Mientras no se cumpla el criterio de convergencia:
    - Actualizar $\mathbf{x}_{k+1} = \mathbf{x}_k - \alpha_k \mathbf{g}_k$.
    - Calcular $\mathbf{s}_k = \mathbf{x}_{k+1} - \mathbf{x}_k$.
    - Calcular $\mathbf{y}_k = \nabla f(\mathbf{x}_{k+1}) - \mathbf{g}_k$.
    - Actualizar $\alpha_{k+1} = \frac{\mathbf{s}_k^T \mathbf{y}_k}{\mathbf{y}_k^T \mathbf{y}_k}$.
    - Actualizar $\mathbf{g}_{k+1} = \nabla f(\mathbf{x}_{k+1})$.


## Método del Gradiente Conjugado
El método del gradiente conjugado es un método iterativo para resolver sistemas de ecuaciones lineales grandes y dispersos, que aparecen a menudo en problemas de optimización.

## Pseudocódigo
1. Inicializar $\mathbf{x}$ con un valor inicial $\mathbf{x}_0$.
2. Calcular el gradiente $\mathbf{g}_0 = \nabla f(\mathbf{x}_0)$.
3. Establecer la dirección inicial $\mathbf{d}_0 = -\mathbf{g}_0$.
4. Mientras no se cumpla el criterio de convergencia:
    - Calcular el paso óptimo $\alpha_k$.
    - Actualizar $\mathbf{x}_{k+1} = \mathbf{x}_k + \alpha_k \mathbf{d}_k$.
    - Calcular el nuevo gradiente $\mathbf{g}_{k+1} = \nabla f(\mathbf{x}_{k+1})$.
    - Calcular $\beta_k$ para la nueva dirección.
    - Actualizar $\mathbf{d}_{k+1} = -\mathbf{g}_{k+1} + \beta_k \mathbf{d}_k$.



## Método de Newton
El método de Newton utiliza el gradiente y la matriz Hessiana de la función objetivo para encontrar los mínimos. Este método es conocido por su rápida convergencia cuando se encuentra cerca del mínimo.

## Pseudocódigo
1. Inicializar $\mathbf{x}$ con un valor inicial $\mathbf{x}_0$.
2. Mientras no se cumpla el criterio de convergencia:
    - Calcular el gradiente $\nabla f(\mathbf{x})$.
    - Calcular la Hessiana $H(\mathbf{x})$.
    - Calcular la dirección de Newton $\mathbf{d} = -H(\mathbf{x})^{-1} \nabla f(\mathbf{x})$.
    - Determinar el paso $\alpha$ usando un método de línea de búsqueda.
    - Actualizar $\mathbf{x} \leftarrow \mathbf{x} + \alpha \mathbf{d}$.


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