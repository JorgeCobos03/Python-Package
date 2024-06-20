import numpy as np
import math

# Función de Himmelblau
def himmelblau(x):
    return (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2

# Gradiente de la función de Himmelblau
def grad_himmelblau(x):
    df_dx = 4 * x[0] * (x[0]**2 + x[1] - 11) + 2 * (x[0] + x[1]**2 - 7)
    df_dy = 2 * (x[0]**2 + x[1] - 11) + 4 * x[1] * (x[0] + x[1]**2 - 7)
    return np.array([df_dx, df_dy])

# Cálculo numérico de la matriz Hessiana
def hessian_matrix(f, x, deltaX=1e-5):
    fx = f(x)
    N = len(x)
    H = []
    for i in range(N):
        hi = []
        for j in range(N):
            if i == j:
                xp = x.copy()
                xn = x.copy()
                xp[i] = xp[i] + deltaX
                xn[i] = xn[i] - deltaX
                hi.append((f(xp) - 2*fx + f(xn)) / (deltaX**2))
            else:
                xpp = x.copy()
                xpn = x.copy()
                xnp = x.copy()
                xnn = x.copy()
                xpp[i] = xpp[i] + deltaX
                xpp[j] = xpp[j] + deltaX
                xpn[i] = xpn[i] + deltaX
                xpn[j] = xpn[j] - deltaX
                xnp[i] = xnp[i] - deltaX
                xnp[j] = xnp[j] + deltaX
                xnn[i] = xnn[i] - deltaX
                xnn[j] = xnn[j] - deltaX
                hi.append((f(xpp) - f(xpn) - f(xnp) + f(xnn)) / (4 * deltaX**2))
        H.append(hi)
    return np.array(H)

# Método de Newton
def newton_method(f, grad_f, x0, tol1=1e-5, tol2=1e-5, tol3=1e-5, max_iter=1000):
    x = np.array(x0)
    
    for k in range(max_iter):
        grad = grad_f(x)
        H = hessian_matrix(f, x)
        
        # Calcular la dirección de Newton
        H_inv = np.linalg.inv(H)
        p = -np.dot(H_inv, grad)
        
        # Búsqueda unidireccional para encontrar α
        def f_alpha(alpha):
            return f(x + alpha * p)
        
        alpha = minimize_scalar(f_alpha).x
        
        # Actualizar x
        x_new = x + alpha * p
        
        norm_x = np.linalg.norm(x)
        if norm_x == 0:
            norm_x = 1  # Evitar división por cero
        
        if np.linalg.norm(x_new - x) / norm_x < tol2 or np.linalg.norm(grad_f(x_new)) <= tol3:
            x = x_new
            break
        
        x = x_new
        
    return x

from scipy.optimize import minimize_scalar

# Ejemplo de uso:
x0 = [0.0, 0.0]
minimo = newton_method(himmelblau, grad_himmelblau, x0)
print(f"Resultado Método de Newton: {minimo}")
