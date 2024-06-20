import math

def himmelblau(x):
    return ((x[0]**2 + x[1] - 11)**2) + ((x[0] + x[1]**2 - 7)**2)

def regla_eliminacion(x1, x2, fx1, fx2, a, b):
    if fx1 > fx2:
        return x1, b
    if fx1 < fx2:
        return a, x2
    return x1, x2

def w_to_x(w, a, b):
    return w * (b - a) + a

def busquedaDorada(funcion, epsilon, a, b):
    PHI = (1 + math.sqrt(5)) / 2 - 1
    aw, bw = 0, 1
    Lw = 1
    k = 1
    
    while Lw > epsilon:
        w2 = aw + PHI * Lw
        w1 = bw - PHI * Lw
        aw, bw = regla_eliminacion(w1, w2, funcion(w_to_x(w1, a, b)), funcion(w_to_x(w2, a, b)), aw, bw)
        k += 1
        Lw = bw - aw
        
    return (w_to_x(aw, a, b) + w_to_x(bw, a, b)) / 2

def gradiente(f, x, deltaX=0.001):
    grad = []
    for i in range(len(x)):
        xp = x.copy()
        xn = x.copy()
        xp[i] = xp[i] + deltaX
        xn[i] = xn[i] - deltaX
        grad.append((f(xp) - f(xn)) / (2 * deltaX))
    return grad

def cauchy(funcion, x0, epsilon1, epsilon2, M, optimizador_univariable):
    terminar = False
    xk = x0
    k = 0
    
    while not terminar:
        grad = gradiente(funcion, xk)
        
        if math.sqrt(sum(g**2 for g in grad)) < epsilon1 or k >= M:
            terminar = True
        else:
            def alpha_function(alpha):
                return funcion([xk[i] - alpha * grad[i] for i in range(len(xk))])
            
            alpha = optimizador_univariable(alpha_function, epsilon=epsilon2, a=0.0, b=1.0)
            x_k1 = [xk[i] - alpha * grad[i] for i in range(len(xk))]
            
            if math.sqrt(sum((x_k1[i] - xk[i])**2 for i in range(len(xk)))) / (math.sqrt(sum(xk[i]**2 for i in range(len(xk)))) + 1e-5) <= epsilon2:
                terminar = True
            else:
                k += 1
                xk = x_k1
    
    return xk

x0 = [0.0, 0.0]
resultado = cauchy(himmelblau, x0, 0.001, 0.001, 100, busquedaDorada)
print(f"Resultado Cauchy: {resultado}")
