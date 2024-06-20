import math

def himmelblau(x):
    return ((x[0]**2 + x[1] - 11)**2) + ((x[0] + x[1]**2 - 7)**2)

def gradiente(f, x, deltaX=0.001):
    grad = []
    for i in range(len(x)):
        xp = x.copy()
        xn = x.copy()
        xp[i] = xp[i] + deltaX
        xn[i] = xn[i] - deltaX
        grad.append((f(xp) - f(xn)) / (2 * deltaX))
    return grad

def barzilai_borwein_step(grad_prev, grad, x_prev, x):
    s = [x[i] - x_prev[i] for i in range(len(x))]
    y = [grad[i] - grad_prev[i] for i in range(len(x))]
    denom = sum(s[i] * y[i] for i in range(len(s)))
    if denom == 0:
        return 1  # Default step size
    alpha = sum(s[i] * s[i] for i in range(len(s))) / denom
    return alpha

def cauchy(funcion, x0, epsilon1, epsilon2, M):
    terminar = False
    xk = x0
    k = 0
    grad_prev = gradiente(funcion, xk)
    x_prev = xk
    
    while not terminar:
        grad = gradiente(funcion, xk)
        alpha = barzilai_borwein_step(grad_prev, grad, x_prev, xk)
        
        x_k1 = [xk[i] - alpha * grad[i] for i in range(len(xk))]
        
        if math.sqrt(sum(g**2 for g in grad)) < epsilon1 or k >= M:
            terminar = True
        else:
            k += 1
            x_prev, grad_prev = xk, grad
            xk = x_k1
    
    return xk

x0 = [0.0, 0.0]
resultado = cauchy(himmelblau, x0, 0.001, 0.001, 100)
print(f"Resultado Cauchy: {resultado}")
