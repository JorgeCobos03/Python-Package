import math

def himmelblau(x):
    return (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2

def grad_himmelblau(x):
    df_dx = 4 * x[0] * (x[0]**2 + x[1] - 11) + 2 * (x[0] + x[1]**2 - 7)
    df_dy = 2 * (x[0]**2 + x[1] - 11) + 4 * x[1] * (x[0] + x[1]**2 - 7)
    return [df_dx, df_dy]

def conjugate_gradient_method(f, grad_f, x0, tol1=1e-5, tol2=1e-5, tol3=1e-5, max_iter=1000):
    x = x0[:]
    grad = grad_f(x)
    s = [-g for g in grad]
    
    for k in range(max_iter):
        # Búsqueda de línea para encontrar λ
        def f_lambda(lmbda):
            x_new = [x[i] + lmbda * s[i] for i in range(len(x))]
            return f(x_new)
        
        lmbda = minimize_scalar(f_lambda).x
        
        x_new = [x[i] + lmbda * s[i] for i in range(len(x))]
        
        if all(abs(x_new[i] - x[i]) / (abs(x[i]) if abs(x[i]) > tol1 else 1) < tol2 for i in range(len(x))) \
                or math.sqrt(sum(g**2 for g in grad_f(x_new))) <= tol3:
            break
        
        grad_new = grad_f(x_new)
        beta = sum(grad_new[i]**2 for i in range(len(x))) / sum(grad[i]**2 for i in range(len(x)))
        
        s = [-grad_new[i] + beta * s[i] for i in range(len(x))]
        x, grad = x_new, grad_new
        
    return x

from scipy.optimize import minimize_scalar

# Ejemplo de uso:
x0 = [0.0, 0.0]
minimo = conjugate_gradient_method(himmelblau, grad_himmelblau, x0)
print(f"Resultado Gradiente Conjugado: {minimo}")
