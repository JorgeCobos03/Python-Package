import numpy as np
import matplotlib.pyplot as plt

class SecantSearch:
    def __init__(self, func, initial_guess1, initial_guess2):
        self.func = func
        self.initial_guess1 = initial_guess1
        self.initial_guess2 = initial_guess2

    def search(self, precision, max_iter=100):
        iterations = []
        x0 = self.initial_guess1
        x1 = self.initial_guess2

        for _ in range(max_iter):
            x_next = x1 - (self.func(x1) * (x1 - x0)) / (self.func(x1) - self.func(x0))
            iterations.append(x_next)
            if abs(x_next - x1) < precision:
                break
            x0 = x1
            x1 = x_next

        return iterations

def f1(x):
    return x**2 + 54/x

def f2(x):
    return x**3 + 2*x - 3

def f3(x):
    return x**4 + x**2 - 33

def f4(x):
    return 3*x**4 - 8*x**3 - 6*x**2 + 12*x

def caja(L):
    return (L * (20 - 2*L) * (10 - 2*L))*-1

def lata_funcion(x):
    return 2 * np.pi * x ** 2 + (500 / x)

search_f1 = SecantSearch(f1, 0.1, 1)
search_f2 = SecantSearch(f2, -5, -4)
search_f3 = SecantSearch(f3, -2.5, -2)
search_f4 = SecantSearch(f4, -1.5, -1)
search_caja = SecantSearch(caja, 2, 3)  
search_lata = SecantSearch(lata_funcion, 0.1, 1)

precision_values = [0.5, 0.1, 0.01, 0.0001]

for precision in precision_values:
    plt.figure(figsize=(15, 10))

    # f1
    plt.subplot(2, 3, 1)
    iterations = search_f1.search(precision)
    x_values = np.linspace(0.01, 10, 1000)
    y_values = f1(x_values)
    plt.plot(x_values, y_values, label=f'Precision = {precision}')
    plt.scatter(iterations, [f1(x) for x in iterations], color='red', label=f'Iterations (Precision: {precision})')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('f1(x) = x^2 + 54/x')
    plt.legend()
    plt.grid(True)

    # f2
    plt.subplot(2, 3, 2)
    iterations = search_f2.search(precision)
    x_values = np.linspace(-5, 5, 1000)
    y_values = f2(x_values)
    plt.plot(x_values, y_values, label=f'Precision = {precision}')
    plt.scatter(iterations, [f2(x) for x in iterations], color='red', label=f'Iterations (Precision: {precision})')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('f2(x) = x^3 + 2x - 3')
    plt.legend()
    plt.grid(True)

    # f3
    plt.subplot(2, 3, 3)
    iterations = search_f3.search(precision)
    x_values = np.linspace(-2.5, 2.5, 1000)
    y_values = f3(x_values)
    plt.plot(x_values, y_values, label=f'Precision = {precision}')
    plt.scatter(iterations, [f3(x) for x in iterations], color='red', label=f'Iterations (Precision: {precision})')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('f3(x) = x^4 + x^2 - 33')
    plt.legend()
    plt.grid(True)

    # f4
    plt.subplot(2, 3, 4)
    iterations = search_f4.search(precision)
    x_values = np.linspace(-1.5, 3, 1000)
    y_values = f4(x_values)
    plt.plot(x_values, y_values, label=f'Precision = {precision}')
    plt.scatter(iterations, [f4(x) for x in iterations], color='red', label=f'Iterations (Precision: {precision})')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('f4(x) = 3x^4 - 8x^3 - 6x^2 + 12x')
    plt.legend()
    plt.grid(True)

    # lata
    plt.subplot(2, 3, 5)
    iterations = search_lata.search(precision)
    x_values = np.linspace(0.01, 10, 1000)
    y_values = lata_funcion(x_values)
    plt.plot(x_values, y_values, label=f'Precision = {precision}')
    plt.scatter(iterations, [lata_funcion(x) for x in iterations], color='red', label=f'Iterations (Precision: {precision})')
    plt.xlabel('Radio (x)')
    plt.ylabel('Área de Superficie')
    plt.title('Lata')
    plt.legend()
    plt.grid(True)

    # caja
    plt.subplot(2, 3, 6)
    iterations = search_caja.search(precision)
    L_values = np.linspace(2, 3, 1000)
    caja_values = caja(L_values)
    plt.plot(L_values, caja_values, label=f'Precision = {precision}')
    plt.scatter(iterations, [caja(x) for x in iterations], color='red', label=f'Iterations (Precision: {precision})')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Caja')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()
