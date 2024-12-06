from sympy import symbols, Eq, solve

# Función para calcular el costo total
def costo_total(t, costo_inicial_mantenimiento, tasa_aumento_mantenimiento, 
                costo_inicial_software, tasa_aumento_software):
    return (costo_inicial_mantenimiento + tasa_aumento_mantenimiento * t +
            costo_inicial_software + tasa_aumento_software * t**2)

# Función para resolver la ecuación y formatear los resultados
def calcular_tiempo(costo_inicial_mantenimiento, tasa_aumento_mantenimiento, 
                    costo_inicial_software, tasa_aumento_software, limite_presupuestado):
    t = symbols('t')
    ecuacion = Eq(costo_total(t, costo_inicial_mantenimiento, tasa_aumento_mantenimiento, 
                              costo_inicial_software, tasa_aumento_software), limite_presupuestado)
    soluciones = solve(ecuacion, t)
    soluciones_validas = [sol for sol in soluciones if sol > 0]
    if soluciones_validas:
        tiempo = soluciones_validas[0]
        costo = costo_total(tiempo, costo_inicial_mantenimiento, tasa_aumento_mantenimiento, 
                            costo_inicial_software, tasa_aumento_software)
        return tiempo, costo
    else:
        return None, None

# Función para formatear la salida
def obtener_resultado(costo_inicial_mantenimiento, tasa_aumento_mantenimiento, 
                      costo_inicial_software, tasa_aumento_software, limite_presupuestado):
    tiempo, costo = calcular_tiempo(costo_inicial_mantenimiento, tasa_aumento_mantenimiento, 
                                    costo_inicial_software, tasa_aumento_software, limite_presupuestado)
    if tiempo is not None:
        return f"Tiempo estimado: {tiempo:.2f} años\nCosto total en ese tiempo: ${costo:,.2f}"
    else:
        return "No se encontró un tiempo que cumpla con el límite presupuestado."