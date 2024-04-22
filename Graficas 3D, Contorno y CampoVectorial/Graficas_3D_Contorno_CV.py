import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def f(x, y):
    return -x**4 + 4 * (x**2 - y**2)

def gradiente(func, x, y, h=0.01):
    df_dx = (func(x + h, y) - func(x - h, y)) / (2 * h)
    df_dy = (func(x, y + h) - func(x, y - h)) / (2 * h)
    return df_dx, df_dy

def plot_funciong(func, xlim=(-2, 2), ylim=(-2, 2), num_points=100):
    x = np.linspace(xlim[0], xlim[1], num_points)
    y = np.linspace(ylim[0], ylim[1], num_points)
    X, Y = np.meshgrid(x, y)
    Z = func(X, Y)
    U = np.zeros_like(X)
    V = np.zeros_like(Y)
    for i in range(num_points):
        for j in range(num_points):
            U[i, j], V[i, j] = gradiente(func, X[i, j], Y[i, j])
    
    # 3D
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='inferno')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D')
    plt.show()

    # CONTORNOS
    plt.figure(figsize=(10, 7))
    sns.set_style("white")
    plt.contour(X, Y, Z, cmap='inferno')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('CONTORNOS')
    plt.show()

    # CAMPO VECTORIAL
    plt.figure(figsize=(10, 7))
    sns.set_style("white")
    plt.quiver(X, Y, U, V)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('CAMPO VECTORIAL')
    plt.show()

plot_funciong(f)
