# En este archivo estará la librería de funciones que se utilizarán en el programa principal

def calcular_poblacion(juveniles_iniciales, adultas_iniciales, tasa_reproduccion, tasa_conversion, tasa_supervivencia, epocas):
    """
    Calcula la población de ardillas a lo largo de varios años.
    
    Parámetros:
        juveniles_iniciales (int): Número inicial de ardillas juveniles.
        adultas_iniciales (int): Número inicial de ardillas adultas.
        tasa_reproduccion (float): Número promedio de juveniles generados por cada adulta.
        tasa_conversion (float): Proporción de juveniles que pasan a ser adultas.
        tasa_supervivencia (float): Proporción de adultas que sobreviven.
        anos (int): Número de años a calcular.
        
    Retorna:
        lista_poblaciones (list): Lista con las poblaciones totales de cada año.
    """
    # Valores iniciales
    juveniles = juveniles_iniciales
    adultas = adultas_iniciales

    lista_poblaciones = []

    for epocas in range(1, epocas + 1):
        # Cálculos
        juveniles_nuevas = adultas * tasa_reproduccion
        juveniles_que_pasan = juveniles * tasa_conversion
        adultas_sobrevivientes = adultas * tasa_supervivencia

        # Nuevos valores de juveniles y adultas
        juveniles = juveniles_nuevas
        adultas = juveniles_que_pasan + adultas_sobrevivientes

        # Población total
        poblacion_total = juveniles + adultas
        lista_poblaciones.append((epocas, juveniles, adultas, poblacion_total))
        # --- RESULTADOS ---
    print(f"{'Año':<5}{'Juveniles':<15}{'Adultas':<15}{'Población Total':<15}")
    for epocas, juveniles, adultas, total in lista_poblaciones:
        print(f"{epocas:<5}{int(juveniles):<15}{int(adultas):<15}{int(total):<15}")
    
    return 

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