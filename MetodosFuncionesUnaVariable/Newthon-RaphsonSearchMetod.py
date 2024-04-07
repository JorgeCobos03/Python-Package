import numpy as np
import matplotlib.pyplot as plt

class NewtonRaphsonSearch:
    def __init__(self, func, derivative, initial_guess):
        self.func = func
        self.derivative = derivative
        self.initial_guess = initial_guess

    def search(self, precision, max_iter=100):
        iterations = []
        x = self.initial_guess

        for _ in range(max_iter):
            x_next = x - self.func(x) / self.derivative(x)
            iterations.append(x_next)
            if abs(x_next - x) < precision:
                break
            x = x_next

        return iterations

def f1(x):
    return x**2 + 54/x

def f1_derivative(x):
    return 2*x - 54/x**2

def f2(x):
    return x**3 + 2*x - 3

def f2_derivative(x):
    return 3*x**2 + 2

def f3(x):
    return x**4 + x**2 - 33

def f3_derivative(x):
    return 4*x**3 + 2*x

def f4(x):
    return 3*x**4 - 8*x**3 - 6*x**2 + 12*x

def f4_derivative(x):
    return 12*x**3 - 24*x**2 - 12*x + 12

def caja(L):
    return (L * (20 - 2*L) * (10 - 2*L))*-1

def caja_derivative(L):
    return 200 - 120*L + 12*L**2

def lata_funcion(x):
    return 2 * np.pi * x ** 2 + (500 / x)

def lata_funcion_derivative(x):
    return 4 * np.pi * x - 500 / x**2

search_f1 = NewtonRaphsonSearch(f1, f1_derivative, 0.1)
search_f2 = NewtonRaphsonSearch(f2, f2_derivative, -5)
search_f3 = NewtonRaphsonSearch(f3, f3_derivative, -2.5)
search_f4 = NewtonRaphsonSearch(f4, f4_derivative, -1.5)
search_caja = NewtonRaphsonSearch(caja, caja_derivative, 2.5)  
search_lata = NewtonRaphsonSearch(lata_funcion, lata_funcion_derivative, 0.1)

precision_values = [0.5, 0.1, 0.01, 0.0001]

for precision in precision_values:
    plt.figure(figsize=(10, 6))

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
