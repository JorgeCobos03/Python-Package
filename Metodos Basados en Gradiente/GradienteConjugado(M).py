import math
import numpy as np
from scipy.optimize import minimize_scalar

def himmelblau(x):
    return (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2

def grad_himmelblau(x):
    df_dx = 4 * x[0] * (x[0]**2 + x[1] - 11) + 2 * (x[0] + x[1]**2 - 7)
    df_dy = 2 * (x[0]**2 + x[1] - 11) + 4 * x[1] * (x[0] + x[1]**2 - 7)
    return np.array([df_dx, df_dy])

def conjugate_gradient_method(f, grad_f, x0, tol1=1e-5, tol2=1e-5, tol3=1e-5, max_iter=1000):
    x = np.array(x0)
    grad = grad_f(x)
    s = -grad
    grad_prev = grad
    x_prev = x
    
    for k in range(max_iter):
        def f_alpha(alpha):
            return f(x + alpha * s)
        
        res = minimize_scalar(f_alpha, bounds=(0, 1), method='bounded')
        alpha = res.x
        
        x_new = x + alpha * s
        
        norm_x_new = np.linalg.norm(x_new)
        norm_x = np.linalg.norm(x)
        
        if norm_x == 0:
            norm_x = 1  # Evitar división por cero
        
        if norm_x_new == 0:
            norm_x_new = 1  
        
        if np.linalg.norm(x_new - x) / norm_x < tol2 or np.linalg.norm(grad_f(x_new)) <= tol3:
            return x_new.tolist()
        
        grad_new = grad_f(x_new)
        beta = np.dot(grad_new, grad_new) / np.dot(grad, grad)
        s = -grad_new + beta * s
        
        norm_s = np.linalg.norm(s)
        if norm_s > 1e10:
            s = s / norm_s
        
        x_prev, grad_prev = x, grad
        x, grad = x_new, grad_new
    
    return x.tolist()

x0 = [0.0, 0.0]
minimo = conjugate_gradient_method(himmelblau, grad_himmelblau, x0)
print(f"Resultado Gradiente Conjugado: {minimo}")
