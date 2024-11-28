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
    
    return lista_poblaciones