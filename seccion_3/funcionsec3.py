from sympy import symbols, Eq, solve

# Función para el costo cuadrático de Pepito_Perez
def costo_pepito_perez(t):
    return -2000 * t**2 + 20000 * t + 800000

# Función para el costo lineal de Interprase
def costo_interprase(t):
    return 850000 + 22000 * t

# Función para el costo lineal de Soluciones Express
def costo_soluciones(t):
    return 1150000 + 420 * t

# Resolver la ecuación cuadrática de Pepito_Perez para encontrar el tiempo
def calcular_tiempo_limite(limite):
    t = symbols('t', real=True)
    ecuacion = Eq(costo_pepito_perez(t), limite)
    soluciones = solve(ecuacion, t)
    # Filtrar soluciones válidas (tiempo positivo y real)
    soluciones_validas = [sol for sol in soluciones if sol.is_real and sol > 0]
    return soluciones_validas[0] if soluciones_validas else None

# Comparar los costos en el tiempo calculado
def comparar_costos(limite):
    t_max = calcular_tiempo_limite(limite)
    if t_max:
        ci = costo_interprase(t_max)
        cs = costo_soluciones(t_max)
        return t_max, ci, cs
    else:
        return None, None, None