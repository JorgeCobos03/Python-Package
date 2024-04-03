import numpy as np
import matplotlib.pyplot as plt

class ExhaustiveSearch:
    def __init__(self, func, lower_bound, upper_bound):
        self.func = func
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def search(self, precision):
        x = self.lower_bound
        x_values = []
        y_values = []
        visited_points = []

        while x <= self.upper_bound:
            x_values.append(x)
            y = self.func(x)
            y_values.append(y)
            visited_points.append((x, y))
            x += precision

        min_index = np.argmin(y_values)
        min_x = x_values[min_index]
        min_y = y_values[min_index]

        return x_values, y_values, min_x, min_y, visited_points

def f1(x):
    return x**2 + 54/x

def f2(x):
    return x**3 + 2*x - 3

def f3(x):
    return x**4 + x**2 - 33

def f4(x):
    return 3*x**4 - 8*x**3 - 6*x**2 + 12*x

def V(L):
    return 200 * L - 60 * L**2 + 4 * L**3

def lata_funcion(x):
    return 2 * np.pi * x ** 2 + (500 / x)

search_f1 = ExhaustiveSearch(f1, 0.1, 10)
search_f2 = ExhaustiveSearch(f2, -5, 5)
search_f3 = ExhaustiveSearch(f3, -2.5, 2.5)
search_f4 = ExhaustiveSearch(f4, -1.5, 3)
search_V = ExhaustiveSearch(V, 2, 3)  
search_lata = ExhaustiveSearch(lata_funcion, 0.1, 10)  

precision_values = [0.5, 0.1, 0.01, 0.0001]

for precision in precision_values:
    plt.figure(figsize=(10, 6))

    # f1
    plt.subplot(2, 3, 1)
    x_values, y_values, min_x, min_y, visited_points = search_f1.search(precision)
    plt.plot(x_values, y_values, label=f'Precision = {precision}')
    plt.scatter([p[0] for p in visited_points], [p[1] for p in visited_points], color='blue', alpha=0.3, label='Visited Points')
    plt.scatter(min_x, min_y, color='red', label=f'Mínimo en x ≈ {min_x:.4f}, f(x) ≈ {min_y:.4f}')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('f1(x) = x^2 + 54/x')
    plt.legend()
    plt.grid(True)

    # f2
    plt.subplot(2, 3, 2)
    x_values, y_values, min_x, min_y, visited_points = search_f2.search(precision)
    plt.plot(x_values, y_values, label=f'Precision = {precision}')
    plt.scatter([p[0] for p in visited_points], [p[1] for p in visited_points], color='blue', alpha=0.3, label='Visited Points')
    plt.scatter(min_x, min_y, color='red', label=f'Mínimo en x ≈ {min_x:.4f}, f(x) ≈ {min_y:.4f}')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('f2(x) = x^3 + 2x - 3')
    plt.legend()
    plt.grid(True)

    # f3
    plt.subplot(2, 3, 3)
    x_values, y_values, min_x, min_y, visited_points = search_f3.search(precision)
    plt.plot(x_values, y_values, label=f'Precision = {precision}')
    plt.scatter([p[0] for p in visited_points], [p[1] for p in visited_points], color='blue', alpha=0.3, label='Visited Points')
    plt.scatter(min_x, min_y, color='red', label=f'Mínimo en x ≈ {min_x:.4f}, f(x) ≈ {min_y:.4f}')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('f3(x) = x^4 + x^2 - 33')
    plt.legend()
    plt.grid(True)

    # f4
    plt.subplot(2, 3, 4)
    x_values, y_values, min_x, min_y, visited_points = search_f4.search(precision)
    plt.plot(x_values, y_values, label=f'Precision = {precision}')
    plt.scatter([p[0] for p in visited_points], [p[1] for p in visited_points], color='blue', alpha=0.3, label='Visited Points')
    plt.scatter(min_x, min_y, color='red', label=f'Mínimo en x ≈ {min_x:.4f}, f(x) ≈ {min_y:.4f}')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('f4(x) = 3x^4 - 8x^3 - 6x^2 + 12x')
    plt.legend()
    plt.grid(True)

    # lata
    plt.subplot(2, 3, 5)
    x_values, y_values, min_x, min_y, visited_points = search_lata.search(precision)
    plt.plot(x_values, y_values, label=f'Precision = {precision}')
    plt.scatter([p[0] for p in visited_points], [p[1] for p in visited_points], color='blue', alpha=0.3, label='Visited Points')
    plt.scatter(min_x, min_y, color='red', label=f'Mínimo en x ≈ {min_x:.4f}, f(x) ≈ {min_y:.4f}')
    plt.xlabel('Radio (x)')
    plt.ylabel('Área de Superficie')
    plt.title('Lata')
    plt.legend()
    plt.grid(True)

    # caja
    plt.subplot(2, 3, 6)
    L_values, V_values, max_L, max_V, visited_points = search_V.search(precision)
    plt.plot(L_values, V_values, label=f'Precision = {precision}')
    plt.scatter([p[0] for p in visited_points], [V(p[0]) for p in visited_points], color='blue', alpha=0.3, label='Visited Points')
    plt.scatter(max_L, max_V, color='red', label=f'Máximo en L ≈ {max_L:.2f}, V ≈ {max_V:.2f}')
    plt.xlabel('L')
    plt.ylabel('Volumen')
    plt.title('Caja')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()
